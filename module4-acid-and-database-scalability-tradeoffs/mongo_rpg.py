# mongo_rpg.py


# Questions:

# 1. How many total Characters are there?
# 2. How many of each specific subclass?
# 3. How many total items?
# 4. How many of the Items are weapons? How many are not?
# 5. How many Items dow each character have? (Return first 20 rows)
# 6. How many Weapons does each character have? (Return first 20 rows)
# 7. On average, how many Items does each Character have?
# 8. On average, how many Weapons does each character have?


# Answers:

# 1. 302 Characters
# 2. 75 Clerics
# 2. 68 Fighters
# 2. 108 Magers
# 2. 51 Thieves
# 2. 11 Necromancers
# 3. 174 Total Items
# 4. 37 Items are Weapons. 137 Items are not Weapons.
# 5. Each character has [3, 3, 2, 4, 4, 1, 5, 3, 4, 4, 3, 3, 4, 4, 4, 1, 5, 5, 3, 1] Items in the first 20 rows
# 6. Each character has [2, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 2, 3, 2, 2, 2, 1, 1, 1] Weapons in the first 20 rows
# 7. 2.9735099337748343 Items
# 8. 1.3096774193548386 Weapons 


# Imports

import os
import json
import pymongo
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")


# Connect to MongoDB

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)


# Name the db RPG_db

db = client.RPG_db
print("----------------")
print("DB:", type(db), db)


# Name the collection RPG_collection

collection = db.RPG_collection
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())
print("DOCS:", collection.count_documents({}))


# 1. How many total Characters are there?

tot_char = collection.count_documents({"model": "charactercreator.character"})
print("ANSWER 1: Total Characters:", tot_char)


# 2. How many of each specific subclass?

clerics = collection.count_documents({"model": "charactercreator.cleric"})

fighters = collection.count_documents({"model": "charactercreator.fighter"})

mages = collection.count_documents({"model": "charactercreator.mage"})

thieves = collection.count_documents({"model": "charactercreator.thief"})

necromancers = collection.count_documents({"model": "charactercreator.necromancer"})

print("ANSWER 2: Total Clerics:", clerics, "Total Fighters:", fighters, "Total Mages", mages,
      "Total Thieves:", thieves, "Total Necromancers:", necromancers)


# 3. How many total items?

tot_items = collection.count_documents({"model": "item"})

print("ANSWER 3: Total Items:", tot_items)


# 4. How many of the Items are weapons? How many are not?


# 5. How many Items dow each character have? (Return first 20 rows)


# 6. How many Weapons does each character have? (Return first 20 rows)


# 7. On average, how many Items does each Character have?


# 8. On average, how many Weapons does each character have?

