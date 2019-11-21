# imports
import pandas as pd
import sqlite3
import pymongo

# connect to mongodb database
client = pymongo.MongoClient("mongodb://dbUser:P4AjNTd6QGtA7Kiw@cluster0-shard-00-00-xh0di.mongodb.net:27017,cluster0-shard-00-01-xh0di.mongodb.net:27017,cluster0-shard-00-02-xh0di.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg_items

# test connection
print(client.list_database_names())

# connect to sqlite database
sql_conn = sqlite3.connect('rpg_db.sqlite3')

# generate dataframe from rpg database
query = """SELECT * FROM armory_item"""
character_df = pd.read_sql(query, sql_conn)

# df to dict
db.rpg_items.insert_many(character_df.to_dict(orient='records'))

print(list(db.rpg_items.find()))