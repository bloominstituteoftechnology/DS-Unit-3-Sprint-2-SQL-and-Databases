# app/rpg_mongo.py

import pymongo
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
load_dotenv()

DB_USER = os.getenv("RPG_MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("RPG_MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("RPG_MONGO_CLUSTER_NAME", default="OOPS")

#mongodb+srv://Ekram_mongo:<password>@cluster0-t4zhg.mongodb.net/test?retryWrites=true&w=majority
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

RPG_FILEPATH = os.path.join(os.path.dirname(__file__), '..','data', 'rpg_db.sqlite3')

connection = sqlite3.connect(RPG_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

table = 'SELECT * FROM charactercreator_character;'
content = cursor.execute(table).fetchall()
print('---------------')
print(content)

##################################################
db = client.rgb_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.charactercreator_character # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

column_names = ['id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']

df = pd.DataFrame(content, columns=column_names)
print(df.head())


collection.insert_many(df.to_dict('records'))
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())