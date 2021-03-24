import os
import sqlite3
from dotenv import load_dotenv
import pandas as pd
import pymongo

# adds contents of the .env file to our enviornment
load_dotenv()

# 1. CONNECT TO SQLITE DATABASE
conn_sql = sqlite3.connect('C:/Users/dougcohen/Repos/Unit-3/DS-Unit-3-Sprint-2\
-SQL-and-Databases/module2-sql-for-analysis/app/rpg_db.sqlite3')
print('SQLITE CONNECTION:', conn_sql)


# 2. CONNECT TO MONGO DB
DB_USER = os.getenv('MONGO_USER', default='OOPS')
DB_PASSWORD = os.getenv('MONGO_PASSWORD', default='OOPS')
CLUSTER_NAME = os.getenv('MONGO_CLUSTER_NAME', default='OOPS')
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)


# 3. QUERY CHARACTER TABLE FROM SQLITE
cur_sql = conn_sql.cursor()
charactercreator_character_table = 'SELECT * FROM charactercreator_character;'
charactercreator_character_results = cur_sql.execute(charactercreator_character_table).fetchall()
# print('---------------')
# print(charactercreator_character_results)

# 4. CREATE DATABASE AND COLLECTION IN MONGO DB
db = client.rpg_db # "rpg_db" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)


collection = db.charactercreator_character # "charactercreator_character" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

# 4. CONVERT TABLE TO DATAFRAME

column_names = ['id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
df = pd.DataFrame(charactercreator_character_results, columns=column_names)
print(df.head())


# 5. IMPORT CHARACTER TABLE INTO MONGO DB USING df.to_dict('records')
collection.insert_many(df.to_dict('records'))
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names()) 