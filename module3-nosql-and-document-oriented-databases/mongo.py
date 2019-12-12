import pymongo
import psycopg2

#user : admin
#pass : 12TPzLpCVUkL3Lvh

client = pymongo.MongoClient("mongodb+srv://admin:12TPzLpCVUkL3Lvh@ds9-unit3-module3-k1toc.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg_data

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

q1 = 'SELECT * FROM charactercreator_character'
pg_curs.execute(q1)
chars = pg_curs.fetchall()
columns = [x[0] for x in pg_curs.description]

characters = []
for char in chars:
    td = {}
    for val, col in zip(char, columns):
        td[col] = val
    characters.append(td)

db.rpg_data.insert_many(characters)