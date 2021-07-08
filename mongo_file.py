#  connecting and trying MongoDB

import pymongo
connection_string = 'mongodb://4PCVgBLJ:yzPHeu8m@bn2stjwa-shard-00-00-cgxuq.mongodb.net:27017,bn2stjwa-shard-00-01-cgxuq.mongodb.net:27017,bn2stjwa-shard-00-02-cgxuq.mongodb.net:27017/test?ssl=true&replicaSet=bn2Stjwa-shard-0&authSource=admin&retryWrites=true'

client = pymongo.MongoClient(connection_string)

# check dir
dir(client)

# check the nodes (it's important)
client.nodes

# help
help(client.server_info)

# create a test file using client
# client is the connection between the server Mongo and creating the file here
db = client.test

dir(db)

# that's how we insert to doc in?
db.test.insert

# the methods either insert one instance or many
help(db.test.insert_one)
help(db.test.insert_many)

# example doc insertion
valeries_doc = {'favorite_animal': 'dolphin'}
if not db.test.find_one(valeries_doc):
    print('Inserting!')
    result = db.test.insert_one(valeries_doc)

# let's check if it can find what we just inserted
db.test.find_one(valeries_doc)

# let's assign what we are inserting into a variable form the above code
result = db.test.insert_one(valeries_doc)

result.inserted_id
db.test.find_one(valeries_doc)

list(results)

# Let's do Daniel's doc now
daniels_doc = {'favorite game': 'go'}
db.test.insert_one(daniels_doc)
db.test.find_one(daniels_doc)

# list out every result
list(db.test.find({}))

# let's insert more
db.test.insert_one({'1': 2, 'a': 3})

# another one
db.test.insert_one({'1': 2, 'a': 4, 'b': 17})

#  SELECT * FROM test WHERE key ='1' AND keys_value = 2 ("pseudo-SQL")
list(db.test.find({'1': 2}))
