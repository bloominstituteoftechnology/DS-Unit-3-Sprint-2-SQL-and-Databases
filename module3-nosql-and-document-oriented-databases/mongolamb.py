import pymongo 
import datetime
client = pymongo.MongoClient("mongodb+srv://foobarfoobar:foobarfoobar@cluster0.vvgzp.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#collection =  db.test_collection

"""represent a document as a dict, or json"""

testpost = {"author": "Dave Liu",
            "text": "trivial example of document",
            "tags": ["mongodb", "hello world", "python"],
            "date": datetime.datetime.now()}
posts = db.posts
post_id = posts.insert_one(testpost).inserted_id
print(post_id)
  