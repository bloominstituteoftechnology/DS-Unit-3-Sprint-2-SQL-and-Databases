import pymongo
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

client = pymongo.MongoClient("mongodb://admin:admin@cluster0-shard-00-00-hhcas.mongodb.net:27017,cluster0-shard-00-01-hhcas.mongodb.net:27017,cluster0-shard-00-02-hhcas.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['rpg']
col = db['characters']

# make a list of dictionaries describing each character
char_list = []
for row in curs.execute('SELECT * FROM charactercreator_character;'):
    character = {
        'char_id'  : row[0],
        'name' : row[1],
        'level' : row[2],
        'exp' : row[3],
        'hp' : row[4],
        'strength' : row[5],
        'intelligence' : row[6],
        'dexterity' : row[7],
        'wisdom' : row[8]
    }
    char_list.append(character)

col.insert_many(char_list)

# working with mongo made it somewhat easier to insert items and
# create new tables. On the other hand, postgres made it much easier, at least
# in my opinion, to view and work with the data, and ultimately just feels
# more reliable.