import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb+srv://btross:NWF77Q5rRin70QIT@cluster0-yevzi.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

LOCAL_DB_PATH = 'rpg_db.sqlite3'

def db_query(query):
  db = sqlite3.connect(LOCAL_DB_PATH)
  db.row_factory = sqlite3.Row
  cur = db.cursor()

  cur.execute(query)

  data = cur.fetchall()
  return data

  cur.close()
  db.close()

chars = db_query('''SELECT * FROM charactercreator_character''')

cols = ['sql_id', 'name', 'level', 'exp', 'hp', 'strength',
        'intelligence', 'dexterity', 'wisdom']

charDocs = []
for char in chars:
    chardict = {}
    for i, col in enumerate(cols):
        chardict[col] = char[i]
    charDocs.append(chardict)

db.test.insert_many(charDocs)