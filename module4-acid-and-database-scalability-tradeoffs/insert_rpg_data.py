"""
After a 1-on-1 with my TL, I decided to redo inserting
the RPG data into mongoDB, per his comments.
"""

import sqlite3
import pymongo
from password_example import password
# Note: For the above to work, you'll have to change the
# password in password_example to whatever your
# mongoDB cluster's password is.


client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-bxlcw.mongodb.net:27017,cluster0-shard-00-01-bxlcw.mongodb.net:27017,cluster0-shard-00-02-bxlcw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

tables = ['charactercreator_character',
          'charactercreator_mage', 'charactercreator_necromancer',
          'charactercreator_thief', 'charactercreator_cleric',
          'charactercreator_fighter', 'armory_item', 'armory_weapon',
          'charactercreator_character_inventory']

for table in tables:
    info_query = f'PRAGMA table_info({table});'
    table_info = curs.execute(info_query).fetchall()

    column_names = []
    for tup in table_info:
        column_names.append(tup[1])

    row_query = f'SELECT * FROM {table};'
    table_rows = curs.execute(row_query).fetchall()
    for row in table_rows:
        mongo_entry = {}
        
        # First key is the table name.
        mongo_entry['table_name'] = table
        # Next, we get the values from the dataset.
        for i in range(len(column_names)):
            key = column_names[i]
            value = row[i]
            mongo_entry[key] = value
        
        db.rpg_data.insert_one(mongo_entry)
