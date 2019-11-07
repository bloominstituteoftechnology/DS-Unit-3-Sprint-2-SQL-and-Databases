import pymongo, json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:U2BpmUqX1eqhXP2p@playground-plblg.mongodb.net/test?retryWrites=true&w=majority")
db = client["test"]

# Make two collections for weapons and characters
coll_char = db["rpg_char"]
coll_wpn  = db["rpg_wpn" ]

# Load JSON file
with open("rpg_data.json") as f:
    json_rpg = json.load(f)

# List comprehension to get list of all characters'/weapons' values
json_char = [i["fields"] for i in json_rpg if i["model"] == "charactercreator.character"]
json_wpn  = [i["fields"] for i in json_rpg if i["model"] == "armory.weapon"]

# Insert into DB
coll_char.insert_many(json_char)
coll_wpn.insert_many(json_wpn)

# Search for all characters with inventory length == 4
print(list(coll_char.find({"inventory": { "$size": 4}})[:10]))
