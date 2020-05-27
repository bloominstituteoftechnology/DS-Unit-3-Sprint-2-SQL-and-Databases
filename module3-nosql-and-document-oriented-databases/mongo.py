import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
hostname = os.getenv('hostname')

print(username)
print(password)
print(
    f"mongodb+srv://{username}:{password}@cluster0-paxoc.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@{hostname}/test?retryWrites=true&w=majority")
db = client.test
print('db', db)

try:
    print('hahaha')
    result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
    print(result.inserted_id)
    print(db.test.find_one({'stringy key': [2, 'thing', 3]}))
except:
    print("Err")
