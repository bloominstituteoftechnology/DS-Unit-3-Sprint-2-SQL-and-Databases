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

# The main difference I experienced between MongoDB and 
# SQL is that in SQL I could visualize the data in actual
# tables, the way that I'm used to seeing it.  The relations
# between datapoints on different tables are much clearer,
# which I guess is what I'd expect of relational databases.