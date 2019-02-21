# ./usr/bin/env python
" Importing from JSON to MongoDB"

from dotenv import load_dotenv
import os
import pymongo
import requests
load_dotenv()
URL = os.getenv("MongoDB_URL")

client = pymongo.MongoClient(connection_string)
response = requests.get(URL)
data = response.json()
collection = db.rpg_collection
result = collection.insert_many(data)
