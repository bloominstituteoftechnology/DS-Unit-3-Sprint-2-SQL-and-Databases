import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:GumMjaykCrVjxWCs@cluster0-jvz2z.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
# print(db)

# print(client.nodes)

# db.test.insert_one({'x':1})
print(db.test.count_documents({'x':1}))

artins_doc = {'favorite animal': 'silver panther'}
db.test.insert_one(artins_doc)
print(db.test.find_one(artins_doc))

# Find will find all matching 
results = db.test.find({'x': 1})
print(list(results))