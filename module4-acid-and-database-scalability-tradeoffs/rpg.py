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

sql_query = 'SELECT * FROM charactercreator_character;'

data_from_sql = curs.execute(sql_query).fetchall()

list_data = []
for row in data_from_sql:
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
    list_data.append(obj)
# print(list_data)
db['Character'].drop()
db.create_collection('Character')
db.Character.insert_many(list_data)

# - How many total Characters are there? 302 chracters
# - How many of each specific subclass? not sure what the question exactly means. i'd say 5 because there are cleric, fighter, mage, necromancer and thief.
# - How many total Items? 174 items
# - How many of the Items are weapons? How many are not? 37 items are weapon items and 137 items are not weapons
# - How many Items does each character have? (Return first 20 rows)
# - How many Weapons does each character have? (Return first 20 rows)
# - On average, how many Items does each Character have?
# - On average, how many Weapons does each character have?
