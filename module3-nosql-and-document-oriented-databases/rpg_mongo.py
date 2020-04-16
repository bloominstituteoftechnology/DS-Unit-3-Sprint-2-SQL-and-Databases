import pymongo
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.rpg_database
print("----------------")
print("DB:", type(db), db)

collection = db.charactercreator_character
print("----------------")
print("collection:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

JSON_DATA_URL = "https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json"
df = pd.read_json(JSON_DATA_URL)
records = df[df.model == "charactercreator.character"]["fields"].tolist() 

collection.insert_many(records)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

print("DOCS:", collection.count_documents({}))

# How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?


