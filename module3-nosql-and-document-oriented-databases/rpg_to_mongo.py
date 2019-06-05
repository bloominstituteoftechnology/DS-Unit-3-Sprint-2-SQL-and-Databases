import sqlite3
import pymongo

# connect to MongoDB 
client = pymongo.MongoClient("""mongodb://admin:{}@cluster0-shard-
00-00-yhyf0.mongodb.net:27017,cluster0-shard-00-01-yhyf0.mongodb.net:
27017,cluster0-shard-00-02-yhyf0.mongodb.net:27017/test?ssl=
true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=
majority""".format(input('enter password: ')))
db = client.test

# open connection to sqlite3 db
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# retrieve all characters to make a list of tuples
characters = curs.execute('SELECT * FROM charactercreator_character;').fetchall()

# go through list of characters and put in JSON format while
# inserting each character into Mongo test DB
for _ in characters:
    db.test.insert_one({
    'sql_id': _[0],
    'name': _[1],
    'level': _[2],
    'exp': _[3],
    'hp': _[4],
    'strength': _[5],
    'intelligence': _[6],
    'dexterity': _[7],
    'wisdom': _[8]
})