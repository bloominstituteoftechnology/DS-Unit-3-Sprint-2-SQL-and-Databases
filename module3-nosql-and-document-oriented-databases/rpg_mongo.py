import pymongo
import sqlite3
import json
import pandas as pd

# Connect to mongodb
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-dyztz.mongodb.net:27017,cluster0-shard-00-01-dyztz.mongodb.net:27017,cluster0-shard-00-02-dyztz.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Connect to rpg db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# List of table names
tables = ['charactercreator_character', 'charactercreator_character_inventory', 'charactercreator_mage',
          'charactercreator_thief', 'charactercreator_cleric', 'charactercreator_fighter',
          'charactercreator_necromancer', 'armory_item', 'armory_weapon']


def convert_to_mongo(table_name):
    """Function to convert sqlite3 table into mongodb collection"""
    df = pd.read_sql_query(f'SELECT * FROM {table_name};', con=sl_conn)
    data = json.loads(df.to_json(orient='records'))
    new_col = db[table_name]
    new_col.insert(data)


# Load rpg data into mongodb
for table in tables:
    convert_to_mongo(table)
