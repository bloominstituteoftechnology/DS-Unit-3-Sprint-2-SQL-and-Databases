"""Script for taking json data and transferring it to MongoDB."""
# I found that MongoDB is easier for me to understand, mainly because I have
# worked with so many different functions and classes for Python, that it is
# easier than learning a new language, even though SQL is still really easy and
# intuitive. The main thing I found more difficult was that connection to
# MongoDB Atlas cloud was more difficult than ElephantSQL, but I had just made
# some stupid mistakes.

import sqlite3
import pymongo
import json


# Username and password to be set by user.
username = "TODO"
password = "TODO"
cluster = "TODO"
group = "TODO"

# Load json and select data.
data = json.loads(open("testdata.json").read())
collections = {}
for obj in data:
    if obj["model"] not in collections:
        collections[obj["model"]] = []
    d = obj["fields"]
    d["pk"] = obj["pk"]
    collections[obj["model"]].append(d)

# Access MondoDB, create rpg_db and charactercreator_character collection,
# and add data from json file.
s = "mongodb+srv://{}:{}@{}-{}.mongodb.net/admin".format(username,
                                                         password,
                                                         cluster,
                                                         group)
client = pymongo.MongoClient(s)
dbnames = client.list_database_names()
if 'rpg_db' in dbnames:
    client.drop_database('rpg_db')
rpg_db = client["rpg_db"]
for c in collections:
    x = rpg_db[c].insert_many(collections[c])
    # Print number of objects added to MongoDB.
    print(len(x.inserted_ids))
