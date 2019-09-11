# Pythonic Python Pythonifies the Pythas.
import sqlite3
import pymongo
import os
import pandas as pd


def scourMongo(db):
    # Finds and lists all entries
    all_e = list(db.test.find())
    print(f'\n\tAmount of Entries: {len(all_e)}\n')
    for a in all_e:
        print(f'\n{a}')


conn = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

pswd = os.environ.get('password')
user = os.environ.get('username')
ipdr = os.environ.get('ip')

# My linter is screaming at me.
client = pymongo.MongoClient(
f'mongodb://{user}:{pswd}@cluster0-shard-00-00-0adlv.mongodb.net:27017,' +
'cluster0-shard-00-01-0adlv.mongodb.net:27017,cluster0-shard-00-02-0adlv.' +
'mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=' +
'admin&retryWrites=true&w=majority')
# That's right, still calling it test
db = client.test

# Lesse checque
scourMongo(db)
# Remove everything if need be
db.collection.delete_many({})

table_names = ['armory_item', 'armory_weapon',
               'charactercreator_character',
               'charactercreator_character_inventory',
               'charactercreator_cleric',
               'charactercreator_fighter',
               'charactercreator_mage',
               'charactercreator_necromancer',
               'charactercreator_thief',
               ]

tables = []
t_len = len(table_names)
# Makes two keys, one is the cursor object ID and the other is the table name
# Unsure if want a dict for each table -> name: list of values
# (so all in one collection or whatever)
# or if it should be like different collections for each type of table
# inside that collection is name: value times however many values there are
# to have, so a whole lot.
for n in range(t_len):
    tables.append({table_names[n]: curs.execute(f'''
    SELECT * FROM {table_names[n]}
    ''').fetchall()})

# Lesse
print(f'''
\tMy list length: {len(table_names)}
\t\t\t{len(tables)}
\n{tables}\n
''')

# Now let's throw these tables up there into the yonder cloud
db.test.insert_many(tables)

# See the whole kit and caboodle
scourMongo(db)
# See specific entry
