#pip install pymongo
import pymongo
import sqlite3

mong_password ='@_-Keaton1986'

client = pymongo.MongoClient(
  "mongodb://ThisIsJorgeLima:<password>@cluster0-shard-00-00-sn2m7.mongodb.net:27017,cluster0-shard-00-01-sn2m7.mongodb.net:27017,cluster0-shard-00-02-sn2m7.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test3
db

