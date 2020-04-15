# queries to find aspects of the databases we created.

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
# MONGO_URL = os.getenv("MONGO_URL", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# use the connection uri to connect to the mongoDB
client = pymongo.MongoClient(connection_uri)

# link to the db and the collection with in the mongo db
db = client.titanic
collection = db.titanic_passengers

# write a query 
# how many passengers were 35 or older
print(collection.count_documents({"Age": {"$gte": 35}}))
print("____________")

# how many passengers had a spouse or a sibling on board
# BUT no parents or children on board?
print(collection.count_documents(
                                 {"$and": [{"Siblings_Spouses_Aboard": {"$gte": 0}},
                                 {"Parents_Children_Aboard": {"$eq": 0}}]}))