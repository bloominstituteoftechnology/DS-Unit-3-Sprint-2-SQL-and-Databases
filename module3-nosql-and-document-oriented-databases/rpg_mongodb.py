pip install pymongo
pip install dnspython

import pymongo
import sqlite3


# My Connection Info
password = 'ADwab28tm'
dbname ='test'
connection = ('mongodb+srv://PKrom:' + password +
              '@cluster0.7m4yd.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient(connection)
db = client.test

# Extract
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Copy characters from character table
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

# Assigning characters to list
characters = [characters]

# Insert characters
db.test.insert_many(characters)