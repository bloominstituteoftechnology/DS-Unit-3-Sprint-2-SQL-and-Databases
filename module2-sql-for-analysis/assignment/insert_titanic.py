"""Creates and populates PostgreSql table 'titanic'

Reads data from '../titanic.csv', relative to this file.
"""

import os

import pandas as pd
import psycopg2

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

CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'titanic.csv')
assert os.path.exists(CSV_FILE), '../titanic.csv NOT FOUND'

INSERT = 'INSERT INTO titanic (survived, pclass, name, sex, age, '
INSERT += 'sib_spouse_count, parent_child_count, fare) VALUES '
VALUES = "({0}, {1}, '{2}', '{3}', {4}, {5}, {6}, {7})"

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST
)

try:
    curs = conn.cursor()

    # create the table
    query = """
    DROP TABLE IF EXISTS titanic;
    CREATE TABLE titanic (
        id SERIAL PRIMARY KEY,
        survived bool,
        pclass int,
        name text,
        sex text,
        age float8,
        sib_spouse_count int,
        parent_child_count int,
        fare float8
    );
    """
    curs.execute(query)

    # get and clean data
    df = pd.read_csv(CSV_FILE)
    df['Survived'] = df['Survived'].astype(bool)
    df['Name'] = df['Name'].str.replace("'", "''")

    # create insert query
    values = []
    for row in df.itertuples(False, None):
        v = VALUES.format(row[0], row[1], row[2], row[3],
                          row[4], row[5], row[6], row[7])
        values.append(v)
    query = INSERT + ','.join(values) + ';'

    # execute query and commit
    curs.execute(query)
    conn.commit()
finally:
    conn.close()
