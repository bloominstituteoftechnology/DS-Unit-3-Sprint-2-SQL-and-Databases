<<<<<<< HEAD
import pymongo
import json
import pandas as pd

# MongoDB and PostgreSQL both had their share of smooth sailing and of
#  hardship. In each case, massaging data to a readable format provided the
#  most headaches. I found working with PostgreSQL much easier overall. It's
#  hard to say which one is easier or harder to work with, though, because we 
# didn't spend much time with either. In both cases I'm left with the 
# impression that there's a great deal of power under the hood, and that at 
# scale amazing things are possible. I get the sense that the malleability of
#  working in a looser-schema'd environment like MongoDB could be more
#  difficult but allow more flexibility in types of data used, whereas
#  PostgreSQL and other relational databases are stricter about what you work
#  with but once you have the data in there it's relatively easy to look at it
#  how you want to.

client = pymongo.MongoClient("mongodb://bwhitman:mF44bPifV9miFea2@cluster0-shard-00-00-0zuv8.mongodb.net:27017,cluster0-shard-00-01-0zuv8.mongodb.net:27017,cluster0-shard-00-02-0zuv8.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

df = pd.read_json('rpg_data.json')
json_string = df.to_json(orient='records')
json_to_load = json.loads(json_string)
db.test.insert_many(json_to_load)
=======
import pymongo
import json
import pandas as pd

# MongoDB and PostgreSQL both had their share of smooth sailing and of
#  hardship. In each case, massaging data to a readable format provided the
#  most headaches. I found working with PostgreSQL much easier overall. It's
#  hard to say which one is easier or harder to work with, though, because we 
# didn't spend much time with either. In both cases I'm left with the 
# impression that there's a great deal of power under the hood, and that at 
# scale amazing things are possible. I get the sense that the malleability of
#  working in a looser-schema'd environment like MongoDB could be more
#  difficult but allow more flexibility in types of data used, whereas
#  PostgreSQL and other relational databases are stricter about what you work
#  with but once you have the data in there it's relatively easy to look at it
#  how you want to.

client = pymongo.MongoClient("mongodb://bwhitman:mF44bPifV9miFea2@cluster0-shard-00-00-0zuv8.mongodb.net:27017,cluster0-shard-00-01-0zuv8.mongodb.net:27017,cluster0-shard-00-02-0zuv8.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

df = pd.read_json('rpg_data.json')
json_string = df.to_json(orient='records')
json_to_load = json.loads(json_string)
db.test.insert_many(json_to_load)
>>>>>>> e129c9013501e4f576e512934244ce5e21ce9d99
