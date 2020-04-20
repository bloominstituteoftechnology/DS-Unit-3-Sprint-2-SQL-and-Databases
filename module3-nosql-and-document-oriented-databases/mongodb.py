import pymongo
import urllib
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_PW = os.getenv("MONGO_PW")
pw = urllib.parse.quote_plus(MONGO_PW)
mongo_url = "mongodb+srv://alexmjn:" + pw + "@cluster0-semjk.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url, connect = False)
print("client:", type(client))
#print(dir(client))
#class mongo client
db = client.test
#this creates new "test" database on the fly -
# not a "test" method." built in to pymongo.
print("db", type(db))
#print(dir(db))
#class pymongo.database.Database
result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
#class pymongo.results.InsertOneResult
print("result", type(result))
print(result.inserted_id)
print(db.test.find_one({'stringy key': [2, 'thing', 3]}))
