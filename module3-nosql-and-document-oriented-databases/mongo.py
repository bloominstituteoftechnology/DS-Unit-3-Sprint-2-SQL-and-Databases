import pymongo
import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()

conn = sqlite3.connect(os.path.join(os.path.dirname(
    __file__), 'rpg_db.sqlite3'))
curs = conn.cursor()

username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('host')

print(host)
client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority")
db = client.test
print('db', db)

# try:
#     print('hahaha')
#     result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
#     print(result.inserted_id)
#     print(db.test.find_one({'stringy key': [2, 'thing', 3]}))
# except:
#     print("Err")

# query_1 = 'SELECT * FROM armory_item;'
# ans_1 = curs.execute(query_1).fetchall()
# print(f'How many total Characters are there? {ans_1}')
