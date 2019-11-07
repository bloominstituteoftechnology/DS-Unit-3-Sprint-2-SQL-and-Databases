"""
Upload Titanic data to MongoDB
"""

import pandas as pd
import numpy as np
import pymongo
from password_example import password
# Note: For the above to work, you'll have to change the
# password in password_example to whatever your
# mongoDB cluster's password is.


client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-bxlcw.mongodb.net:27017,cluster0-shard-00-01-bxlcw.mongodb.net:27017,cluster0-shard-00-02-bxlcw.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

df = pd.read_csv('titanic.csv')

columns = df.columns

for i in range(len(df)):
    row = df.loc[i]
    mongo_entry = {}
    for j in range(len(columns)):
        key = columns[j]
        value = row[j]
        # Mongo doesn't like numpy values, so any numpy value
        # needs to be converted. (I got the following code from Stack Overflow.)
        if isinstance(value, np.bool_):
            value = bool(value)
        elif isinstance(value, np.int64):
            value = int(value)
        elif isinstance(value, np.float64):
            value = float(value)
        mongo_entry[key] = value
    db.titanic.insert_one(mongo_entry)

print(db.titanic.find_one())

print(list(db.titanic.find({'Pclass': 1})))
# The above gives a giant list lol.
