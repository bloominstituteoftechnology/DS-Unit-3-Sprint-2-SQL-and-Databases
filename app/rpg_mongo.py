# app/rpg_mongo.py

import pymongo
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
load_dotenv()

# RPG DB filepath

RPG_FILEPATH = os.path.join(os.path.dirname(__file__), '..','data', 'rpg_db.sqlite3')
sq_connection = sqlite3.connect(RPG_FILEPATH)
sq_cursor = sq_connection.cursor()


#create table

table = 'SELECT * FROM charactercreator_character;'
characters = sq_cursor.execute(table).fetchall()
print('---------------')
print(characters[:2])

#schema

print("_______________________")
print("Schema:", sq_cursor.execute('PRAGMA table_info(charactercreator_character);').fetchall())

# creating dataframe

characters_df = pd.DataFrame(characters)
print("-----------------")
print("column names", characters_df.columns)

# renaming column names

column_names = {
    0: "character_id",
    1: "name",
    2: "level",
    3: "exp",
    4: "hp",
    5: "strength",
    6: "intelligence",
    7: "dexterity",
    8: "wisdom"
}

characters_df = characters_df.rename(columns=column_names)
print("_______________________")
print("updated column names:", characters_df.columns)

# get dictionary of characters

dictionary_of_characters = characters_df.to_dict(orient='records')

# mongo db

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")


#mongodb+srv://Ekram_mongo:<password>@cluster0-t4zhg.mongodb.net/test?retryWrites=true&w=majority
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)


##################################################
db = client.rpg_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.rpg_character # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)


collection.insert_many(dictionary_of_characters)
print("----------------")

