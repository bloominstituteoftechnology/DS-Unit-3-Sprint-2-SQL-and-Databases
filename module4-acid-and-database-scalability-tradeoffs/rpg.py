import pymongo
import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()

conn = sqlite3.connect(os.path.join(os.path.dirname(
    __file__), 'rpg_db.sqlite3'))
curs = conn.cursor()

mongo_username = os.getenv('mongo_username')
mongo_password = os.getenv('mongo_password')
mongo_host = os.getenv('mongo_host')

print(
    f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_host}/test?retryWrites=true&w=majority")
client = pymongo.MongoClient(
    f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_host}/test?retryWrites=true&w=majority")
db = client.test

query_1 = 'SELECT * FROM charactercreator_character;'
query_2 = 'SELECT * FROM charactercreator_inventory;'
query_3 = 'SELECT * FROM charactercreator_cleric;'
query_4 = 'SELECT * FROM charactercreator_fighter;'
query_5 = 'SELECT * FROM charactercreator_mage;'
query_6 = 'SELECT * FROM charactercreator_necromancer;'
query_7 = 'SELECT * FROM charactercreator_thief;'
query_8 = 'SELECT * FROM armory_item ai LEFT JOIN armory_weapon aw on ai.item_id = aw.item_ptr_id;'

data_1 = curs.execute(query_1).fetchall()
data_1 = curs.execute(query_1).fetchall()

# migrate sqlite3 data to mongoDB
list_character = []
for row in data_1:
    obj = {
        'id': row[0],
        'name': row[1],
        'level': row[2],
        'exp': row[3],
        'hp': row[4],
        'strength': row[5],
        'inteligence': row[6],
        'dexterity': row[7],
        'wisdom': row[8],
    }
    list_character.append(obj)
# print(list_data)
db['Character'].drop()
db.create_collection('Character')
db.Character.insert_many(list_character)

breakpoint()

# - How many total Characters are there? 302 chracters
db['Character'].count_documents({})

# - How many of each specific subclass?

# - How many total Items? 174 items

# - How many of the Items are weapons? How many are not? 37 items are weapon items and 137 items are not weapons

# - How many Items does each character have? (Return first 20 rows)

# - How many Weapons does each character have? (Return first 20 rows)

# - On average, how many Items does each Character have?

# - On average, how many Weapons does each character have?
