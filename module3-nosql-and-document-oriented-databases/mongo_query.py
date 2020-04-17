import pymongo
import os
#from dotenv import load_dotenv

#load_dotenv()

"""
client = pymongo.MongoClient("mongodb+srv://hkang:<password>@cluster0-ihfxe.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
print(result.inserted_id)
print(db.test.find_one({'stringy key': [2, 'thing', 3]}))
"""
DB_USER = 'hkang'
DB_PASSWORD = 'dotenvsucks'
CLUSTER_NAME = "cluster0-ihfxe"

#_________________________________________________________________________
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # name the database "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

#_________________________________________________________________________
# Let's insert some documents

# here's a single document
collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400, }    )

# let's insert a full team

warturtle = {"name": "Warturtle", "level": 90, "exp": 100, "hp": 1000, }

jigglypuff = {"name": "Jigglypuff", "level": 99, "exp": 100000000000, "hp": 500, }

# let's give this one some attacks
charizard = {"name": "charizard", "level": 30, "exp": 4450000000, "hp": 500,
    "learned_moves":{"flamethrower":30, "fly": 42 } }

pikachu = {"name": "Pikachu", "level": 80, "exp": 90000000000, "hp": 900, }

swampert = {"name": "Swampert", "level": 100, "exp": 1059860, "hp": 361,}

snorlax = {"name": "Snorlax", "level": 100, "exp": 1059860, "hp": 361,}

team = [warturtle, jigglypuff, charizard, pikachu, swampert, snorlax]

collection.insert_many(team)


#_________________________________________________________________________
# Let's try querying (filtering and printing results)
# We'll use common examples that we saw in SQL

# similar to SELECT count(id) FROM pokemon
print("DOCS:", collection.count_documents({}))

# similar to SELECT * FROM pokemon WHERE name = "pikachu"
print("Count Pikachus:", collection.count_documents({"name": "Pikachu"}))

# SELECT * FROM pokemon WHERE name = "pikachu" LIMIT 1
pika = collection.find_one({"name":"Pikachu"})
print("One Pikachu" , pika)

# SELECT * FROM pokemon WHERE name = "pikachu" 
pikas = list(collection.find({"name":"Pikachu"}))
print("All Pikachus")
for pikachu in pikas:
    print(pikachu)

#_________________________________________________________________________
# Let's try more advanced queries

# Range Query
# for valid operators, use https://docs.mongodb.com/manual/reference/operator/query/ 

# let's look for only high level pokemon with level >= 70
high_level = list(collection.find({"level": {"$gte": 70} }))
print("High Level Pokemon")
for pokemon in high_level:
    print(pokemon)
