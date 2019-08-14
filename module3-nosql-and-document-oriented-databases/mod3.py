# QUESTIONS
'''
How was working with MongoDB different from
working with PostgreSQL? What was easier,
and what was harder?

I feel as if it will be a lot easier to grab certain things from MongoDB.
For example writing db.test.find({'level': 2}) is a lot easier than
SELECT * FROM characters WHERE level = 3
Maybe that's just me. ¯\_(ツ)_/¯
'''



import pymongo
import sqlite3

# MONGO DB STUFF
client = pymongo.MongoClient("mongodb+srv://admin:L2oz0xJtZmJwfTsg@cluster0-2wndt.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# SQLITE3 STUFF
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# EXECUTE QUERY AND SAVE FETCHALL TO CHARACTERS
curs.execute('SELECT * FROM charactercreator_character')
characters = curs.fetchall()

# THIS CODE IS FOR THE ABILITY TO RE-RUN WITHOUT ISSUES
if list(db.test.find()) != []:
    db.test.delete_many({})

# FOR EACH CHARACTER IN THE DATABASE, CREATE A DOCUMENT IN MONGO
for character in characters:
    db.test.insert_one({
        'id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    })

# PRINT EACH DOC ONE AT A TIME
for doc in list(db.test.find()):
    print(doc)

# CHECK TO MAKE SURE THAT THE NUMBER OF DOCUMENTS IS EQUAL TO 302
assert(len(list(db.test.find())) == 302)

 