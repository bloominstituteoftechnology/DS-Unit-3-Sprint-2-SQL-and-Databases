# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

#mongodb+srv://Ekram49:<password>@cluster0-jclao.mongodb.net/test?retryWrites=true&w=majority
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)



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
    "other_attr":{
        "a":1,
        "b":[1,2,3]
    }
})

warturtle = {
    "name": "Warturtle",
    "level": 90,
    "exp": 100,
    "hp": 1000,
}

jigglypuff = {
    "name": "Jigglypuff",
    "level": 99,
    "exp": 100000000000,
    "hp": 500,
}

Rayquaza = {
    "name": "Rayquaza",
    "level": 99,
    "exp": 1000,
    "hp": 1000,
}


team = [warturtle, jigglypuff, Rayquaza]
collection.insert_many(team)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

print("DOCS:", collection.count_documents({}))
# SELECT COUNT(id) from pokemon

print("PIKAS", collection.count_documents({"name": "Pikachu"}))
# SELECT COUNT(id) from pokemon WHERE name = "Pikachu"

pikas = list(collection.find({"name": "Pikachu"}))
# SELECT * FROM pokemon WHERE name = "pikachu"

print(pikas)

strong_pokemon = list(collection.find({"level": {"$gte": 70}}))
# SELECT * FROM pokemon WHERE level >= 70
print("HIGH LEVEL POKEMON", strong_pokemon)

