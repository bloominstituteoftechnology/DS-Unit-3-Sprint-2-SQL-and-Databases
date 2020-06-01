import os
from dotenv import load_dotenv
import pymongo


load_dotenv()

DB_USER = os.getenv('MONGO_DB_USER', default='oops')
DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', default='oops')
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME', default='oops')

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_uri)
db = client.rpg_database

# How many total Characters are there?
collection = db.charactercreator_character
result = collection.count_documents({})
print(f'There are {result} total characters')

# How many of each specific subclass?
print('\n')
collection = db.charactercreator_cleric
result = collection.count_documents({})
print(f'There are {result} clerics')

collection = db.charactercreator_fighter
result = collection.count_documents({})
print(f'There are {result} fighters ')

collection = db.charactercreator_mage
result = collection.count_documents({})
print(f'There are {result} mages')

collection = db.charactercreator_necromancer
result = collection.count_documents({})
print(f'There are {result} necromancers (a subset of mages)')

collection = db.charactercreator_thief
result = collection.count_documents({})
print(f'There are {result} thieves')

# How many total Items?
print('\n')
collection = db.armory_item
result = collection.count_documents({})
print(f'There are {result} total items')

# How many of the Items are weapons? How many are not?
print('\n')
collection = db.armory_weapon
weapon_result = collection.count_documents({})

collection = db.armory_item
item_result = collection.count_documents({})

print(f'There are {weapon_result} total weapons')
print(f'There are {item_result - weapon_result} items that are not weapons')

# How many Items does each character have? (Return first 20 rows)
print('\n')
collection = db.charactercreator_character
result = list(collection.find({}))
for i in range(20):
    character_number = result[i]['pk']
    number_of_items = len(result[i]['inventory'])
    print(f"Character {character_number} has {number_of_items} items")

# How many Weapons does each character have? (Return first 20 rows)
print('\n')
collection = db.charactercreator_character
inventory_result = list(collection.find({}))
inventory_list = [x['inventory'] for x in inventory_result]
print(inventory_list[0].drop(20))

# On average, how many Items does each Character have?
print('\n')
collection = db.charactercreator_character
result = list(collection.find({}))
inventory_count = [len(x['inventory']) for x in result]
print(f'On average, each character has {sum(inventory_count) / len(inventory_count)} items')

# On average, how many Weapons does each character have?


client.close()

