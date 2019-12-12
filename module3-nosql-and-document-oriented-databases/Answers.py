"""How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?

- Different API. PostgreSQL psychopg2 has issues when trying to install it and use it with pure python. Easier to install and use pymongo

- elephant SQL, practice sql queries, with mongoDB, no practicing sql queries

- MongoDB is easier to work with because you don't have to worry about your connection closing and shuting you out when you make a mistake list PostgreDB does. 

- MongoDB only accepts data in dictionary format, PostreDB accepts Tables
"""

import pymongo

# establishing connection to MongoDB database

username: admin
password: r4rCSZfx1Wt97ztV

client = pymongo.MongoClient("mongodb://admin:r4rCSZfx1Wt97ztV@experiment-shard-00-00-ulgaw.mongodb.net:27017,experiment-shard-00-01-ulgaw.mongodb.net:27017,experiment-shard-00-02-ulgaw.mongodb.net:27017/test?ssl=true&replicaSet=experiment-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

dir(db.test)

# insert a document
db.test.insert_one({'x':1})

# count how many documents to verify that document was correctly inserted. 
db.test.count_documents({'x':1})

# looking for a document
db.test.find({'x':1})

# find a specific document and store it's location in the variable curs
curs = db.test.find({'x':1})

# creating many different documents
evidence_doc = {
    'favorite animal': 'Black Panther',
    'favorite color': 'Red'
}

next_doc = {
    'favorite animal': ['Unicorn', 'Cats']
}

expe_doc = {
    'favorite color': ['red', 'blue', 'green']
}

# inserting many documents at once
db.test.insert_many([expe_doc, next_doc, evidence_doc])

#look at all documents
list(db.test.find())

# creating a for loop that will generate many documents and 
# append it ot more_docs list
more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0 } # 'even' = key, 'i % 2 == 0' is value
    doc['number'] = i # 'value' = key, 'i' is value
    more_docs.append(doc)
    
# verifying that the for loop worked. 
more_docs

# inserting many documents
db.test.insert_many(more_docs)

# list all documents
list(db.test.find())

# update one document
db.test.update_one({'number':3},
                  {'$inc': {'number': 5}})

# list all documents
list(db.test.find())

# update many documents
db.test.update_many({'even': True},
                   {'$inc': {'number': 100}})

# delete many documents
db.test.delete_many({'even': False})

list(db.test.find())

# in order to insert something into MongoDB, it needs to be a dictionary in order to be cast to MongoDB. So, trying to insert a list or tuple will throw an error. 

# how to cast a tuple into a dictionary
rpg_example = (1, 'King Bob', 10, 3, 0, 0, 0)
# this will produce an error message, 
# db.test_one(rpg_character)

# instead, cast it into a dictionary
db.test.insert_one({'rpg_example': rpg_example})

db.test.insert_one({
    'sql_id': rpg_example[0],
    'name': rpg_example[1],
    'hp': rpg_example[2],
    'level': rpg_example[3]
})

list(db.test.find())
