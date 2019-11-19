# imports

import pymongo
import sqlite3
import csv

# get full driver from mongodb (copied from 'full driver example') & db

client = pymongo.MongoClient("mongodb://admin:ndNKACRnpi8KMofG@cluster0-shard-00-00-gn4uy.mongodb.net:27017,cluster0-shard-00-01-gn4uy.mongodb.net:27017,cluster0-shard-00-02-gn4uy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg

'''TRANSFORM .SQLITE3 FILE INTO .CSV'''

# connect to sqlite db and create cursor
sql_conn = sqlite3.connect('rpg_db_2.sqlite3')
csr = sql_conn.cursor()

# execute query of specific table
csr.execute("SELECT * FROM charactercreator_character;")

# transform this query to .csv
with open('rpg_db.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in csr.description])
    writer.writerows(csr)

# read .csv to df
import pandas as pd
rpg = pd.read_csv('rpg_db.csv')

'''Data to dictionary form for insertion in mongoDB'''

# transform df to dictionary
rpg_dict_ = rpg.to_dict(orient='records')

# insertion into mongoDB
db.rpg.insert_many(rpg_dict_)

# take a look at our db
list(db.rpg.find())
