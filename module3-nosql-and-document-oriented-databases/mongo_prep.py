# mongo_prep.py


import os
import pymongo
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

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection = db.pokemon
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

print(collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))

#
# INSERTS
#

mewtwo = {
    "name": "Mewtwo",
    "level": 100,
    "exp": 76000000000,
    "hp": 450,
    "strength": 550,
    "intelligence": 450,
    "dexterity": 300,
    "wisdom": 575
}

pikachu = {
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
}

blastoise = {
    "name": "Blastoise",
    "lvl": 70,
}

characters = [mewtwo, pikachu, blastoise]

print("INSERT ONE AT A TIME...")
for character in characters:
    print(character["name"])
    collection.insert_one(character)

print(collection.count_documents({}), "DOCS")
print(collection.count_documents({"level": {"$gte": 50}}), "ABOVE 50")
print(collection.count_documents({"name": "Pikachu"}))

pikas_cursor = collection.find({"name": "Pikachu"})
pikas = list(pikas_cursor)
print(len(pikas), "PIKAS")

print("INSERT MANY...")

db.things.insert_one({"thing":"one"})
db.things.insert_many([{"thing":"one"}, {"thing": "two"}])
print(db.things.count_documents({"thing": "one"}))


#try:
#    collection.insert_many(characters)
#except Exception as err:
#    print(err)
#    print("...")
#
#    for char in characters:
#        char["caught_at"] = str(datetime.now())
#    print(characters[0])
#    collection.insert_many(characters)
#
#print(collection.count_documents({"name": "Pikachu"}))