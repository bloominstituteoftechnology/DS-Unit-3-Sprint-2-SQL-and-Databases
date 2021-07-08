"""Script for taking restaurant.json data and transferring it to MongoDB."""

import sqlite3
import pymongo
import json


# Username and password to be set by user.
username = "TODO"
password = "TODO"
cluster = "TODO"
group = "TODO"

# Load json and select data.
json_data = open("restaurant.json").read().replace("$", "").split("\n")
json_data = [x for x in json_data if x != ""]
data = json.loads("[" + ",".join(json_data) + "]")

# Access MondoDB, create restaurant db and restaurant collection
s = "mongodb+srv://{}:{}@{}-{}.mongodb.net/admin".format(username,
                                                         password,
                                                         cluster,
                                                         group)
client = pymongo.MongoClient(s)
dbnames = client.list_database_names()
if 'restaurant' in dbnames:
    client.drop_database('restaurant')
rest_db = client["restaurant"]
x = rest_db["restaurants"].insert_many(data)
# Print number of objects added to MongoDB.
print(len(x.inserted_ids))
