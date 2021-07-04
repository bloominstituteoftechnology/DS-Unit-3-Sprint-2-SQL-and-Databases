import pymongo
import sqlite3

'''
The purpose of this script is to load a local sqlite3 file and insert
it's contents into a mongoDB 'NoSQL' database
'''

# File path to sqlite tables
SOURCE = 'C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases'
path = SOURCE + '/module1-introduction-to-sql/rpg_db.sqlite3'

# Initializing the connection and cursor
sl_conn = sqlite3.connect(path)
sl_curs = sl_conn.cursor()

# Generating a list of tuples for each character in table
characters = sl_curs.execute(
    'SELECT * FROM charactercreator_character;'
    ).fetchall()

# Connecting to database
SOURCE = 'mongodb://mjh09:XXXX@cluster0-shard-00-00-ojdma.mongodb.net:27017,'
path = SOURCE + 'cluster0-shard-00-01-ojdma.mongodb.net:27017,'
path1 = path + 'cluster0-shard-00-02-ojdma.mongodb.net:27017/test?ssl=true&replicaSet'
path2 = path1 + '27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
client = pymongo.MongoClient(path2)
db = client.test

# For loop to insert
for character in characters:
    db.test.insert_one({
        'sql_id' : character[0],
        'name' : character[1],
        'level' : character[2],
        'exp' : character[3],
        'hp' : character[4],
        'strength' : character[5],
        'intelligence' : character[6],
        'dexterity' : character[7],
        'wisdom' : character[8],
    })


# Used to check
#print(len(characters))
#print(db)
#print(db.test.find_one({'sql_id' : 4}))
sl_curs.close()
sl_conn.commit()