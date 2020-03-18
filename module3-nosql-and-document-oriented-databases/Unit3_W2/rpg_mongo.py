#rpg_mongo.py

import pymongo
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

#connecting to db

DB_FILEPATH = 'rpg_db.sqlite3'
connect = sqlite3.connect('rpg_db.sqlite3')
cursor = connect.cursor()
print("CONNECT:", connect)

db = client.rpg_db


armor_item = """
SELECT
	*
FROM 
	armory_item
"""
leet_items = cursor.execute(armor_item).fetchall()

collection = db.rpg_items
print("----------------")
print("COLLECTION:", type(collection), collection)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

for n in leet_items:
    collection.insert_one({
        "item_id":n[0],
        "name": n[1],
        "weight": n[2],
        "value": n[3]
    })

        