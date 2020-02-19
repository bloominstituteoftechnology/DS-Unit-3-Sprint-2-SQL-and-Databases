import numpy as np
import os
import pandas as pd
import pymongo
import sqlite3
from dotenv import load_dotenv

# Get credentials from .env file
load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME")

client = pymongo.MongoClient(
    f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER_NAME}/test?retryWrites=true&w=majority'
    )
db = client.titanic

# Read the csv file
df = pd.read_csv('titanic.csv')

# Get the column names
column_names = df.columns

# Build the dictionary
for i in range(len(df)):
    row = df.loc[i]
    mongo_entry = {}
    for j in range(len(column_names)):
        key = column_names[j]
        value = row[j]
        # set the type of the value
        if isinstance(value, np.bool_):
            value = bool(value)
        elif isinstance(value, np.int64):
            value = int(value)
        elif isinstance(value, np.float64):
            value = float(value)
        mongo_entry[key] = value
    # Insert the rows
    db.titanic.insert_one(mongo_entry)

# Get a document
print(db.titanic.find_one())