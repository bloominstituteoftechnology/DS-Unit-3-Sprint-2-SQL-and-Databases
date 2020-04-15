import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
import sqlite3

load_dotenv()




# "How was working with MongoDB different from working with
# PostgreSQL? What was easier, and what was harder?"
 # With MongoDB, I didnt have to first create a table to store my file but instead I created a collection. 
 # MongoDB seemed less fussy about how I stored the .json file into the collection in comparison
 # to all the issues I ran into trying to store the rpg.sqlite3 file into a PostgreSQL table
 # this could have been particular to the way I went about it - and the relative ease of
 # MongoDB could be due to all the time I spent the day before trying to figure out
 # how to pass in a file from sqlite3.
 # For sqlite3 i used a copy_from to load the csv, and for mongoDB I 
 # used a json.load to copy the the json file.


# Let's try to store the RPG data in our MongoDB

FILEPATH = os.path.join(os.path.dirname(__file__),"testdata.json")


MONGO_DB_USER = os.getenv("MONGO_DB_USER", default="OOPS")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD", default="OOPS")
MONGO_CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = "mongodb+srv://Kyle_Yates_Mongo:LAMBDADS13@cluster0-t0nfl.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

rpg_db = client['rpg_db'] # "test_database" or whatever you want to call it

collection = rpg_db['game_data']

# Code for deleting docs:

# x = collection.delete_many({})

# print(x.deleted_count, " documents deleted.")


# Code for loading data

# with open(FILEPATH) as f:
#     file_data = json.load(f)


# Code for inserting data

# collection.insert_many(file_data)

client.close()

print("DOCS:", collection.count_documents({}))
