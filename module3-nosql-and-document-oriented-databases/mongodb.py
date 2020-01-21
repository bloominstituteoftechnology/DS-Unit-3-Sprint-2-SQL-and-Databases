import requests
import json
import pymongo
import pandas as pd

URL = 'mongodb://<USERNAME>:<PASSWORD>@cluster0-shard-00-00-bbxlp.mongodb.net:27017,cluster0-shard-00-01-bbxlp.mongodb.net:27017,cluster0-shard-00-02-bbxlp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'

connection_string = URL
client = pymongo.MongoClient(connection_string)
data_url = 'https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json'

# Request API data
res = requests.get(data_url)

# Check if API data has been received
res.status_code

# Check the headers:
res.headers

# Convert res to json format
data = res.json()
data

# Check the data
for item in data[:1]:
    print(item.keys())
    print(item)
    print(item['fields'])
    print(type(item['fields']))
    print(item['fields'].keys())
    print(item['fields']['name'])
    for i in item['fields']:
        print(item['fields'][i])


db_game = client.test3
list(db_game.test.find({}))

# Insert API data into MongoDB
for item in data:
    for key in item.keys():
        if key == 0:
            key = '0'
    if not db_game.test.find_one(item):
        db_game.test.insert_one(item)


list(db_game.test.find({}))

# Create titanic db
db_titanic = client.test2

# load csv data to pandas dataframe
csv_url = 'https://raw.githubusercontent.com/zarrinan/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
t = pd.read_csv(csv_url)

# convert pandas dataframe to json string -> json object
js = t.to_json(orient='records')
d = json.loads(js)

# insert data into titanic db
for passenger in d:
    if not db_titanic.test.find_one(passenger):
        db_titanic.test.insert_one(passenger)  

# Check titanic db
list(db_titanic.test.find({}))
