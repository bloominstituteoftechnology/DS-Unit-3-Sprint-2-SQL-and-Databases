import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime
import dns
import json
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

try:
    connection_uri = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")
    print("Connected successfully!")
except:
    print("Could not connect to MongoDB :()") 


print("Now creating empty database in Mongo DB")
test_db = connection_uri.test

print("..................")

print('Now inserting rpg data into MongoDB')

try:
    with open('testdata.json') as json_file:
        rpg_data = json.load(json_file)
        print("Data inserted successfully!")
except:
    print("Import failed, data must already be uploaded")
    test_db.test.insert_many(rpg_data)

#  print the inserted data
cursor = test_db.test.find()
for record in cursor:
    print(record)

