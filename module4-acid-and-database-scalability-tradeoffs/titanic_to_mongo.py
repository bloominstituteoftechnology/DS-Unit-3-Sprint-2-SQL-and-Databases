import pymongo
import sqlite3

# MONGO DB STUFF
client = pymongo.MongoClient("mongodb+srv://admin:L2oz0xJtZmJwfTsg@cluster0-2wndt.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# SQLITE3 STUFF
conn = sqlite3.connect('titanic')
curs = conn.cursor()

# EXECUTE QUERY AND SAVE FETCHALL TO passengerS
curs.execute('SELECT * FROM titanic')
passengers = curs.fetchall()

# THIS CODE IS FOR THE ABILITY TO RE-RUN WITHOUT ISSUES
if list(db.test.find()) != []:
    db.test.delete_many({})

# FOR EACH passenger IN THE DATABASE, CREATE A DOCUMENT IN MONGO
for passenger in passengers:
    db.test.insert_one({
        'id': passenger[0],
        'survived': passenger[1],
        'pclass': passenger[2],
        'sex': passenger[4],
        'age': passenger[5],
        'siblings_spouses_aboard': passenger[6],
        'parents_children_aboard': passenger[7],
        'name': passenger[3],
        'fare': passenger[8]
    })

# PRINT EACH DOC ONE AT A TIME
for doc in list(db.test.find()):
    print(doc)