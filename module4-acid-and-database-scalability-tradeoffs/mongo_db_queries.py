"""
Using MongoDB queries to get info
on the RPG data.
"""

import pymongo
from password_example import mongo_password

client = pymongo.MongoClient(f"mongodb://admin:{mongo_password}@cluster0-shard-00-00-bxlcw.mongodb.net:27017,cluster0-shard-00-01-bxlcw.mongodb.net:27017,cluster0-shard-00-02-bxlcw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print('Question 1: How many total Characters are there?')
num_chars = db.rpg_data.count_documents({'table_name': 'charactercreator_character'})
print(f'Answer: There are {num_chars} total Characters.')
print(' ')

print('Question 2: How many of each specific subclass?')
print('Answer:')
classes = ['mage', 'necromancer', 'thief', 'cleric', 'fighter']
for char_class in classes:
    num_class = db.rpg_data.count_documents({'table_name': f'charactercreator_{char_class}'})
    print(f'There are {num_class} total {char_class} Characters.')
print(' ')

print('Question 3: How many total Items?')
num_unique_items = db.rpg_data.count_documents({'table_name': 'armory_item'})
num_held_items = db.rpg_data.count_documents({'table_name': 'charactercreator_character_inventory'})
print(f'Answer: Characters own a total of {num_held_items} Items; there are {num_unique_items} total unique Items.')
print(' ')

print('Question 4: How many of the Items are weapons? How many are not?')
num_unique_weapons = db.rpg_data.count_documents({'table_name': 'armory_weapon'})
weapons = list(db.rpg_data.find({'table_name': 'armory_weapon'}))
weapon_ids = [weapon['item_ptr_id'] for weapon in weapons]
num_held_weapons = db.rpg_data.count_documents({'table_name': 'charactercreator_character_inventory',
                                                'item_id': {'$in': weapon_ids}})
print('Answer:')
print(f'Characters own a total of {num_held_weapons} weapons and {num_held_items - num_held_weapons} non-weapons.')
print(f'There are {num_unique_weapons} unique weapons and {num_unique_items - num_unique_weapons} unique non-weapons.')
print(' ')

print('Question 5: How many Items does each character have? (Return first 20 rows)')
results = db.rpg_data.aggregate(
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
print('Answer:')
for result in results:
    print(result)
print(' ')

print('Question 6: How many Weapons does each character have? (Return first 20 rows)')
#results = db.rpg_data.aggregate([
#    {'$match': {'table_name': 'charactercreator_character_inventory'}},
#    {'$group': {
#        '_id': '$character_id',
#        'num_weapons': {
#            '$switch': {
#                'branches': [
#                    {
#                        'case': {'$in': ['item_id', weapon_ids]},
#                        'then': {'$sum': 1}
#                    },
#                    {
#                        'case': {'$not': {'$in': ['item_id', weapon_ids]}},
#                        'then': {'$sum': 0}
#                    }
#                ],
#                'default': 0
#            }
#        }
#    }},
#    {'$sort': {'_id': 1}},
#    {'$limit': 20}
#])
#
#print('Answer:')
#for result in results:
#    print(result)
print('Answer: I give up!!!')
