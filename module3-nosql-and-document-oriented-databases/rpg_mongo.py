# How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
# I would say MongoDB was definitely more flexible than PostgreSQL when it came to inserting the data into the
# database. I still need to practice these steps for both of them, but in my opinion I feel like
# MongoDB would be a preferred database for future projects since I was having some difficulties with PostgreSQL.

import pymongo
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd


# construct a path to wherever your sql3 database exists and create a connection to DB
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
sqlite_connection = sqlite3.connect(DB_FILEPATH)
# sqlite_connection.row_factory = sqlite3.Row

# construct the cursor for sqlite3
sqlite_cursor = sqlite_connection.cursor()

# get the characters table from the sqlite3 database file
get_characters = """SELECT * FROM charactercreator_character"""
characters = sqlite_cursor.execute(get_characters).fetchall()

# print(characters[:5])

# get the schema from the data base to view the column headers
print("_______________________")
print("Schema:", sqlite_cursor.execute('PRAGMA table_info(charactercreator_character);').fetchall())

# Need to transform the data so that we can add a list of dictionaries to update MongoDB
# create a dataframe from the characters list
characters_df = pd.DataFrame(characters)
print("_______________________")
print("column names:", characters_df.columns)

# the columns are a number range so will need to rename the columns to improve
# the insertion of data into MongoDB
column_names = {
    0: "character_id",
    1: "name",
    2: "level",
    3: "exp",
    4: "hp",
    5: "strength",
    6: "intelligence",
    7: "dexterity",
    8: "wisdom",
}

characters_df = characters_df.rename(columns=column_names)
print("_______________________")
print("updated column names:", characters_df.columns)

# move the dataframe to give us a dictionary for each row
dictionary_of_characters = characters_df.to_dict(orient='records')

# connect to mongo database so we can transfer over the data from characters
# dictionary that we got from sqlite3 db.
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
# MONGO_URL = os.getenv("MONGO_URL", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# use the connection urit to connect to the mongoDB
client = pymongo.MongoClient(connection_uri)

# create the database inside mongo connection
db = client.rpg  # "test_database" or whatever you want to call it

# create the collection 
collection = db.rpg_characters  # "pokemon_test" or whatever you want to call it

# insert our characters dictionary into the collection
collection.insert_many(dictionary_of_characters)
