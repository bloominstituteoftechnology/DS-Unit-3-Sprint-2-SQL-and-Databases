"""Module 1 Assignment

Uses pandas to convert a csv file to a sqlite database.
Queries that database using SQL.
"""

import os
import sqlite3

import pandas as pd

CSV_FILE = os.path.join(os.path.dirname(__file__), '..',
                        'buddymove_holidayiq.csv')
DB_FILE = 'buddymove_holidayiq.sqlite3'

df = pd.read_csv(CSV_FILE)
# verify expected dataframe
# print('shape:', df.shape)
assert df.shape == (249, 7), 'Unexpected dataframe shape.'
# print('any nulls:', df.isnull().any().any())
assert df.isnull().any().any() == False, 'Unexpected nulls in dataframe.'
# replace spaces in column names with underscores
df.columns = df.columns.str.replace(' ', '_')

conn = sqlite3.connect(DB_FILE)
df.to_sql('review', conn, if_exists='replace', index=False)
conn.row_factory = sqlite3.Row
curs = conn.cursor()

# Count how many rows you have - it should be 249!
query = """
SELECT COUNT(*) AS count FROM review;
"""
result = curs.execute(query).fetchall()
print('Number of rows:', result[0]['count'])

# How many users who reviewed at least 100 Nature in the category also
# reviewed at least 100 in the Shopping category?
query = """
SELECT
    COUNT(*) as count
FROM review
WHERE Nature > 99 AND Shopping > 99;
"""
result = curs.execute(query).fetchall()
print('Number of users >= 100 in Nature and Shopping:', result[0]['count'])

# (Stretch) What are the average number of reviews for each category?
query = """
SELECT
    AVG(Sports) AS avg_sports
    ,AVG(Religious) AS avg_religious
    ,AVG(Nature) AS avg_nature
    ,AVG(Theatre) AS avg_theatre
    ,AVG(Shopping) AS avg_shopping
    ,AVG(Picnic) AS avg_picnic
FROM review;
"""
result = curs.execute(query).fetchall()
print('Average number of reviews for each category:')
for key in result[0].keys():
    print(f'{key}: {result[0][key]}')

conn.close()