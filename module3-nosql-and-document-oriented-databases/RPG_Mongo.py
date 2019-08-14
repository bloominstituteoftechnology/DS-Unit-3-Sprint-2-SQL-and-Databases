
import pymongo
import sqlite3
# MongoDB Password: UkHGft1qF7I3eLWz


client = pymongo.MongoClient(
    "mongodb+srv://admin:UkHGft1qF7I3eLWz@cluster0-4qxo0.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# print(db)
# print(client.nodes)
#print(db.test.count_documents({'x': 1}))

conn = sqlite3.connect("rpg_db.sqlite3")
curs = conn.cursor()

characters = curs.execute(
    '''SELECT * FROM charactercreator_character;''').fetchall()

print(characters)

'''for character in characters:
    db.test.insert_one({
        'sql_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': characters[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    })'''

print(list(db.test.find()))