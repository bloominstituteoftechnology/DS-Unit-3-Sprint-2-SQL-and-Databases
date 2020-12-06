import pymongo
import sqlite3



password = "?"
dbname = "Cluster0"

def create_connection(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://rgiuffre90:" + password +"@cluster0.h7zhk.mongodb.net/"+ dbname +"?retryWrites=true&w=majority"
    )
    return client


def show_all(db):
    all_docs = list(db.test.find())
    return all_docs

# Sqlite3 transfer from rpg dataset

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Create query

def new_query(query):
    curs.execute(query)
    return curs.fetchall()

query = """
SELECT * FROM charactercreator_character;
"""
results = new_query(query)

# loop to extract data

characters = []

for character in results:
    doc = {
        'character_id' : character[0],
        'name' : character[1],
        'level' : character[2],
        'exp' :  character[3],
        'hp' : character[4],
        'strength' : character[5],
        'intellegence' : character[6],
        'dexterity' : character[7],
        'wisdom' : character[8]
    }
    characters.append(doc)

# Documents

doc1= {'X': 1}

blanknames_doc = {
    'food': 'salmon',
    'color': 'pink',
    'number': 3
}

blanknames_doc2 = {
    'food': 'lettuce',
    'color': 'gray',
    'number': 0
}

blanknames_doc3 = {
    'city': 'New York',
    'color': 'brown'
}

all_docs = [blanknames_doc, blanknames_doc2, blanknames_doc3]

if __name__ == "__main__":
    client = create_connection(password, dbname)
    db = client.test
    db2 = client.rpgdata
    db.test.insert_one(doc1)
    db.test.insert_many(all_docs)
    db2.rpgdata.insert_many(characters)

    print(db)
    print(db.test.count_documents({'X': 1}))
    print(db.test.find_one({'X': 1}))
    print(show_all(db))   