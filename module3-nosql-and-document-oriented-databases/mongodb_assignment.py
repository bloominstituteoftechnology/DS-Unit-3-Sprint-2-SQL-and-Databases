
import sqlite3
import json

filename = "rpg_db.sqlite3"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect(filename)
connection.row_factory = dict_factory
cursor = connection.cursor()
cursor.execute("SELECT * FROM armory_weapon")
results = cursor.fetchall()
print(results)
connection.close()

import pymongo
import urllib
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_PW = os.getenv("MONGO_PW")
pw = urllib.parse.quote_plus(MONGO_PW)
mongo_url = "mongodb+srv://alexmjn:" + pw + "@cluster0-semjk.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url, connect = False)

db = client.rpg_data
name = "armory_weapon"
collection = db[name]
collection.insert_many(results)
print(collection.count_documents({}))
