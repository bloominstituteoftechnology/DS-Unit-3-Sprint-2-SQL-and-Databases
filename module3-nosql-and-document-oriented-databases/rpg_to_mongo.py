import os
import pymongo
import sqlite3
from dotenv import load_dotenv

# Get credentials from .env file
load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME")

client = pymongo.MongoClient(
    f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER_NAME}/test?retryWrites=true&w=majority'
    )
db = client.rpg

# Connect to sqlite rpg database
connection = sqlite3.connect('rpg_db.sqlite3')
cursor = connection.cursor()

# Get table names from the rpg database
# and add them in a list
table_names=[]
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
        AND name LIKE 'character%' OR name LIKE 'armory%'
    ORDER BY name;
    """)
grab_table = cursor.fetchall()
for item in grab_table:
    table_names.append(item[0])

for table in table_names:
    # Get the column names for each table
    query = f'PRAGMA table_info({table});'
    table_info = cursor.execute(query).fetchall()
    # The output for the above query has the id as first column
    # and the name as second column
    column_names = []
    for row in table_info:
        column_names.append(row[1])
    
    # Select all rows from each table
    query = f'SELECT * FROM {table};'
    table_rows = cursor.execute(query).fetchall()
    # Build the dictionary for the MongoDB entry
    # key -> column name
    # values -> row entries
    for row in table_rows:
        mongo_entry={}
        for i in range(len(column_names)):
            key = column_names[i]
            values = row[i]
            mongo_entry[key] = values
    
        # Insert the data
        db[table].insert_one(mongo_entry)

#------ Confirmation --------
# Print all collections
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# Count all documents for a collection
print("----------------")
collection = db.armory_item
print("COUNT ALL DOCUMENTS FOR armory_item COLLECTION:")
print(collection.count_documents({})) # Should be 174
