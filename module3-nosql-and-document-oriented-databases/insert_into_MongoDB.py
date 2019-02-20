import pymongo
import json

"""I have a file called rpg_as_json.json in the directory"""


client = pymongo.MongoClient("mongodb://<username>:<PassWord>@lambda-mongo-db-shard-00-00-ht3ri.mongodb.net:27017,lambda-mongo-db-shard-00-01-ht3ri.mongodb.net:27017,lambda-mongo-db-shard-00-02-ht3ri.mongodb.net:27017/test?ssl=true&replicaSet=Lambda-Mongo-DB-shard-0&authSource=admin&retryWrites=true")

with open('rpg_as_json.json') as f:
	file_data = json.load(f)

# client is my pymongo.MongoClient() 
# create a MongoDB called rpg

rpg = client.rpg

# create a collection called rpg_table
rpg_table = rpg['rpg_data']

# insert the JSON file into rpg_table
rpg_table.insert_manyy(file_data)

# And now if we go to MongoDB Atlas the rpg Database appears in the cluster I created earlier

