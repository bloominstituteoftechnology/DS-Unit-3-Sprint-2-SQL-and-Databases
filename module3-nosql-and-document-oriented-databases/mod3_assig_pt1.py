# Module 3 Assignment
# Michael Toce - ds14
import pandas as pd
import numpy as np

#-----------------------------------------------------------------------------------------------------------------------
# HOW WAS WORKING WITH MongoDB DIFFERENT FROM WORKING WITH PostgreSQL?
# WHAT WAS EASIER AND WHAT WAS HARDER?
#-----------------------------------------------------------------------------------------------------------------------
# It's easier to understand the data with SQL because we can do some exploratory
# analysis by writing and executing queries. With MongoDB, there is no SQL, so
# we would need to download the data and use pandas for exploratory analysis.
# In terms of loading in data, relational databases utilized tuple lists while
# while MongoDB utilizes json files to load in the data. Both are fairly easy
# to work with, however it is important to know the differences between them.
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# 1: LOAD IN ENVIRONMENT VARIABLES
#-----------------------------------------------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

#-----------------------------------------------------------------------------------------------------------------------
# 2: READ IN RPG_DB FROM SQLITE3
#-----------------------------------------------------------------------------------------------------------------------
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

lite_conn = sqlite3.connect(DB_FILEPATH)
lite_curs = lite_conn.cursor()

get_first_table = '''
select *
from armory_item
'''

# cursor point to grab the object
lite_obj = lite_curs.execute(get_first_table).fetchall()
# use list comp to create tuple list from cursor object
lite_tlist = [list(x) for x in lite_obj]

# create df with lite_tlist
armory_items = pd.DataFrame(lite_tlist, columns = ['item_id', 'name', 'value', 'weight'])

armory_items.head()

#-----------------------------------------------------------------------------------------------------------------------
# 3: CONNECT TO MONGO_DB
#-----------------------------------------------------------------------------------------------------------------------
import pymongo
import json

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.rpg_db # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.rpg # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

#-----------------------------------------------------------------------------------------------------------------------
# 4: UPLOAD RPG_DB with PYTHON TO MONGO_DB
#-----------------------------------------------------------------------------------------------------------------------

# approach 1
records = json.loads(armory_items.T.to_json()).values()
db.collection.insert(records)
# prove that the db insert worked
print(db.list_collection_names())

# approach 2
# records = json.loads(df.to_json(orient='records'))
# db.collection.insert_many(df.to_dict('records'))

