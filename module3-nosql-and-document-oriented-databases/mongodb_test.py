import pymongo
client = pymongo.MongoClient(
    "mongodb://aaron-huizenga@lambdastudents.com:MpO22RB2O6kgq7ae@mycluster0-shard-00-00.mongodb.net:27017,mycluster0-shard-00-01.mongodb.net:27017,mycluster0-shard-00-02.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin")
db = client.test

db

dir(db)

db.test

help(db.test.insert_one)

db.test.count_documents({'x': 1})

db.insert_one({'x': 1})

db.test.count_documents({'x': 1})

db.insert_one({'x': 1})

db.test.count_documents({'x': 1})

db.test.find_one({'x': 1})

curs = db.test.find({'x': 1})

curs

dir(curs)

list(curs)

aarons_doc ={
    'name': 'aaron',
    'favorite_animal': 'dog',
    'favorite_color': 'green',
    'favorite_number': 5,
    'favorite_tv_show': 'riverdale'
}

juds_doc = {
    'name': 'jud',
    'favorite_animal': 'liger',
    'favorite_color': 'green',
    'favorite_sport': 'football'
}

baisali_doc = {
    'name': 'baisali',
    'favorite_animal': 'elephant',
    'favorite_color': 'red',
    'favorite_number': 2
}

faraazs_doc ={
    'name': 'faraaz',
    'favorite_animal': 'ring-tailed lemur',
    'favorite_color': 'forest green',
    'favorite_restaurant': 'in-n-out'
}

all_docs = [aarons_doc, juds_doc, baisali_doc, faraazs_doc]

len(all_docs)

db.test.insert_many(all_docs)

list(db.test.find())

more_docs = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i
  more_docs.append(doc)

more_docs

db.test.insert_many(more_docs)

list(db.test.find({'even': True, 'value': 0}))

list(db.test.find({'even': True}))

list(db.test.find({'favorite_color': 'green'}))

# What is CRUD?
# C - Create
# R - Read
# U - Update
# D - Delete

# AKA - As Aaron Gallant puts it - most apps
rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)

# Lazy and not good for long term goals
db.test.insert_one({'rpg_character': rpg_character})

db.test.find_one({'rpg_character': rpg_character})

# Ideal even though SCHEMA isn't required, we should make informative/useful
# key names in our docs
rpg_doc = {
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
}
db.test.insert_one(rpg_doc)

list(db.test.find(rpg_doc))