import pymongo

pwd = 'NKtCh2Wet9VeBtw'
conn_str = 'mongodb://edc:'+pwd+'@cluster0-shard-00-00-4q5yv.mongodb.net:27017,cluster0-shard-00-01-4q5yv.mongodb.net:27017,cluster0-shard-00-02-4q5yv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
client = pymongo.MongoClient(conn_str)
db = client.rpg

edc_doc = {'guitar': '1959 Gibson Les Paul'}
if not db.rpg.find_one(edc_doc):
    db.rpg.insert_one(edc_doc)
r = db.rpg.find()
results = list(r)
for doc in results:
    print(type(doc))
    print(doc)
