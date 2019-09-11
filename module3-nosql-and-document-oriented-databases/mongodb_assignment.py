'''
This file is the assigment Unit 3 Sprint 2 Module 3
Wednesday, Sept. 11 2019

The objective is to move data from a sqlite db to a mongo db.

Information necessary for connecting to MongoDB
--------------------
IP: 75.39.26.83
Username: jayson
password: layson
--------------------
'''

import pymongo
import sqlite3
import os
# NOT FULLY PEP8 COMPLIANT BECAUSE MY EDITOR WAS HAVING TROUBLE WITH THE LONG PATHS ON MULTIPLE LINES
# Create connection to sqlite database - not pep8 compliant but my editor was struggling to find the file
file = """C:/Users/ajaco/Desktop/repos/noreallyimfine/DS-Unit-3-Sprint-2-SQL-and-Databases/module3-nosql-and-document-oriented-databases/rpg_db.sqlite3"""
conn = sqlite3.connect(file)
curs = conn.cursor()

# Get all the tables
tables = curs.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()

# Create dict with table names as keys and table data as the values
table_dict = {}
for table in tables:
    query = 'SELECT * FROM ' + table[0]
    data = curs.execute(query).fetchall()
    table_dict[table[0]] = data

# Open connection to MongoDB
client = pymongo.MongoClient(
    """mongodb://jayson:layson@cluster0-shard-00-00-nxctz.mongodb.net:27017,cluster0-shard-00-01-nxctz.mongodb.net:27017,cluster0-shard-00-02-nxctz.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority""")
db = client.test

# Insert dictionary of data into MongoDB
db.test.insert_one(table_dict)

# See if its there
list(db.test.find())
