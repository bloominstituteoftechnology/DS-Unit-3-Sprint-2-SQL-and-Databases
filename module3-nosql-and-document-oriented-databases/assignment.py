"""
With MongoDB, you're not using SQL queries or cursors.
It may be easier in the short term, but once you really get
into SQL, working with MongoDB may prove more counterintuitive
than PostgreSQL.
"""

import pymongo
import sqlite3

mlab_url = "mongodb://USERNAME:PASSWORD@MLABUSERID.mlab.com:41268/nosql-test?retryWrites=false&w=majority"
client = pymongo.MongoClient(mlab_url)
db = client["nosql-test"]

sl_conn = sqlite3.connect('module3-nosql-and-document-oriented-databases/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()

allChars = []
for character in characters:
  oneChar = {'sql_id': character[0]}
  oneChar['name'] = character[1]
  oneChar['level'] = character[2]
  oneChar['exp'] = character[3]
  oneChar['strength'] = character[4]
  oneChar['intelligence'] = character[5]
  oneChar['dexterity'] = character[6]
  oneChar['wisdom'] = character[7]
  allChars.append(oneChar)
print(allChars)

db.test.insert_many(allChars)
print('Uploaded the RPG data to database')

sl_curs.close()