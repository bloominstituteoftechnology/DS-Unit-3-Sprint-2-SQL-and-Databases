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
query_2 = """
    SELECT * FROM charactercreator_character cc
    INNER JOIN charactercreator_cleric cleric
    on cc.character_id = cleric.character_ptr_id;
    """
query_3 = """
    SELECT * FROM charactercreator_character cc
    INNER JOIN charactercreator_fighter fighter
    on cc.character_id = fighter.character_ptr_id;
    """
query_4 = """
    SELECT * FROM charactercreator_character cc
    INNER JOIN charactercreator_mage mage
    on cc.character_id = mage.character_ptr_id;
    """
query_5 = """
    SELECT * FROM charactercreator_character cc
    INNER JOIN charactercreator_necromancer necromancer
    on cc.character_id = necromancer.character_ptr_id;
    """
query_6 = """
    SELECT * FROM charactercreator_character cc
    INNER JOIN charactercreator_thief thief
    on cc.character_id = thief.character_ptr_id;
    """

# query_3 = 'SELECT * FROM charactercreator_character_inventory;'
# query_4 = 'SELECT * FROM charactercreator_cleric;'
# query_5 = 'SELECT * FROM charactercreator_fighter;'
# query_6 = 'SELECT * FROM charactercreator_mage;'
# query_7 = 'SELECT * FROM charactercreator_necromancer;'
# query_8 = 'SELECT * FROM charactercreator_thief;'
# query_9 = 'SELECT * FROM armory_item ai LEFT JOIN armory_weapon aw on ai.item_id = aw.item_ptr_id;'

data_1 = curs.execute(query_1).fetchall()
data_2 = curs.execute(query_2).fetchall()
data_3 = curs.execute(query_3).fetchall()
data_4 = curs.execute(query_4).fetchall()
data_6 = curs.execute(query_6).fetchall()
# data_7 = curs.execute(query_7).fetchall()

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

list_cleric = []
for row in data_2:
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
        'character_ptr_id': row[9],
        'using_shield': row[10],
        'mana': row[11]
    }
    list_cleric.append(obj)
# print(list_data)
db['cleric'].drop()
db.create_collection('cleric')
db['cleric'].insert_many(list_cleric)


# - How many total Characters are there? 302 chracters
result_1 = db['Character'].count_documents({})
print('result_1: ', result_1)

# - How many of each specific subclass?
result_2 = db['cleric'].count_documents({})
print('result_2: ', result_2)

# - How many total Items? 174 items

# - How many of the Items are weapons? How many are not? 37 items are weapon items and 137 items are not weapons

# - How many Items does each character have? (Return first 20 rows)

# - How many Weapons does each character have? (Return first 20 rows)

# - On average, how many Items does each Character have?

# - On average, how many Weapons does each character have?


"""
    Opinion on this assignment
    To be honest, I don't see a point of this assignment,
    especially, Lambada must specify if SQL -> NOSQL: data migration
    is the key for this assignment. I don' think it is worth doing this data manipulation
    I can continue doing so, but I really wish lambda explain us what are the expectations from the student
    so let me stop doing the assignment for this moudle 4
"""
