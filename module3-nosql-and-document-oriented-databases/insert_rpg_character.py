# imports

import pymongo
import sqlite3
import requests

# full driver from mongodb (copied from 'full driver example')

client = pymongo.MongoClient("mongodb://admin:ndNKACRnpi8KMofG@cluster0-shard-00-00-gn4uy.mongodb.net:27017,cluster0-shard-00-01-gn4uy.mongodb.net:27017,cluster0-shard-00-02-gn4uy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg

sql_conn = sqlite3.connect('rpg_db_2.sqlite3')
csr = sql_conn.cursor()

csr.execute("SELECT * FROM charactercreator_character;")

import csv
with open('rpg_db.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in csr.description])
    writer.writerows(csr)

import pandas as pd
rpg = pd.read_csv('rpg_db.csv')

rpg_dict_ = rpg.to_dict(orient='records')

db.rpg.insert_many(rpg_dict_)

list(db.rpg.find())
