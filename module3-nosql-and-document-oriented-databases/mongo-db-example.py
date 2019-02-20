#!/usr/bin/env python
"""Example using MongoDB"""

import pymongo
import json
import urllib.request
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

# connection parameters
USER = 'TODO'
PASSWORD = 'TODO'

# connect to mongo db client
connection_string = ('mongodb://' + USER + ':' + PASSWORD + ''
                     '@cluster0-shard-00-00-f1lyf.mongodb.net:27017,'
                     'cluster0-shard-00-01-f1lyf.mongodb.net:27017,'
                     'cluster0-shard-00-02-f1lyf.mongodb.net:27017/test?'
                     'ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&'
                     'retryWrites=true')
client = pymongo.MongoClient(connection_string)

# test inserting a document
db = client.test
test_doc = {'favorite animal' : 'dolphin'}
if not db.test.find_one(test_doc):
    db.test.insert_one(test_doc)


# insert rpg data into new collection and document
# read rpg data
url = 'https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json'
response = urllib.request.urlopen(url)
rpg_data = json.loads(response.read().decode())

# insert data
db_rpg = client.rpg
db_rpg.rpg.delete_many({}) # remove data, if it exists
db_rpg.rpg.insert_many(rpg_data)

# answering questions about rpg data
# 1. How many total Characters are there?
print ('Character Counts')
characters = db_rpg.rpg.find({'model': 'charactercreator.character'})
characters_count = characters.count()
print ('Total Characters', characters_count)
# 2. How many of each specific subclass?
for subclass in ['fighter', 'mage', 'necromancer', 'cleric', 'thief']:
    sub_characters = db_rpg.rpg.find({'model': 'charactercreator.'+subclass})
    print ('Total', subclass, ':', sub_characters.count())

# 3. How many total Items?
items_count = db_rpg.rpg.find({'model': 'armory.item'}).count()
print ('Total Items:', items_count)

# 4. How many of the Items are weapons? How many are not?
weapons_count = db_rpg.rpg.find({'model': 'armory.weapon'}).count()
print ('Total Weapons', weapons_count)
print ('Total Non-Weapons', items_count - weapons_count)

# 5. How many Items does each character have? (Return first 20 rows)
# each model.charactercreator.character has an inventory w item list
print ('\nCharacter Item Counts')
for character in characters[:20]:
    print (character['fields']['name'], len(character['fields']['inventory']))

# 6. How many Weapons does each character have? (Return first 20 rows)
# same idea, but we need to check if something is a weapon by id
print ('\nCharacter Weapon Counts')
characters = db_rpg.rpg.find({'model': 'charactercreator.character'})
weapons =  db_rpg.rpg.find({'model': 'armory.weapon'})
weapons_keys = [weapon['pk'] for weapon in weapons]
for character in characters[:20]:
    name = character['fields']['name']
    char_items = character['fields']['inventory']
    char_weapons = len([item for item in char_items if item in weapons_keys])
    print (name, char_weapons)

# 7. On average, how many Items does each Character have?
print ('\nAverage Item and Weapon Counts')
characters = db_rpg.rpg.find({'model': 'charactercreator.character'})
total_items = 0
total_weapons = 0
for character in characters:
    char_items = character['fields']['inventory']
    total_items += len(char_items)
    total_weapons += len([item for item in char_items if item in weapons_keys])
average_items = total_items / characters_count
print ('Average Items', average_items)

# 8. On average, how many Weapons does each character have?
average_weapons = total_weapons / characters_count
print ('Average Weapons', average_weapons)