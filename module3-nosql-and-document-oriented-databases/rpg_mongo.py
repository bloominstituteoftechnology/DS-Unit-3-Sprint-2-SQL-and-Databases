import pymongo
import os
from dotenv import load_dotenv
import sqlite3
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("URI:", connection_uri)


client = pymongo.MongoClient(connection_uri)
print("----------------")

print("CLIENT:", type(client), client)
db = client.rpg
print("----------------")
print("DB:", type(db), db)

collection = db.armory_item

rpg_connection = sqlite3.connect("rpg_db.sqlite3")
rpg_cursor = rpg_connection.cursor()

query = """
SELECT
*
FROM armory_item
"""

item_result = rpg_cursor.execute(query).fetchall()


for i in range(len(item_result)):
    collection.insert_one({
        "item_id": item_result[i][0],
        "name": item_result[i][1],
        "value": item_result[i][2],
        "weight": item_result[i][3]
    })
