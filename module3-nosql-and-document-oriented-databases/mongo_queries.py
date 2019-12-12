import pymongo
import sqlite3

client = pymongo.MongoClient("mongodb+srv://btross:NWF77Q5rRin70QIT@cluster0-yevzi.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

print(list(db.test.find()))