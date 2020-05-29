'''
I think that relational databases are easier to work with. The biggest reason is because
it makes it a lot easier to follow visually. MongoDB was easier to use because the rules
seem to be a lot less strict on creating and inserting data. But I can also see that being a problem
too, so it's a little bit of a double egded sword.
'''

import os
import sqlite3
import pymongo
from dotenv import load_dotenv

DB_FILEPATE = os.path.join(os.path.dirname(__file__), '..', 'module1-introduction-to-sql', 'rpg_db.sqlite3')

connection = sqlite3.connect(DB_FILEPATE)

connection.row_factory = sqlite3.Row
cursor = connection.cursor()

#make dictionaries for each row in charactercreator_character
query = 'SELECT * FROM charactercreator_character'
cursor.execute(query)
result = cursor.fetchall()

character_rows = [dict(row) for row in result]

# make dict for each row in armory item
query = 'SELECT * FROM armory_item'
cursor.execute(query)
result = cursor.fetchall()
item_rows = [dict(row) for row in result]




load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

db = client.Module3_db 

# insert characters into db
collection1 = db.characters 
collection1.insert_many(character_rows)

# insert items into db
collection2 = db.items
collection2.insert_many(item_rows)



