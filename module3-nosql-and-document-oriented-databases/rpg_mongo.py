#Pull out the IP address for this collab notebook
!curl ipecho.net/plain

# admin

#How do we figure out our python version?
import sys
print(sys.version)

!pip install pymongo

import pymongo

#Use 3.4 connection string for clarity

client = pymongo.MongoClient("mongodb://admin:password@cluster0-shard-00-00-za38b.mongodb.net:27017,cluster0-shard-00-01-za38b.mongodb.net:27017,cluster0-shard-00-02-za38b.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db

#check how many machines
client.nodes

help(db)

dir(db.test)

help(db.test.insert_one)

#Count how many documents
db.test.count_documents({'x':1})

#Insert a document
db.test.insert_one({'x': 1})

#Count again how many documents
db.test.count_documents({'x':1})

#Insert a document again
db.test.insert_one({'x': 1})

#Count again how many documents
db.test.count_documents({'x':1})

db.test.find_one({'x': 1})

db.test.find({'x':1})

curs = db.test.find({'x':1})

dir(curs)

list(curs)

jason_doc = {
    'favorite animal': ['Shark', 'Cats']
}

matthew_doc = {
    'favorite animal': 'Platypus'
}

nick_doc = {
    'favorite animal' : 'Hippogriff'
}

db.test.insert_many([jason_doc, matthew_doc, nick_doc])

list(db.test.find())

#Now let's make more docs.

more_docs = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i
  more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even':False}))

list(db.test.find({'favorite animal': 'Platypus'}))

help(db.test.update_one)

help(db.test.delete_one)

db.test.update_one({'value':3},
                   {'$inc': {'value': 5}})

list(db.test.find())

db.test.update_many({'even': True},
                    {'$inc': {'value':100}})

list(db.test.find({'even':True}))

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

#This gets error because not a dictionary!
#db.test.insert_one(rpg_character)
#Wrap it in a simple dictionary so that the insert_one method works
db.test.insert_one({'rpg_character' : rpg_character})

db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]

})

list(db.test.find())
