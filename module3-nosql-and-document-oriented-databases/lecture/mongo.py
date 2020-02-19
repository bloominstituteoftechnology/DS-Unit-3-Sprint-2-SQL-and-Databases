
import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

assert load_dotenv() == True, 'Unable to load .env'
MONGO_URL = os.getenv('MONGO_URL')
assert MONGO_URL is not None, 'MONGO_URL not found in environment'

client = MongoClient(MONGO_URL)

def ddir(o):
    print(type(o))
    for a in [attrib for attrib in dir(o) if not attrib.startswith('_')]:
        print(a)

# db = client.gettingStarted
# people = db.people
# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }
# people.insert_one(personDocument)
# print(client)