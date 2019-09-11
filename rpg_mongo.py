import sqlite3
import pymongo

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

characters = curs.execute('SELECT * FROM charactercreator_character;').fetchall()

dict = {'characters': characters}

# Use 3.4 connection string for clarity
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-wk9ed.mongodb.net:27017,cluster0-shard-00-01-wk9ed.mongodb.net:27017,cluster0-shard-00-02-wk9ed.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db.test.insert_one(dict)

print(list(db.test.find()))
