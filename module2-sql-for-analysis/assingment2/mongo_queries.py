# These are the notes from Wednesday's MongoDB lecture.
# None of it is hooked up to anything.
# I would need to connect to my Mongo Database
# and put credentials in .env file, done near 1:15:00 of lecture

# uncomment

# import pymongo
# import os
# from dotenv import load_dotenv
# load_dotenv()
# DB_USER = os.getenv("MONGO_USER", default="OOPS")
# DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
# CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
# connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
# print("----------------")
# print("URI:", connection_uri)
# client = pymongo.MongoClient(connection_uri)
# print("----------------")
# print("CLIENT:", type(client), client)
# db = client.test_database_2 # "test_database" or whatever you want to call it
# print("----------------")
# print("DB:", type(db), db)
# collection = db.pokemon_collection_2 # "pokemon_test" or whatever you want to call it
# print("----------------")
# print("COLLECTION:", type(collection), collection)
# print("----------------")
# print("COLLECTIONS:")
# print(db.list_collection_names())
# collection.insert_one({
#     "name": "Pikachu",
#     "level": 30,
#     "exp": 76000000000,
#     "hp": 400,
#     "metadata": {
#         "a":"something",
#         "b":"something else"
#     }
# }) # can insert nested structures / documents!!!
# collection.insert_one({
#     "name": "Bulbasaur",
#     "level": 15,
#     "experience": 4000000,
#     "hp": 300,
# }) # can insert documents with different structures
# print("----------------")
# print("COLLECTIONS:")
# print(db.list_collection_names())
# print("DOCS:", collection.count_documents({})) # select *
# print("PIKA DOC:", collection.count_documents({"name": "Pikachu"})) # like a WHERE clause with filter conditions
# print("LOW LEVELS:", collection.count_documents({"level": {"$lt": 25}})) # like a WHERE clause with filter conditions