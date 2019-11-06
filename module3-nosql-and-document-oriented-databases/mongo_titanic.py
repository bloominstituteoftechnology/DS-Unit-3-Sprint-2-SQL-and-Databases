import pandas as pd
import pymongo

from db import ACCESS

df = pd.read_csv('titanic.csv')

# connect to MongoDB
client = pymongo.MongoClient(ACCESS)
db = client.test

# add each row of titanic to db
for i in range(df.shape[0]):
    row = {
        'survived': str(df.iloc[i][0]),
        'class': str(df.iloc[i][1]),
        'name': str(df.iloc[i][2]),
        'sex': str(df.iloc[i][3]),
        'age': str(df.iloc[i][4]),
        'sibspouse': str(df.iloc[i][5]),
        'parentchild': str(df.iloc[i][6]),
        'fare': str(df.iloc[i][7])
    }
    db.test.insert_one(row)
