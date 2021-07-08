import pymongo
import json
import pandas as pd

# Connect to mongodb
client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-dyztz.mongodb.net:27017,cluster0-shard-00-01-dyztz.mongodb.net:27017,cluster0-shard-00-02-dyztz.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


def csv_to_mongo(df, collection_name):
    """Function to convert csv file into mongodb collection"""
    data = json.loads(df.to_json(orient='records'))
    new_col = db[collection_name]
    new_col.insert(data)


# Import Titanic data
titanic = pd.read_csv('titanic.csv')

# Load Titanic data to mongodb
csv_to_mongo(titanic, 'Titanic')
