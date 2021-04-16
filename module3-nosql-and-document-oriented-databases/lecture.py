#!/usr/bin/env python

import pymongo

with open('./module3-nosql-and-document-oriented-databases/mongodb-password', 'r') as pwfile:
	PASSWORD = pwfile.read()

url = f'mongodb+srv://dbadmin:{PASSWORD}@c0-wudpf.azure.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)
db = client.test

db.test.insert_one({'x': 4})
db.test.insert_one({'x': 2})
db.test.insert_one({'y': 1})

print(db.test.count_documents({'x': 2}))
