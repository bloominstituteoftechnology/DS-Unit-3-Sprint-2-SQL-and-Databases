
# app/mongo_queries.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = MongoClient("mongodb+srv://<username>:<password>@cluster0-6sjdp.mongodb.net/<dbname>?retryWrites=true&w=majority")

print("----------------")
print("CLIENT:", type(client), client)

breakpoint()

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
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

bulbasaur = {
   "name": "Bulbasaur",
   "type": "grass",
   "moves":["Leech Seed", "Solar Beam"]
}

eevee = {
    "name": "Eevee",
    "level": 40,
    "exp": 7500,
    "hp": 120,
}

team = [bulbasaur, eevee]
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))