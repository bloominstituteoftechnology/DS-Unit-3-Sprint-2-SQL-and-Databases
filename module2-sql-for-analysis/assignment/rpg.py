"""Creates and populates PostgreSql tables from rpg_db.sqlite3

Reads data from '../../module1-introduction-to-sql/rpg_db.sqlite3',
relative to this file.
"""

import os
import sqlite3

import pandas as pd
import psycopg2
from dotenv import load_dotenv
from psycopg2.errors import UndefinedTable

assert load_dotenv() == True, 'Failed to load .env'
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
assert DB_NAME is not None, 'DB_NAME not found in environment'
assert DB_USER is not None, 'DB_USER not found in environment'
assert DB_PASS is not None, 'DB_PASS not found in environment'
assert DB_HOST is not None, 'DB_HOST not found in environment'

DB_FILE = os.path.join(os.path.dirname(__file__),
                       '../../module1-introduction-to-sql',
                       'rpg_db.sqlite3')
assert os.path.exists(DB_FILE), \
    '../../module1-introduction-to-sql/rpg_db.sqlite3 NOT FOUND'


def fix_create_query(query):
    """Return a PostgreSql CREATE query from a SQLite CREATE query."""
    query = query.replace(
        'integer NOT NULL PRIMARY KEY AUTOINCREMENT',
        'SERIAL NOT NULL PRIMARY KEY')
    query = query.replace(' datetime ', ' text ')
    query = query.replace('(name,seq)', '(name text, seq int)')
    query = query.replace(' unsigned ', ' ')
    query = query.strip() + ';'
    return query


def get_max_referenced_index(references, names):
    """Return the largest index referenced in a pandas.Series.

    Parameters:

    references: list of names that are in a pandas.Series (names)

    names: pandas.Series to get indexes for a matched name

    Returns:
    largest index of [ref in references] in names
    """
    if len(references) == 0:
        return 0
    return max([
        names[names==ref].index[0]
        for ref in references
    ])


conn_sql = sqlite3.connect(DB_FILE)
conn_pgs = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST
)

try:
    cursor = conn_pgs.cursor()
    df_tables = pd.read_sql_query(
        'SELECT name, sql FROM sqlite_master WHERE type="table";',
        conn_sql
    )
    drop_tables = 'DROP TABLE IF EXISTS ' + ','.join(df_tables['name']) + ';'
    print('Dropping known tables, if present')
    cursor.execute(drop_tables)

    # create PostgreSQL CREATE queries from SQL CREATE queries
    df_tables['sql'] = df_tables['sql'].apply(fix_create_query)

    # sorting for table creation, to ensure tables with references
    # are created after the tables they reference
    #
    # create lists of tables referenced in sql queries
    df_tables['references'] = df_tables['sql'].str.findall(
        ' REFERENCES "?([^\s"]+)"?'
    )
    # create column to sort on
    df_tables['max_ref_index'] = df_tables['references'].apply(
        get_max_referenced_index,
        names=df_tables['name']
    )
    df_tables = df_tables.sort_values(by='max_ref_index')

    # create tables
    print('Creating tables')
    for query in df_tables['sql']:
        cursor.execute(query)

    # insert data into tables
    for table in df_tables['name']:
        print(f'Copying table data: {table}')
        df = pd.read_sql_query(f'SELECT * FROM {table};', conn_sql)
        filename = os.path.join(os.path.dirname(__file__), f'{table}.csv')
        df.to_csv(filename, index=False, header=False, quotechar="'", sep='\t')
        with open(filename, 'r') as f:
            cursor.copy_from(f, f'"{table}"')
        os.remove(filename)

    conn_pgs.commit()        

finally:
    conn_sql.close()
    conn_pgs.close()
