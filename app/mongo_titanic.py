# app/mongo_rpg.py
# take the data from the titanic csv and move it to the MongoDB

import pymongo
import os
from dotenv import load_dotenv
# import sqlite3
import pandas as pd

# construct a path to where the titanic csv exists
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")

df = pd.read_csv(CSV_FILEPATH)
print("dimensions of titanic data:",df.shape)

# get the data into a list of dictionaries to make 
# inserting into mongo possible
# first I am going to rename a couple columns to get
# rid of spacing in the column headers
column_names = {
    "Siblings/Spouses Aboard": "Siblings_Spouses_Aboard",
    "Parents/Children Aboard": "Parents_Children_Aboard"
}

# rename the columns in the Dataframe
df = df.rename(columns=column_names)
print("________________")
print(df.columns)

# move each row (passenger data) to a dictionary
passenger_dictionary = df.to_dict(orient='records')

# connect to mongo database so we can transfer over the data from titanic
# passenger dictionary that we got from titanic csv.
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
# MONGO_URL = os.getenv("MONGO_URL", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

# use teh connection urit to connect to the mongoDB
client = pymongo.MongoClient(connection_uri)

# create the database inside mongo connection
db = client.titanic  # "test_database" or whatever you want to call it

# create the collection 
collection = db.titanic_passengers  # "pokemon_test" or whatever you want to call it

# insert our characters dictionary into the collection
collection.insert_many(passenger_dictionary)
print("passengers have been added")