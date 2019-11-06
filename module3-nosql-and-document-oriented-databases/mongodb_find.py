""" code to pull up the table without adding more stuff to it"""

import pymongo

password = 'L7bBVGuzHz8QjX4j'

client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-pafox.mongodb.net:27017,cluster0-shard-00-01-pafox.mongodb.net:27017,cluster0-shard-00-02-pafox.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print(list(db.test.find()))
