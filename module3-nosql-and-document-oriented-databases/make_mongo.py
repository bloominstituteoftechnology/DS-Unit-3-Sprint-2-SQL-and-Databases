import json
import pymongo
import pandas as pd
from password import password

# Instantiate client and see if a test database works
client = pymongo.MongoClient("mongodb+srv://dimakav:" + password + "@cluster0-41he1.mongodb.net/test?retryWrites=true")
db = client.test
result = db.test.insert_one({'string key': [2, 'thing', 3]})
print('Test db is working, heres the inserted id:', result.inserted_id)

# Create a new database for rpg
db = client.rpgdb
with open('rpg_data.json') as f:
    file_data = json.load(f)
db.rpgdb.insert_many(file_data)

# How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?

# Working with MongoDB is way different from SQL. The SQL table structure
# is much more pandas friendly and the querying syntax is more intuitive to me.
# The most important distinction between the two SQL is vertically scalable,
# (think of this as adding floors to building) whereas noSQL is horizontally
# scalable (adding more buildings). For SQL, performance is increased by adding
# CPU, RAM, or faster hds. Mongo traffic capcacity is increased by sharding or
# adding more servers.
