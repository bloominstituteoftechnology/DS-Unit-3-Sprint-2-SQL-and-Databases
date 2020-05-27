import pymongo
import os
from dotenv import load_dotenv
import json


load_dotenv()

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'rpg.json')
with open(DATA_FILE_PATH) as f:
    rpg_data = json.load(f)

charactercreator_thief_list = [x for x in rpg_data if x['model'] == 'charactercreator.thief']
charactercreator_necromancer_list = [x for x in rpg_data if x['model'] == 'charactercreator.necromancer']
armory_weapon_list = [x for x in rpg_data if x['model'] == 'armory.weapon']
charactercreator_cleric_list = [x for x in rpg_data if x['model'] == 'charactercreator.cleric']
charactercreator_fighter_list = [x for x in rpg_data if x['model'] == 'charactercreator.fighter']
charactercreator_character_list = [x for x in rpg_data if x['model'] == 'charactercreator.character']
armory_item_list = [x for x in rpg_data if x['model'] == 'armory.item']
charactercreator_mage_list = [x for x in rpg_data if x['model'] == 'charactercreator.mage']

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


# charactercreator_thief
collection = db.charactercreator_thief
collection.insert_many(charactercreator_thief_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_necromancer
collection = db.charactercreator_necromancer
collection.insert_many(charactercreator_necromancer_list)
print("DOCS:", collection.count_documents({}))

# armory_weapon
collection = db.armory_weapon
collection.insert_many(armory_weapon_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_cleric
collection = db.charactercreator_cleric
collection.insert_many(charactercreator_cleric_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_fighter
collection = db.charactercreator_fighter
collection.insert_many(charactercreator_fighter_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_character
collection = db.charactercreator_character
collection.insert_many(charactercreator_character_list)
print("DOCS:", collection.count_documents({}))

# armory_item
collection = db.armory_item
collection.insert_many(armory_item_list)
print("DOCS:", collection.count_documents({}))

# charactercreator_mage
collection = db.charactercreator_mage
collection.insert_many(charactercreator_mage_list)
print("DOCS:", collection.count_documents({}))

client.close()
