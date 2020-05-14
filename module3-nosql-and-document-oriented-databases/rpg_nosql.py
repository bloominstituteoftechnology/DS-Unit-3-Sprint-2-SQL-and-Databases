import pymongo
import os
from dotenv import load_dotenv
import ssl
import sqlite3

load_dotenv()

# Set path to rpg data
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), 
                    '..', 'module1-introduction-to-sql', 
                    'rpg_db.sqlite3')

DB_USER = os.getenv("MONGO_USER", default="You shouldn't be here...")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="You shouldn't be here...")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="You shouldn't be here...")

# Create connection to rpg_data
sqlite_connection = sqlite3.connect(DATABASE_FILEPATH)
sqlite_connection.row_factory = sqlite3.Row
sqlite_cursor = sqlite_connection.cursor()

# Test connection and cursor
print("Connection:", sqlite_connection)
print("Cursor:", sqlite_cursor)

# Set uri using hidden credentials
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# Check that uri variable is correct
print("------------------")
print("URI:", connection_uri)

# Connect to Mongo Client
client = pymongo.MongoClient(connection_uri, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
print("------------------")
print("CLIENT:", type(client), client)

# Create new database
db = client.rpg_database # Not created until we input some data
print("-----------------")
print('DB:', type(db), db)

# Get tables from sqlite using SQL commands

get_items = get_items = """
                 SELECT
                    *
                 FROM
                    armory_item
                 """

get_weapons = """
                 SELECT
                    *
                 FROM
                    armory_weapon
                 """

get_characters = """
                 SELECT
                    *
                 FROM
                    charactercreator_character
                 """

get_inventories = """
                 SELECT
                    *
                 FROM
                    charactercreator_character_inventory
                 """

get_clerics = """
                 SELECT
                    *
                 FROM
                    charactercreator_cleric
                 """

get_fighters = """
                 SELECT
                    *
                 FROM
                    charactercreator_fighter
                 """

get_mages = """
                 SELECT
                    *
                 FROM
                    charactercreator_mage
                 """

get_necromancers = """
                 SELECT
                    *
                 FROM
                    charactercreator_necromancer
                 """

get_thieves = """
                 SELECT
                    *
                 FROM
                    charactercreator_thief
                 """

# Execute SQL SELECT commands
items = sqlite_cursor.execute(get_items).fetchall()
weapons = sqlite_cursor.execute(get_weapons).fetchall()
characters = sqlite_cursor.execute(get_characters).fetchall()
inventories = sqlite_cursor.execute(get_inventories).fetchall()
clerics = sqlite_cursor.execute(get_clerics).fetchall()
fighters = sqlite_cursor.execute(get_fighters).fetchall()
mages = sqlite_cursor.execute(get_mages).fetchall()
necromancers = sqlite_cursor.execute(get_necromancers).fetchall()
thieves = sqlite_cursor.execute(get_thieves).fetchall()

# Create new collection for each table from rpg_data
item_collection = db.items
print("-----------------")
print("COLLECTION:", type(item_collection), item_collection)

weapon_collection = db.weapons
print("-----------------")
print("COLLECTION:", type(weapon_collection), weapon_collection)

character_collection = db.characters
print("-----------------")
print("COLLECTION:", type(character_collection), character_collection)

inventory_collection = db.inventories
print("-----------------")
print("COLLECTION:", type(inventory_collection), inventory_collection)

cleric_collection = db.clerics
print("-----------------")
print("COLLECTION:", type(cleric_collection), cleric_collection)

fighter_collection = db.fighters
print("-----------------")
print("COLLECTION:", type(fighter_collection), fighter_collection)

mage_collection = db.mages
print("-----------------")
print("COLLECTION:", type(mage_collection), mage_collection)

necromancer_collection = db.necromancers
print("-----------------")
print("COLLECTION:", type(necromancer_collection), necromancer_collection)

thief_collection = db.thieves
print("-----------------")
print("COLLECTION:", type(thief_collection), thief_collection)

# Insert new document into item_collection
for item in items:
    item_collection.insert_one({
        "item_id" : item[0],
        "name" : item[1],
        "value" : item[2],
        "weight" : item[3]
    })

print(item_collection.count_documents({})) # Should see 174

for weapon in weapons:
    weapon_collection.insert_one({
        "item_ptr_id" : weapon[0],
        "power" : weapon[1]
    })

print(weapon_collection.count_documents({})) # Should see 37

for character in characters:
    character_collection.insert_one({
        "character_id" : character[0],
        "name" : character[1],
        "level" : character[2],
        "exp" : character[3],
        "hp" : character[4],
        "strength" : character[5],
        "intelligence" : character[6],
        "dexterity" : character[7],
        "wisdom" : character[8]
    })

print(character_collection.count_documents({})) # Should see 302

for inventory in inventories:
    inventory_collection.insert_one({
        "id" : inventory[0],
        "character_id" : inventory[1],
        "item_id" : inventory[2],
    })

print(inventory_collection.count_documents({})) # Should see 898

for cleric in clerics:
    cleric_collection.insert_one({
        "character_ptr_id" : cleric[0],
        "using_shield" : cleric[1],
        "mana" : cleric[2],
    })

print(cleric_collection.count_documents({})) # Should see 75

for fighter in fighters:
    fighter_collection.insert_one({
        "character_ptr_id" : fighter[0],
        "using_shield" : fighter[1],
        "rage" : fighter[2],
    })

print(fighter_collection.count_documents({})) # Should see 68

for mage in mages:
    mage_collection.insert_one({
        "character_ptr_id" : mage[0],
        "has_pet" : mage[1],
        "mana" : mage[2],
    })

print(mage_collection.count_documents({})) # Should see 108

for necromancer in necromancers:
    necromancer_collection.insert_one({
        "mage_ptr_id" : necromancer[0],
        "mana" : necromancer[1]
    })

print(necromancer_collection.count_documents({})) # Should see 11

for thief in thieves:
    thief_collection.insert_one({
        "character_ptr_id" : thief[0],
        "is_sneaking" : thief[1],
        "energy" : thief[2]
    })

print(thief_collection.count_documents({})) # Should see 51

