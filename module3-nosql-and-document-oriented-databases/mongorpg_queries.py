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
print("CLIENT", type(client), client)
#print(dir(client))
print("DB NAMES:", client.database_names)

db = client.rpg_database #creating database
print("-----------")
print("DB:", type(db), db)
# Loop through each row in database, conver to dict, then insert
collection = db.charactercreator_character 
print("-------------")
print("COLLECTION:", type(collection), collection)

print("----------")
print("COLLECTIONS:")
print(db.list_collection_names)

collection.insert_one({
    "name": "Aliquid iste optio reiciendi",
    "level": 0,
    "exp": 0,
    "hp": 10,
})
print("DOCS",  collection.count_documents({})) #usually sekect count(distincy id) from charactercreator_character sql
print(collection.count_documents({"name": "Aliquid iste optio reiciendi"})) # usually select count(distinct id) form charactercreator_character


optio ={
    "name": "Optio dolorem ex a",
    "level": 0,
    "exp": 0,
    "hp": 10,
}



minus_c ={
    "name": "Minus c",
    "level": 0,
    "exp": 0,
    "hp": 10,
}


sit_ut ={
    "name": "Sit ut repr",
    "level": 0,
    "exp": 0,
    "hp": 10,
}


character_team = [optio, minus_c, sit_ut, ]
collection.insert_many(character_team)

print("DOCS:", collection.count_documents({})) #SELECT count(distinct id) from charactercreator_character


ali = list(collection.find({"name": "Aliquid iste optio reiciendi"}))

print(ali[0]["_id"]) #> ObjectId('5ebc64d7ad9e6c84d14dd2bc')
#print(len(ali)[0]["name"]) having problems running this line...

#collection.insert_one({"_id": "OURVAL", "name":"TEST"})
#can overwrie the _id not insert duplicate _id values

strong = list(collection.find({"level": {"Sgte": 0}}))

print("Success!")
print(db.character_df)
print(db.armory_df)


### I enjoyed working with Mongo. It felt a little easier to create the database. Things went smoother. I'd say.