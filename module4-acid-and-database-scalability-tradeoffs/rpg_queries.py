import os
import pymongo
import sqlite3
from dotenv import load_dotenv

# Get credentials from .env file
load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME")

client = pymongo.MongoClient(
    f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER_NAME}/test?retryWrites=true&w=majority'
    )
db = client.rpg

# Explore data
print('1: How many total Characters are there?')
total_char = db.rpg.count_documents({'table_name': 'charactercreator_character'})
print(f'Total characters: {total_char}')
print('--------')

print('2: How many of each specific subclass?')
subclass = ['mage', 'necromancer', 'thief', 'cleric', 'fighter']
for item in subclass:
    total_subclass = db.rpg.count_documents({'table_name': f'charactercreator_{item}'})
    print(f'There are {total_subclass} total {item} Characters.')
print('--------')

print('3: How many total Items?')
total_items = db.rpg.count_documents({'table_name': 'armory_item'})
print(f'Total items: {total_items}')
print('--------')

print('4: How many of the Items are weapons? How many are not?')
unique_weapons = db.rpg.count_documents({'table_name': 'armory_weapon'})
weapons = list(db.rpg.find({'table_name': 'armory_weapon'}))
weapon_ids = [weapon['item_ptr_id'] for weapon in weapons]
num_held_weapons = db.rpg.count_documents({'table_name': 'charactercreator_character_inventory',
                                                'item_id': {'$in': weapon_ids}})
print(f'Characters own a total of {num_held_weapons} weapons and {num_held_items - num_held_weapons} non-weapons.')
print(f'There are {unique_weapons} unique weapons and {num_unique_items - unique_weapons} unique non-weapons.')
print('--------')

print('5: How many Items does each character have? (Return first 20 rows)')
results = db.rpg.aggregate(
            [{'$match': {'table_name': 'charactercreator_character_inventory'}},
            {'$group':
                {
                    '_id': '$character_id',
                    'num_items': {'$sum': 1}
                }
            },
            {'$sort': {'_id': 1}},
            {'$limit': 20}]
        )
for result in results:
    print(result)
print('--------')