import pymongo
client = pymongo.MongoClient("mongodb+srv://cshields143:Th30rum143@cluster0-qacvh.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

import json
data = json.load(open('rpg.json'))
data2 = list(filter(lambda x: x['model'] == 'charactercreator.character', data))
chars = [row['fields'] for row in data2]

for ch in chars:
  db.test.insert_one(ch)