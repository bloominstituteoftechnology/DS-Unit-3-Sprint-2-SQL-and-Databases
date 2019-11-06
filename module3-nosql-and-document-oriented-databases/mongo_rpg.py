import pymongo
import sqlite3

"""
QUESTION:  "How was working with MongoDB different from working with
38 PostgreSQL? What was easier, and what was harder?"

ANSWER: MongoDB does not have a schema but PostgreSQL does. MongoDB 
felt easier to setup initially.

"""

client = pymongo.MongoClient("mongodb://admin:<Password>@ds8-shard-00-00-ya1q2.mongodb.net:27017,ds8-shard-00-01-ya1q2.mongodb.net:27017,ds8-shard-00-02-ya1q2.mongodb.net:27017/test?ssl=true&replicaSet=DS8-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Sqlite setup
s3_conn = sqlite3.connect('rpg_db.sqlite3')
s3_curs = s3_conn.cursor()

# Char Query (only displaying first one)
ppl = s3_curs.execute('SELECT * FROM charactercreator_character;').fetchall()


# Function for making dictionary from ppl
def dict_ppl(x):
    more_ppl = []
    for i in range(len(x)):
        ppls_dict = {'char': x[i]}
        more_ppl.append(ppls_dict)
    return more_ppl


# Creating final dictionary object
dict_ppl_list = dict_ppl(ppl)

# Insert into MongoDB and print list from database from mongoDB
db.test.insert_many(dict_ppl_list)
print(list(db.test.find()))
