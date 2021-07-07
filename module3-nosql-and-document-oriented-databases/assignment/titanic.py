"""Copy titanic data from csv to MongoDb.

titanic.csv: ../../module2-sql-for-analysis/titanic.csv
"""

import os

import pandas as pd

from dotenv import load_dotenv
from pymongo import MongoClient

# establish environment
assert load_dotenv() == True, 'Unable to load .env'
MONGO_URL = os.getenv('MONGO_URL')
assert MONGO_URL is not None, 'MONGO_URL not found in environment'

# ensure input file is present and readable
CSV_FILE = os.path.join(os.path.dirname(__file__),
                        '../../module2-sql-for-analysis',
                        'titanic.csv')
assert os.path.isfile(CSV_FILE) and os.access(CSV_FILE, os.R_OK), \
    '../../module2-sql-for-analysis/titanic.csv NOT FOUND'

DB_NAME = 'titanic'
COLLECTION_NAME = 'passengers'

# get data from csv
df = pd.read_csv(CSV_FILE)
# clean up column names
df.columns = df.columns.str.replace('[^a-zA-Z0-9_-]', '')
print('Normalized column names:')
print(df.columns.tolist())

# convert dataframe to list of dictionaries
documents = [dict(row._asdict()) for row in df.itertuples(index=False)]

# connect to MongeDB server
client = MongoClient(MONGO_URL)
# remove existing database
if DB_NAME in client.list_database_names():
    client.drop_database(DB_NAME)
# create database
db = client[DB_NAME]
# create collection
collection = db[COLLECTION_NAME]
# add all documents
collection.insert_many(documents)

# verify
assert DB_NAME in client.list_database_names(), \
    f'DATABASE {DB_NAME} NOT FOUND BY MongoClient'
assert len(documents) == df.shape[0], \
    'NUMBER OF DOCUMENTS NOT EQUAL TO NUMBER OF ROWS IN DATAFRAME'
assert collection.count_documents(filter={}) == len(documents), \
    'DOCUMENT COUNT IN COLLECTION NOT EQUAL TO NUMBER OF DOCUMENTS'

# close connection
client.close()
