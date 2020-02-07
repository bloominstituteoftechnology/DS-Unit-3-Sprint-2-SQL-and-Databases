import pymongo

connection_uri = 'mongodb+srv://QgdR42Ke:0kHlbksI4LvZ5GEg@cluster0-wre3a.mongodb.net/test?retryWrites=true&w=majority'
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

attackers = collection.find({"attack": {'$gt':60}})
for attacker in attackers:
    print(attacker)