# If colab not locally Find out the IP address of this Colab Instance
# !curl ipecho.net/plain
"""first make shell and install pymongo and dnspython"""
import pymongo

password = 'Aa02155120'  # Don't commit/share this! Reset it if it leak
User = 'Aa02155120'
dbname = 'test'
connection = ('mongodb+srv://Aa02155120:' + password +
              '@cluster0.nadgn.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient()
db = client.test
dir(db.test)
# Let's figure out inserting some data
help(db.test.insert)
help(db.test.insert_one)
db.test.count()
