"""Copy data from rpg_db.sqlite3 into Mongodb.

rpg_db.sqlite: ../../module1-introduction-to-sql/rpg_db.sqlite3
"""

import os
import sqlite3

import pandas as pd

from dotenv import load_dotenv
from pymongo import MongoClient

# establish environment
assert load_dotenv() == True, 'Unable to load .env'
MONGO_URL = os.getenv('MONGO_URL')
assert MONGO_URL is not None, 'MONGO_URL not found in environment'

# ensure input file is present and readable
DB_FILE = os.path.join(os.path.dirname(__file__),
                       '../../module1-introduction-to-sql',
                       'rpg_db.sqlite3')
assert os.path.isfile(DB_FILE) and os.access(DB_FILE, os.R_OK), \
    '../../module1-introduction-to-sql/rpg_db.sqlite3 NOT FOUND'

DB_NAME = 'rpg_db'

def df_rows_to_list_of_dict(df):
    """Returns the rows of a dataframe as a list of dictionaries.

    Parameters:

    df: pandas dataframe

    Returns:
    rows of the dataframe as a list of dictionaries
    """
    return [dict(row._asdict()) for row in df.itertuples(index=False)]


def sqlite_to_dict_of_dataframes(conn):
    """Returns the tables of a sqlite database as a dictionary of dataframes.

    Parameters:

    conn: sqlite3.Connection

    Returns:
    dictionary of dataframes with table names as keys
    """
    df_tables = pd.read_sql_query(
        'SELECT name FROM sqlite_master WHERE type="table";',
        conn
    )
    return {
        table: pd.read_sql_query(f'SELECT * FROM {table}', conn)
        for table in df_tables['name']
    }

try:
    # connect to sqlite database
    conn = sqlite3.connect(DB_FILE)
    # connect to MongeDB server
    client = MongoClient(MONGO_URL)
    # remove existing Mongo database
    if DB_NAME in client.list_database_names():
        print(f'Dropping existing database: {DB_NAME}')
        client.drop_database(DB_NAME)
    # create Mongo database
    print(f'Creating database: {DB_NAME}')
    db = client[DB_NAME]
    # create and populate a collection in Mongo database
    # for each table in sqlite database
    for name, df in sqlite_to_dict_of_dataframes(conn).items():
        # create collection
        print(f'Creating collection: {name}')
        if df.shape[0] == 0:
            db.create_collection(name)
            print('... no data to insert.')
        else:
            collection = db[name]
            # populate collection
            collection.insert_many(df_rows_to_list_of_dict(df))
            # verify documents
            assert collection.count_documents(filter={}) == df.shape[0], \
                f'{name}: DOCUMENT COUNT NOT EQUAL TO COUNT OF DATAFRAME ROWS'
            print(f'... inserted {df.shape[0]} documents.')
finally:
    print('Closing database connections.')
    # close MongoDB connection
    client.close()
    # close sqlite connection
    conn.close()
