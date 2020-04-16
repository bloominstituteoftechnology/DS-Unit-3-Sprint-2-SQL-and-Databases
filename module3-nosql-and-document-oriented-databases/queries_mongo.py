import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
# MONGO_URL = os.getenv("MONGO_URL", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
# connection_uri = "mongodb+srv://jsmaz:vennitio@cluster0-zusxi.mongodb.net/test?retryWrites=true&w=majority"

print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
# client = pymongo.MongoClient(MONGO_URL)
print("----------------")
print("CLIENT:", type(client), client)


db = client.inclass_db_ds13  # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test  # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())  # won't see until after inserting data

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "other_attr": {
        "a": 1,
        "b": [1, 2, 3]
    }
})

warturtle = {
    "name": "Warturtle",
    "level": 90,
    "exp": 100,
    "hp": 1000
}

mewtwo = {
    "name": "Mewtwo",
    "level": 99,
    "exp": 100000000,
    "hp": 500
}

bulbusaur = {
    "name": "Bulbusaur",
    "level": 30,
    "exp": 4450000000,
    "hp": 500,
    "learned_moves": {
        "flamethrower": 30,
        "fly": 42
    }
}

swampert = {
    "name": "Kiplar",
    "level": 100,
    "exp": 1059860,
    "hp": 361
}

snorlax = {
    "name": "snorlax",
    "level": 100,
    "exp": 1059999,
    "hp": 500
}

team = [warturtle, mewtwo, bulbusaur, swampert, snorlax]
collection.insert_many(team)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())  # won't see until after inserting data

print("DOCS:", collection.count_documents({}))
# SELECT count(id) from pokemon

print("PIKAS:", collection.count_documents({"name": "Pikachu"}))
# SELECT count(id) from pokemon WHERE name = "Pikachu"

pika = collection.find_one({"name": "Pikachu"})
# SELECT * FROM pokemon WHERE name = "Pikachu" LIMIT 1
print(pika)

pikas = list(collection.find({"name": "Pikachu"}))
# SELECT * FROM pokemon WHERE name = "Pikachu"
print(pikas)

strong_pokemon = list(collection.find({"level": {"$gte": 70}}))
# SELECT * FROM pokemon WHERE level >= 70
print("HIGH LEVEL POKEMON", strong_pokemon)
