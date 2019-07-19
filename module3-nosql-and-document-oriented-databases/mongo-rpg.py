import os
from pymongo import MongoClient
from dotenv import load_dotenv
import json

load_dotenv()

client = MongoClient(f"mongodb+srv://will:{os.getenv('DB_PASS')}@lambda-ds-will-a8q6c.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg_db
collection = db.rpg_db

filename = './testdata.json'

with open(filename, 'r') as f:
    datastore = json.load(f)

for item in datastore:
    collection.insert_one(item)