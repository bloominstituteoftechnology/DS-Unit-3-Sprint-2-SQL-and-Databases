import sqlite3
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    #This is boiler plate for connecting to mongodb
    USER = os.getenv('MONGO_USER', default = 'oops')
    PASSWORD = os.getenv('MONGO_PASSWORD', default = 'oops')
    CLUSTER = os.getenv('MONGO_CLUSTER', default = 'oops')

    uri = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.mongodb.net/test?retryWrites=true&w=majority'
    
    #connecting to the client
    client = pymongo.MongoClient(uri)

    #naming and creating the database. Future Me: This is the only call you 
    #need, and you can choose what ever name you want. I chose rpg_db
    db = SqliteToMongo(client = client, name = 'rpg_db')

    print('Sanity Checks')
    print('-------------------------------------------------------------------')
    print('URI:', uri)
    print('CLIENT:', client)
    print('DB:', db)
    print('-------------------------------------------------------------------')

    LITE_FILEPATH = os.path.join(os.path.dirname(__file__), 'data', 
                                'rpg_db.sqlite3')

    # where the rubber hits the road
    db.clone_sql_like(LITE_FILEPATH)

    #Sanity checks that it worked
    con = sqlite3.connect(LITE_FILEPATH)
    cur = con.cursor()

    qry = '''
    SELECT count(*) as table_count 
    FROM sqlite_master
    WHERE type='table';
    '''

    print('Sanity Check for 1:1 tables to collection creation')
    print('-------------------------------------------------------------------')
    print('SQLite number of tables:', cur.execute(qry).fetchone()[0])
    print('MongoDB number of tables:', len(db.list_collection_names()))
    print('-------------------------------------------------------------------')

    for tab in db.tables:
        print('Sanity Check for ' + tab + ' length')
        print('-------------------------------------------------------------------')

        qry = 'SELECT count(*) as row_count FROM ' + tab + ';'

        print('SQLite number of tables:', cur.execute(qry).fetchone()[0])
        print('MongoDB number of tables:', db[tab].count_documents({}))

class SqliteToMongo(pymongo.database.Database):

    def clone_sql_like(self, filepath):

        #boilerplate sqlite
        # thought about making these class variables, but decided against it
        # I'm likely only using them this once
        lite_con = sqlite3.connect(filepath)
        lite_con.row_factory = sqlite3.Row
        lite_cur = lite_con.cursor()

        table_name_query = '''
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        '''

        resp = lite_cur.execute(table_name_query).fetchall()

        #I want a list of strings, not tuples lets use list comp
        #to do it. Making this class variable because I'm lazy and want to use
        #it later
        self.tables = [tup[0] for tup in resp]

        for tab in self.tables:
            
            # using this rather than subscripting method (db['necromancers'])
            # because it will create an empty collection and I'm trying to
            # clone my sqlite database
            collection = self.create_collection(tab)

            lite_data = lite_cur.execute('SELECT * FROM ' + tab + ';').fetchall()
            
            # Ignore it if the list is empty
            if lite_data:
                #this is a list of sqlite rows, lets just turn them into dicts
                data = [dict(row) for row in lite_data]

                collection.insert_many(data)
            
        lite_cur.close()
        lite_con.close()

    def clone_mongo_like(self, filepath):
        # TODO Stretch: can I make my clone more mongo like?
        pass

if __name__ == "__main__":
    main()