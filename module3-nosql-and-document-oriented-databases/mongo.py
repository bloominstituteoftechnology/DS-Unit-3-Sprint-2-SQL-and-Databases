iimport pymongo
import os
import json
from dotenv import load_dotenv
from pdb import set_trace as breakpoint

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/dspt6-inclass?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

print(client.list_database_names())

db = client.sample_analytics
print(db.list_collection_names())

customers = db.customers
print(customers.count_documents({}))

# Read the JSON file (copied from: https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json)
with open('test_data_json.txt') as json_file:
    rpg_data = json.load(json_file)

my_db = client.rpg_data

character_table = my_db.characters

character_table.insert_many(rpg_data)
print(character_table.count_documents({}))
