# Imports
import pymongo
import sqlite3

# Connect to Mongo
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-4dniv.mongodb.net:27017,cluster0-shard-00-01-4dniv.mongodb.net:27017,cluster0-shard-00-02-4dniv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Create connection and cursor
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Extract data
get_characters = 'SELECT * FROM charactercreator_character'
characters = curs.execute(get_characters).fetchall()

# Transform data & add to Mongo
for character in characters:
    rpg_doc = {
        'sql_key': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    }
    db.test.insert_one(rpg_doc)

# Create cursor to find new docs
curs = db.test.find({})
print(list(curs)[:5])
