import pandas as pd 
import pymongo
import rpg_data


client = pymongo.MongoClient("mongodb://admin:asdfghjkl@cluster0-shard-00-00-uglnr.mongodb.net:27017,cluster0-shard-00-01-uglnr.mongodb.net:27017,cluster0-shard-00-02-uglnr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


#insert data
db.test.insert_many(rpg_data)



