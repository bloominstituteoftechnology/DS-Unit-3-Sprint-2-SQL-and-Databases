import pymongo
import json

a = 'mongodb://DekuTree:MasterMind1211@cluster0-shard-00-00-blbw2.mongodb.net:27017,cluster0-shard-00-01-blbw2.mongodb'
b = '.net:27017,cluster0-shard-00-02-blbw2.mongodb.net:27017/test?ssl=true&replicaSet='
c = 'Cluster0-shard-0&authSource=admin&retryWrites=true'

client = pymongo.MongoClient(a + b + c)
print(client.list_database_names())

with open('testdata.json') as f:
    data = json.load(f)

client['Test_DB']['testdata'].insert_many(data)
