import pandas as pd
import sqlite3
import pymongo
import json


# Connect to mongodb
client = pymongo.MongoClient("mongodb://admin:<PASSWORD>@cluster0-shard-00-00-fvpwm.mongodb.net:27017,cluster0-shard-00-01-fvpwm.mongodb.net:27017,cluster0-shard-00-02-fvpwm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Connect to rpg_db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# List table names
table_names = ['charactercreator_character', 'charactercreator_character_inventory',
               'charactercreator_mage', 'charactercreator_thief', 'charactercreator_cleric',
               'charactercreator_fighter', 'charactercreator_necromancer',
               'armory_item', 'armory_weapon']

def to_mongo(table):
    '''Convert sqlite3 tables to mongodb objects'''
    # Load sqlite3 data into pandas dataframe
    df = pd.read_sql_query(f'SELECT * FROM {table};', con=sl_conn)

    # Convert dataframe to JSON to work with mongodb
    data = json.loads(df.to_json(orient='records'))

    # Add table data to mongodb
    my_col = db[table]
    my_col.insert(data)

# Insert data into mongodb
for t in table_names:
    to_mongo(t)
