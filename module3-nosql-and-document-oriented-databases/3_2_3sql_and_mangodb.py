# -*- coding: utf-8 -*-
"""3.2.3SQL_and_MangoDB.ipynb

"How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"

The biggest difference between the two was how the information was stored. In PostgreSQL we use schemas
that connect different tables that holds the data. PostgreSQL uses relational databases to organize and
work with the data. MongoDB, on the other hand, stores all of the data in documents. Documents seem to
be free floating units that aren't necessarily related to other documents, other than being in the same
database. What's interesting about documents is that they don't have standard rows, columns, features, etc.
set up by the user, but can all be completely unique from one another.
"""

!pip install pymongo

!curl ipecho.net/plain

"""Username: Admin
password: 6$b2BFPXAy2^
"""

import pymongo


client = pymongo.MongoClient("mongodb://admin:6$b2BFPXAy2^@cluster0-shard-00-00-hwd8g.mongodb.net:27017,cluster0-shard-00-01-hwd8g.mongodb.net:27017,cluster0-shard-00-02-hwd8g.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

db    # This is telling us how many computers are working on this right now.

client.nodes

help(db)

dir(db.test)

dir(db.test.insert_one)

db.test.count_documents({'x':1})

# There are 0 becuase this is an empty document.

#Insert a document
db.test.insert_one({'x': 1})

# Do the count again
db.test.count_documents({'x':1})

db.test.find_one({'x':1})

db.test.find({'x':1})

curs = db.test.find({'x':1})

dir(curs)

# Tells us where the two documents are. They're two documents even though they're the same.
list(curs)

#JSON objects

samantha_doc = {
    'favorite animal': ['Kokopo', 'Dog']
}

rosie_doc = {
    'favorite animal': 'Snakes',
    'favorite color': 'Cyan'
}

amer_doc = {
    'favorite animal':'Red Panda'
}

db.test.insert_many([samantha_doc, rosie_doc, amer_doc])

# These are all of the objects we've put in.
list(db.test.find())

# Let's make more documents
more_docs = []
for i in range(10):
  doc = {'even': i % 2 ==0}
  doc['value'] = i
  more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find())

list(db.test.find({'even': False}))

list(db.test.find({'favorite animal': 'Red Panda'}))

help(db.test.update_one)

db.test.update_one({'value':3},
                   {'$inc':{'value':5}})

list(db.test.find())

db.test.update_many({'even':True},
                    {'$inc': {'value':100}})

list(db.test.find({'even':True}))

db.test.delete_many({'even':False})

list(db.test.find())

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)  # Db.insert_one wouldn't work on this because this isn't a dictionary

# Wrap this in a simple dictionary so that the inser_one method works.
db.test.insert_one({'rpg_character': rpg_character})

list(db.test.find())

db.test.insert_one({
    'sql_id': rpg_character,
    'name': rpg_character,
    'hp': rpg_character,
    'level': rpg_character
})

list(db.test.find())
