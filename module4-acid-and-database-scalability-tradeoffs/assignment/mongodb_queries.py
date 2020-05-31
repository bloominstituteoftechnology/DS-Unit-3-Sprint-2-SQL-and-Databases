import os
from dotenv import load_dotenv
import pymongo


load_dotenv()

DB_USER = os.getenv('MONGO_DB_USER', default='oops')
DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', default='oops')
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME', default='oops')

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_uri)
db = client.rpg_database

# How many total Characters are there?
collection = db.charactercreator_character
result = collection.count_documents({})
print(f'There are {result} total characters')

# How many of each specific subclass?

# How many total Items?

# How many of the Items are weapons? How many are not?

# How many Items does each character have? (Return first 20 rows)

# How many Weapons does each character have? (Return first 20 rows)

# On average, how many Items does each Character have?

# On average, how many Weapons does each character have?


client.close()

