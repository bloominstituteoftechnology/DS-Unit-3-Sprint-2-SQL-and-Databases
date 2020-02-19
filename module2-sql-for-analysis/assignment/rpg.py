"""Creates and populates PostgreSql tables from rpg_db.sqlite3

Reads data from '../../module1-introduction-to-sql/rpg_db.sqlite3',
relative to this file.
"""

import os

import pandas as pd
import psycopg2
import sqlite3

from dotenv import load_dotenv

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

INSERT = 'INSERT INTO titanic (survived, pclass, name, sex, age, '
INSERT += 'sib_spouse_count, parent_child_count, fare) VALUES '
VALUES = "({0}, {1}, '{2}', '{3}', {4}, {5}, {6}, {7})"


def fix_create_query(query):
    """Make a PostgreSql CREATE query from a SQLite CREATE query."""
    query = query.replace(
        'integer NOT NULL PRIMARY KEY AUTOINCREMENT',
        'SERIAL NOT NULL PRIMARY KEY')
    query = query.replace(' datetime ', ' text ')
    query = query.replace('(name,seq)', '(name text, seq int)')
    query = query.replace(' unsigned ', ' ')
    return query


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
    create_queries = [fix_create_query(sql) for sql in df_tables['sql']]
    no_refs = []
    has_refs = []
    for query in create_queries:
        if 'REFERENCES' in query:
            has_refs.append(query)
        else:
            no_refs.append(query)
    print('Dropping any tables that are present')
    cursor.execute(drop_tables)
    print('Creating tables')
    cursor.execute(';'.join(no_refs + has_refs[::-1]))

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
