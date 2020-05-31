# "How was working with MongoDB different from working with
# PostgreSQL? What was easier, and what was harder?"

# Answer: MongoDB is a lot simpler in terms of Inserting data.
# I would not say one is easier than the other because they all
# have different purpose, pros and cons


import pymongo
import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()

conn = sqlite3.connect(os.path.join(os.path.dirname(
    __file__), 'rpg_db.sqlite3'))
curs = conn.cursor()

username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('host')
print(
    f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority")
client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority")
db = client.test
# print('db', db)

sql_query = 'SELECT * FROM charactercreator_character;'

data_from_sql = curs.execute(sql_query).fetchall()
# print(data_from_sql[0])

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
# breakpoint()
db.Character.insert_many(list_data)
