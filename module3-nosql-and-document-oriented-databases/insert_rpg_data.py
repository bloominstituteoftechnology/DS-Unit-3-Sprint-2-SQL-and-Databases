"""
Inserting RPG data into mongoDB.
QUESTION: "How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"
ANSWER: It's easier to input data with MongoDB, at least using Python. Since MongoDB takes dictionaries,
Python's inbuilt capabilities make it relatively straightforward to convert sqlite data.
However, PostgreSQL requires SQL queries, which are kind of a pain to do in Python.
On the other hand, retrieving/sorting/manipulating the data is easier in Postgre IMO.
I find the relevant SQL commands more intuitive/powerful than the respective Mongo commands.
"""

import sqlite3
import pymongo
from password_example import password
# Note: For the above to work, you'll have to change the
# password in password_example to whatever your
# mongoDB cluster's password is.

client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-bxlcw.mongodb.net:27017,cluster0-shard-00-01-bxlcw.mongodb.net:27017,cluster0-shard-00-02-bxlcw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg_data

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# My plan is to run a for-loop eventually, but I'll practice on a single table.

query = 'SELECT * FROM charactercreator_character;'
rows = curs.execute(query).fetchall()

for row in rows:
    mongo_entry = {
        'character_id': row[0],
        'name': row[1],
        'level': row[2],
        'exp': row[3],
        'hp': row[4],
        'strength': row[5],
        'intelligence': row[6],
        'dexterity': row[7],
        'wisdom': row[8]
    }
    db.charactercreator_character.insert_one(mongo_entry)

# Confirm that this worked.
print(db.charactercreator_character.find_one())

# Now we can run a for-loop. First, we need a list of all our tables.
tables = ['charactercreator_mage', 'charactercreator_necromancer',
          'charactercreator_thief', 'charactercreator_cleric',
          'charactercreator_fighter', 'armory_item', 'armory_weapon',
          'charactercreator_character_inventory']

# Next is the loop. We'll be iterating on each table individually.
for table in tables:
    # First we need to know the column names.
    # We can do this through a "PRAGMA table_info" query.
    info_query = f'PRAGMA table_info({table});'
    table_info = curs.execute(info_query).fetchall()

    # The above gives us a list of tuples. The *second* entry
    # in each tuple is the column name we want.
    column_names = []
    for tup in table_info:
        column_names.append(tup[1])

    # Now we can do the main loop. First, get all the rows.
    row_query = f'SELECT * FROM {table};'
    table_rows = curs.execute(row_query).fetchall()
    for row in rows:
        mongo_entry = {}
        # The *keys* for the above dictionary are the column names,
        # and the *values* are the row entries.
        for i in range(len(column_names)):
            # We need to set up the loop this way so that each key
            # gets mapped to the proper value.
            key = column_names[i]
            value = row[i]
            mongo_entry[key] = value
        
        # And now we can finally insert the row!
        db[table].insert_one(mongo_entry)
        # Note that you have to use the bracket syntax here (db[table])
        # rather than dot syntax (db.table), since the latter would
        # create a single collection named "table." The bracket syntax
        # creates a different collection for each table, with the same
        # name as the table's name.
