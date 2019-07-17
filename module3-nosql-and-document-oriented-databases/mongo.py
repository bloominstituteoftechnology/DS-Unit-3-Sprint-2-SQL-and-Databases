"""After watching Aaron's video and discussing a bit I'm not fighting with
learning mongo much more than this."""

import pymongo

password = 'Rob1!ert'

client = pymongo.MongoClient(f"mongodb+srv://pkutrich:{password}\
@cluster0-ibfsp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

doc = {'favorite_animal': 'narwhal'}
db.test.insert_one(doc)

print(list(db.test.find(doc)))
