# pip install pymongo
# pip install dnspython

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

characters[:10]
# Assigning characters to list
# characters = [characters]

# Make a doc
for character in characters
    rpg_doc = {
        'sql_key': characters[0],
        'name': characters[1],
        'hp': characters[2],
        'level': characters[3]
    }
    db.test.insert_one(rpg_doc)

# Insert characters
# db.test.insert_many(characters)


### QUESTIONS
### HOW WAS WORKING WITH MONGODB DIFFERENT FROM WORKING POSTGRESQL
# MongoDB seems to have fewer steps but postgresql seems more simple

# PostgreSQL has a stricter schema, you can have different features
# in the data in MongoDB which could cause problems with your DB,

# I think PostgreSQL was easier and MongoDB was harder