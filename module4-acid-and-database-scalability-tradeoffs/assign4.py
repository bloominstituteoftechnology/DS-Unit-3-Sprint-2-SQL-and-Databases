import pymongo
import psycopg2

#user : admin
#pass : 12TPzLpCVUkL3Lvh

client = pymongo.MongoClient("""mongodb+srv://admin:12TPzLpCVUkL3Lvh@ds9-unit3-module3-k1toc.mongodb.net/test?retryWrites=true&w=majority""")
db = client.rpg_data

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

# Q1: How many total Characters are there?
print('Total Characters:\t'+str(len(db.rpg_data.find())))

# Q2: How many of each specific subclass?