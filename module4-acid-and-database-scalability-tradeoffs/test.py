import pymongo
from password_example import password

client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-bxlcw.mongodb.net:27017,cluster0-shard-00-01-bxlcw.mongodb.net:27017,cluster0-shard-00-02-bxlcw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


print(list(db.rpg_data.find({'table_name': 'armory_weapon'})))