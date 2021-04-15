import os
import sqlite3
import pandas as pd
import pymongo
from dotenv import load_dotenv


# Set up .env variables to connect to postgres later
envpath = os.path.join(os.getcwd(),'..', '.env')
# print(envpath)
load_dotenv(envpath)

# grab .env data for mongo database for later
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME')
DB_USER = os.getenv('MONGO_USER')
DB_PASSWORD = os.getenv('MONGO_PASSWORD')

# connect to the Mongo database
print('CONNECTING TO MONGODB...')
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}-siyeu.mongodb.net/test?retryWrites=true&w=majority"
print('------------------------')
print('URI:',connection_uri)

client = pymongo.MongoClient(connection_uri)
print('------------------------')
print('CLIENT:', type(client), client)

db = client.rpg_db
print('------------------------')
print('DB:', type(db), db,)
print('------------------------\n\n')

print('1. How many characters are there?')

print(db.charactercreator_character.count_documents({}),'characters\n')

# --------------------------------------------
print('2. How many of each specific subclass?')

print(f'Fighters: {db.charactercreator_fighter.count_documents({})}')
print(f'Clerics: {db.charactercreator_cleric.count_documents({})}')
print(f'Thieves: {db.charactercreator_thief.count_documents({})}')
print(f'Mages: {db.charactercreator_mage.count_documents({}) - db.charactercreator_necromancer.count_documents({})}')
print(f'Necromancers: {db.charactercreator_necromancer.count_documents({})}\n')

# --------------------------------------------
print('3. How many total items?')

print(db.armory_item.count_documents({}),'total items\n')

# --------------------------------------------
print('4. How many of the items are weapons? How many are not?')

print(f'Non-weapons: {db.armory_item.count_documents({}) - db.armory_weapon.count_documents({})}')
print(f'Weapons: {db.armory_weapon.count_documents({})}')

# --------------------------------------------
print('5. How many items does each character have (first 20 rows)')

# I can't get it to not be sorted, but the ids do match up

curs = db.charactercreator_character_inventory.aggregate([{ 
    "$group": {
        "_id":'$character_id',
        "count": {"$sum":1}
    }   
}])

for i, record in enumerate(curs):
    print(record)

# --------------------------------------------
# print('6. How many weapons does each character have (first 20 rows)')

# MongoDB doesn't support joins, you need to do some wacky referencing
# thing to work around it

# I think I'm going to stop here and work on the postgres stuff
