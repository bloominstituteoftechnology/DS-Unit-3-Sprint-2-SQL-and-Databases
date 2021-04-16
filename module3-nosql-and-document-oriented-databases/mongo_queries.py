# mongo_queries.py


import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime


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

db = client.test_database
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))

collection.insert_one({"name": "Blastoise", "lvl": 70})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Blastoise"}))

pikas_cursor = collection.find({"name": "Pikachu"})
for pika in pikas_cursor:
    print(pika)

new_objects = [
    {"name": "Bulbasaur", "attack": 70},
    {"name": "Charmander", "attack": 100},
    {"name": "Jigglypuff", "attack": 50},
]
collection.insert_many(new_objects)
print("DOCS:", collection.count_documents({}))

# which pokemon have an attack greater than 60?
attackers = collection.find({"attack": {"$gt": 60}})
for attacker in attackers:
    print(attacker)