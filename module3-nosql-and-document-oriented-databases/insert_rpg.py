# Q: How was working with MongoDB different from working with PostgreSQL?
#    What was easier, and what was harder?
# A: While inserting data into MongoDB took a bit more thought than inserting
#    data into Postgre SQL, I found MongoDB easier to interface with, and I
#    enjoyed working with it more.

import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb://admin:<INSERT PASSWORD HERE>@cluster0-shard-00-00-cicid.mongodb.net:27017,cluster0-shard-00-01-cicid.mongodb.net:27017,cluster0-shard-00-02-cicid.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
rpg = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

dict_of_characters = {}
for character in rpg:
    dict_of_characters[str(character[0])] = {'name': character[1],
                                             'level': character[2],
                                             'exp': character[3],
                                             'hp': character[4],
                                             'strength': character[5],
                                             'intelligence': character[6],
                                             'dexterity': character[7],
                                             'wisdom': character[8]}

db.test.insert_one(dict_of_characters)

print(list(db.test.find()))
