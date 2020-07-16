import pymongo
import datetime
import json
client = pymongo.MongoClient(
    "mongodb+srv://foobarfoobar:foobarfoobar@cluster0.vvgzp.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#collection =  db.test_collection

"""EXAMPLE FROM DOCS
represent a document as a dict, or json"""

testpost = {"author": "Dave Liu",
            "text": "trivial example of document",
            "tags": ["mongodb", "hello world", "python"],
            "date": datetime.datetime.now()}
posts = db.posts
post_id = posts.insert_one(testpost).inserted_id
print(post_id)

"""rpg """

rpg_character = {'id': 1, "data": {'name': "test char", 'attr': [10, 3, 0, 0]}}

rpg_test = db.rpg_test

rpg_test.insert_one(rpg_character)

"""  This was to clear out test data:
rpg_test.drop()
rpg_mdb.drop()

"""

with open('testdata.json') as json_file:  # local copy of json file from URL
    rpg_json = json.load(json_file)        # list cont dicts

coll = db.rpg_data          # referecen to rpg_data collection i.e. the data store
for r in rpg_json:          # each element r is a dict with a 'record' that will be
    coll.insert_one(r)      # inserted as a document

"""Verify that we have inserted what we think """

c = db["rpg_data"]
c.estimated_document_count()
