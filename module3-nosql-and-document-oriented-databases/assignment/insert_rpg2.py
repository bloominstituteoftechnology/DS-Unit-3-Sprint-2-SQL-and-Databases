'''
I think the biggest difference between SQL and no SQL was that the SQL required a schema for the data and was more restrict
NoSQL was slightly easier since it would take any type of data
'''

import pymongo
import os
from dotenv import load_dotenv
import json


load_dotenv()

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'rpg.json')
with open(DATA_FILE_PATH) as f:
    rpg_data = json.load(f)

charactercreator_thief_list = [x for x in rpg_data if x['model'] == 'charactercreator.thief']
new_charactercreator_thief_list = [x['fields'] for x in charactercreator_thief_list]
for i in range(len(new_charactercreator_thief_list)):
    new_charactercreator_thief_list[i].update({'pk':charactercreator_thief_list[i]['pk']})

charactercreator_necromancer_list = [x for x in rpg_data if x['model'] == 'charactercreator.necromancer']
new_charactercreator_necromancer_list = [x['fields'] for x in charactercreator_necromancer_list]
for i in range(len(new_charactercreator_necromancer_list)):
    new_charactercreator_necromancer_list[i].update({'pk':charactercreator_necromancer_list[i]['pk']})

armory_weapon_list = [x for x in rpg_data if x['model'] == 'armory.weapon']
new_armory_weapon_list = [x['fields'] for x in armory_weapon_list]
for i in range(len(new_armory_weapon_list)):
    new_armory_weapon_list[i].update({'pk':armory_weapon_list[i]['pk']})

charactercreator_cleric_list = [x for x in rpg_data if x['model'] == 'charactercreator.cleric']
new_charactercreator_cleric_list = [x['fields'] for x in charactercreator_cleric_list]
for i in range(len(new_charactercreator_cleric_list)):
    new_charactercreator_cleric_list[i].update({'pk':charactercreator_cleric_list[i]['pk']})

charactercreator_fighter_list = [x for x in rpg_data if x['model'] == 'charactercreator.fighter']
new_charactercreator_fighter_list = [x['fields'] for x in charactercreator_fighter_list]
for i in range(len(new_charactercreator_fighter_list)):
    new_charactercreator_fighter_list[i].update({'pk':charactercreator_fighter_list[i]['pk']})

charactercreator_character_list = [x for x in rpg_data if x['model'] == 'charactercreator.character']
new_charactercreator_character_list = [x['fields'] for x in charactercreator_character_list]
for i in range(len(new_charactercreator_character_list)):
    new_charactercreator_character_list[i].update({'pk':charactercreator_character_list[i]['pk']})

armory_item_list = [x for x in rpg_data if x['model'] == 'armory.item']
new_armory_item_list = [x['fields'] for x in armory_item_list]
for i in range(len(new_armory_item_list)):
    new_armory_item_list[i].update({'pk':armory_item_list[i]['pk']})

charactercreator_mage_list = [x for x in rpg_data if x['model'] == 'charactercreator.mage']
new_charactercreator_mage_list = [x['fields'] for x in charactercreator_mage_list]
for i in range(len(new_charactercreator_mage_list)):
    new_charactercreator_mage_list[i].update({'pk':charactercreator_mage_list[i]['pk']})

print(new_charactercreator_mage_list[0])

DB_USER = os.getenv('MONGO_DB_USER', default='oops')
DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', default='oops')
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME', default='oops')

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print('----------')
print('URI:', connection_uri)

client = pymongo.MongoClient(connection_uri)
print('----------')
print('CLIENT:', type(client), client)

db = client.rpg_database
print('----------')
print('DB:', type(db), db)

print(charactercreator_thief_list[0])
print(new_charactercreator_thief_list[0])

# charactercreator_thief
collection = db.charactercreator_thief
collection.insert_many(new_charactercreator_thief_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_necromancer
collection = db.charactercreator_necromancer
collection.insert_many(new_charactercreator_necromancer_list)
print("DOCS:", collection.count_documents({}))

# armory_weapon
collection = db.armory_weapon
collection.insert_many(new_armory_weapon_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_cleric
collection = db.charactercreator_cleric
collection.insert_many(new_charactercreator_cleric_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_fighter
collection = db.charactercreator_fighter
collection.insert_many(new_charactercreator_fighter_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_character
collection = db.charactercreator_character
collection.insert_many(new_charactercreator_character_list)
print("DOCS:", collection.count_documents({}))

# armory_item
collection = db.armory_item
collection.insert_many(new_armory_item_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_mage
collection = db.charactercreator_mage
collection.insert_many(new_charactercreator_mage_list)
print("DOCS:", collection.count_documents({}))

client.close()
