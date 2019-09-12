import pandas as pd
import sqlite3
import os

# make this file's directory the working directory
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

df = pd.read_csv('./buddymove_holidayiq.csv')
assert df.shape == (249, 7)
for total in df.isnull().sum():
    assert total == 0

conn = sqlite3.connect(':memory:')
name = 'review'
df.to_sql(name=name, con=conn, if_exists='replace')

curs = conn.cursor()

# get rows
num_rows_query = "SELECT COUNT(*) FROM review;"
num_rows = curs.execute(num_rows_query).fetchone()[0]
print(f'\nThe review table has {num_rows} rows.')

# get column names
columns_query = """
PRAGMA table_info(review)
"""
columns = curs.execute(columns_query).fetchall()
print('\nColumn names for the review table: ')
for column in columns:
    print(column[1])

# Number of users who have over 100 Nature and 100 Shopping reviews
num_users_query = """
SELECT COUNT(*) FROM review
WHERE Nature >= 100 AND Shopping >= 100
"""

num_users = curs.execute(num_users_query).fetchone()[0]
print(f'\n{num_users} users have submitted at least 100 '
      'nature reviews and 100 shopping reviews\n')

# Average number of users for each category
review_cols = ('Sports', 'Religious', 'Nature',
               'Theatre', 'Shopping', 'Picnic')
avg_num_query = """
SELECT AVG(Sports), AVG(Religious), AVG(Nature),
       AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review
"""

avg_num = curs.execute(avg_num_query).fetchall()[0]
print('Average number of reviews per user for each category:')
for i, column in enumerate(review_cols):
    print(f'{column}:'.ljust(11) + f'{avg_num[i]:.2f}'.rjust(6))
print()

curs.close()
conn.close()
