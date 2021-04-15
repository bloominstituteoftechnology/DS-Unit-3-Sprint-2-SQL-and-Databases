import os
import sqlite3
import pandas as pd
import pymongo
from dotenv import load_dotenv


'''
"How was working with MongoDB different from working with PostgreSQL?
What was easier, and what was harder?"

I would say that my biggest hurdle was simply figuring out how to get
data into each system, once I was past that and knew the steps, they're
kind of the same in terms of ease of use.

Kind of.

One thing I noticed about Mongo is that it really doesn't give a damn
about the rules. You can access (and even create if it doesn't exist
already) collections fairly easily, and it doesn't seem to mind what
data you feed into it all that much.

That said, that can also be a hinderance when you accidentally throw,
say, a cleric's data into the fighters collection and it won't raise an
error about how you messed up. Definitely gives me javascript vibes,
and not in a good way.

That said, not having to learn SQL is a bonus, as trying to suss out
how proper querying works and taking the time to learn the language can
be cumbersome. Thankfully, pandas does have some stuff which makes data
flow a bit simpler.

All in all, I can't really gauge which one is easier or harder,
but I will say that I like SQLite, and by association postgres, better.
I've gotten used to SQL and its querying, and while it can be a bit
finnicky sometimes, I like how it's structured and easily readable.

And how you have to yell it.

SELECT!! FROM!!! WHILE!!!!
'''

# Set up .env variables to connect to postgres later
envpath = os.path.join(os.getcwd(),'..', '.env')
# print(envpath)
load_dotenv(envpath)

# grab .env data for mongo database for later
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME')
DB_USER = os.getenv('MONGO_USER')
DB_PASSWORD = os.getenv('MONGO_PASSWORD')

# grab filepath for rpg sqlite db
RPG_FILEPATH = os.path.join(os.getcwd(),'..',
'module1-introduction-to-sql','rpg_db.sqlite3')
# print(RPG_FILEPATH)

# Connect first to the RPG database and pull data from it to
# transfer it to postgres
conn = sqlite3.connect(RPG_FILEPATH)
print('CONNECTION IN:', conn)

def q(q_query, q_conn):
    return pd.read_sql(q_query, q_conn)
# Get all tables in the sqlite database
q_in = 'SELECT name FROM sqlite_master WHERE type = "table";'

rpg_names = q(
    q_in, conn
)

# put them into a list
rpg_names = list(rpg_names['name'].values)
rpg_tables = {}
print(rpg_names)

# get each table as a dataframe to post to nosqr
for table in rpg_names:
    q_in = 'SELECT * FROM ' + table
    rpg_tables[table] = q(q_in, conn)
    print(rpg_tables[table].head())

conn.commit()
conn.close()

print('CONNECTION CLOSED:',conn)

# All data grabbed from sqlite, now to post to MongoDB

print('CONNECTING TO MONGODB...')
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}-siyeu.mongodb.net/test?retryWrites=true&w=majority"
print('------------------------')
print('URI:',connection_uri)

client = pymongo.MongoClient(connection_uri)
print('------------------------')
print('CLIENT:', type(client), client)

db = client.rpg_db
print('------------------------')
print('DB:', type(db), db,'\n\n')

print(f'List of collections in database:\n{db.list_collection_names()}')

# put the tables from sqlite into collections in Mongo
for table in rpg_names:
    # MongoDB usually creates a collection when it's first referenced
    # but I don't think I can say collection = db.table
    # because it won't use the value of table, it'll try to create a
    # collection called table, So I need to use
    # db.create_collection.-
    
    # check if the collection with that name already exists and
    # replace it if need be
    if table in db.list_collection_names():
        print(f'Collection {table} already exists: {type(db[table])}')
        db[table].drop()
    # print(f'Does collection {table} exist? {table in db.list_collection_names()}')
    collection = db.create_collection(table)

    # I need to de-dataframe-ize the stored dataframes I have into
    # dict entries stored in lists
    # print(rpg_tables[table].head())

    # Reset to_mongo beforehand to avoid bad stuff happening
    to_mongo = None
    
    # check if the dataframe is empty and don't transfer it if it is
    if not rpg_tables[table].empty:
        # my reasoning behind this is that mongo doesn't really care
        # that much about documents not existing beforehand
        # so whatever functions designed to add info to documents
        # don't really fail if it's not there; so we don't need empty
        # dataframes because we'll just assume that they're set up the
        # way we need them to be when the time comes to add data.
        to_mongo = rpg_tables[table].to_dict('records')
    print(to_mongo)

    if to_mongo is not None:
        collection.insert_many(to_mongo)

# That should create collections that are equal to the tables
# of the sqlite database containing documents which are equal to
# the values of the tables.