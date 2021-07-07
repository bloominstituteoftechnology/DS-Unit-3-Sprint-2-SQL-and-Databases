import pymongo
from credentials import CONNECTION_STRING
import json
import requests

# Fetch rpg data locally
dataurl = "https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json"
r = requests.get(dataurl) 
 
with open("testdata.json",'wb') as f:  
    f.write(r.content) 

# Read the JSON data
with open('testdata.json', 'r') as f:
    data = json.load(f)

client = pymongo.MongoClient(CONNECTION_STRING)
print(client.nodes)

db = client.rpg

db.rpg.insert_many(data)

result = db.rpg.find({'model': 'charactercreator.character', \
    'fields.name': 'Aliquid iste optio reiciendi'})

print(list(result))
