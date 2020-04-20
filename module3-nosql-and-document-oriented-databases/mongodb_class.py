import pymongo
import urllib
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_PW = os.getenv("MONGO_PW")
pw = urllib.parse.quote_plus(MONGO_PW)
mongo_url = "mongodb+srv://alexmjn:" + pw + "@cluster0-semjk.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url, connect = False)

db = client.new_test
print(db.list_collection_names())

collection = db.pokemon
print(collection)
print(db.list_collection_names())

print(collection.count_documents({}))
print(collection.count_documents({"name":"Pikachu"}))

pika = {
    "name":"Pikachu",
    "level":"30",
    "hp":"460"
}

collection.insert_one(pika)
print(collection)
print(db.list_collection_names())

print(collection.count_documents({}))
print(collection.count_documents({"name":"Pikachu"}))

#once we insert a pikachu in memory, the collection persists.
# running this script multiple times outputs multiple pikachus.
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
    #look at lvl vs level: mongodb/nosql vs sql
    #no enforcement.
}
characters = [mewtwo, pikachu, blastoise]

print("INSERT ONE AT A TIME...")
for character in characters:
    print(character["name"])
    collection.insert_one(character)

#print("INSERT MANY...")
#collection.insert_many(characters)

print("----------------")
print("COUNT ALL DOCUMENTS:")
print(collection.count_documents({}))
print("COUNT ALL PIKACHUS:")
print(collection.count_documents({"name": "Pikachu"}))
print("COUNT ALL HIGH LEVELS:")
#{"date": {"$lt": d}}
print(collection.count_documents({"level": {"$lt": 40}}))
print("COUNT ALL HIGH INTEL:")
print(collection.count_documents({"intelligence": {"$gt": 400}}))
print("COUNT ATTR THAT DOESNT EXIST:")
print(collection.count_documents({"color": "red"}))

# note flexibility of mongodb querying
# stuff operates on the collection object, in general.
# each object looks like a dictionary.

# yep - each comes back as a class: dict. key-value pairs
# between attributes and the attribute names.

print("-----------")
print("LOOPING THROUGH ALL THE PIKAS!")
pikas_cursor = collection.find({"name": "Pikachu"})
print(type(pikas_cursor))
#pikas = list(pikas_cursor)
#print(len(pikas), "PIKAS")
#print(len(pikas_cursor), "PIKAS")
for pika in pikas_cursor:
    #print(pika)
    #print(type(pika))
    print(pika["name"], pika["level"])
    print("---")
