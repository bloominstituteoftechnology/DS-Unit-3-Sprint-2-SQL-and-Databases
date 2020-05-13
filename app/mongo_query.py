# app/mongo_queries.py
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
#mongodb+srv://user123:<password>@cluster0-brbdg.mongodb.net/test?retryWrites=true&w=majority
#client = pymongo.MongoClient("mongodb+srv://user123:<password>@cluster0-brbdg.mongodb.net/test?retryWrites=true&w=majority")
#db = client.test
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
#print(dir(client))
print("DB NAMES:", client.list_database_names()) #> ['admin', 'local']
db = client.ds14_db # "ds14_db" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)
collection = db.ds14_pokemon_collection # "ds14_collection" or whatever you want to call it
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
    "fav_icecream_flavors":["vanila_bean", "choc"],
    "stats":{"a":1,"b":2,"c":[1,2,3]}
})
print("DOCS:", collection.count_documents({})) # SELECT count(distinct id) from pokemon
print(collection.count_documents({"name": "Pikachu"})) # SELECT count(distinct id) from pokemon WHERE name = "Pikachu"
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
blastoise = {
    "name": "Blastoise",
    "lvl": 70, # OOPS we made a mistake with the structure of this dict
}
charmander = {
    "nameeeeeee": "Charmander",
    "level": 70,
    "random_stat": {"a":2}
}
skarmory = {
    "name": "Skarmory",
    "level": 22,
    "exp": 42000,
    "hp": 85,
    "strength": 750,
    "intelligence": 8,
    "dexterity": 57
}
cubone = {
    "name": "Cubone",
    "level": 20,
    "exp": 35000,
    "hp": 80,
    "strength": 600,
    "intelligence": 60,
    "dexterity": 200,
    "wisdom": 200
}
scyther = {
    "name": "Scyther",
    "level": 99,
    "exp": 7000,
    "hp": 40,
    "strength": 50,
    "intelligence": 40,
    "dexterity": 30,
    "wisdom": 57
}
slowpoke = {
    "name": "Slowpoke",
    "level": 1,
    "exp": 100,
    "hp": 80,
    "strength": 100,
    "intelligence": 10,
    "dexterity": 50,
    "wisdom": 200
}
pokemon_team = [mewtwo, blastoise, skarmory, cubone, scyther, slowpoke, charmander]
collection.insert_many(pokemon_team)
print("DOCS:", collection.count_documents({})) # SELECT count(distinct id) from pokemon
#collection.insert_one({"_id": "OURVAL", "name":"TEST"})
# can overwrite the _id but not insert duplicate _id values
#breakpoint()
pikas = list(collection.find({"name": "Pikachu"})) # SELECT * FROM pokemon WHERE name = "Pikachu"
print(len(pikas), "PIKAS")
print(pikas[0]["_id"]) #> ObjectId('5ebc31c79c171e43bb5ed469')
print(pikas[0]["name"])
strong = list(collection.find({"level": {"$gte": 60}}))
# TODO: also try to account for our mistakes "lvl" vs "level"