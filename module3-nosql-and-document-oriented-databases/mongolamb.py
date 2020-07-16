import pymongo 
import datetime
import json
client = pymongo.MongoClient("mongodb+srv://foobarfoobar:foobarfoobar@cluster0.vvgzp.gcp.mongodb.net/?retryWrites=true&w=majority")
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

rpg_character = {'id': 1, "data": {'name': "test char", 'attr': [10,3,0,0]}}

rpg_test = db.rpg_test

rpg_test.insert_one(rpg_character)

json_url = "https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json"
import bson
with open('testdata.json') as json_file:
    rpg_json = json.load(json_file)[0]

rpg_mdb = db.rpg_data
table_id = rpg_mdb.insert_one(rpg_json)
curs = rpg_mdb.find({"_id": table_id})
print(curs.count())

