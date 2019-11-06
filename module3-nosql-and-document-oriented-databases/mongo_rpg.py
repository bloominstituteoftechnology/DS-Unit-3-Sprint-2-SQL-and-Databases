"""MongoDB is a very different animal from a PostgreSQL database.
Rather than having entries that are inherently related to each other
and similarly structured by virtue of occupying the same table,
MongoDB relies on unrelated entries to be structured in a way
that relates them when relevant. When you already have access to
JSON-formatted data, adding it to a MongoDB is simple (see below)."""

import pymongo
import json

from db import ACCESS

# connect to MongoDB
client = pymongo.MongoClient(ACCESS)
db = client.test

# data is now a list of json-formatted dicts -- mongo-ready
with open('testdata.json') as json_file:
    data = json.load(json_file)

db.test.delete_many({})  # so repeated running doesn't fill the db
db.test.insert_many(data)
# print(list(db.test.find({'model': 'charactercreator.character'})))
