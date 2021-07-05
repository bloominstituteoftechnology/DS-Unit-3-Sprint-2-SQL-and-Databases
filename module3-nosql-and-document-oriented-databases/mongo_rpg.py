# module3-nosql-and-document-oriented-databases/mongo_rpg.py

import pymongo
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
from dotenv import load_dotenv


# Create pandas dataframes from RPG database tables.
FILEPATH = os.path.dirname(__file__)
DB_FILEPATH = os.path.join(FILEPATH, "..", "module1-introduction-to-sql", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

query = 'SELECT * FROM charactercreator_character;'
character_df = pd.read_sql_query(query, connection)

query = 'SELECT * FROM armory_item;'
armory_df = pd.read_sql_query(query, connection)

cursor.close()
connection.close()

# Move data into mongo database
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

db = client.rpg_database 

# Loop through each row in database, conver to dict, then insert
collection = db.charactercreator_character 
for _, row in character_df.iterrows():
    collection.insert_one(row.to_dict())

collection = db.armory_item
for _, row in armory_df.iterrows():
    collection.insert_one(row.to_dict())

print("Success!")
