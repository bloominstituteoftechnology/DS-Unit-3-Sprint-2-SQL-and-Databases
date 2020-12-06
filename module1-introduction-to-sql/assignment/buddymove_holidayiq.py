import pandas as pd
import os
import sqlite3


CSV_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'buddymove_holidayiq.csv')
DB_FILEPATH = DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'buddymove_holidayiq.sqlite3')


df = pd.read_csv(CSV_FILEPATH)
col_list = df.columns.tolist()
for i in range(len(col_list)):
    col_list[i] = col_list[i].lower().replace(' ', '_')
df.columns = col_list

connection = sqlite3.connect(DB_FILEPATH)

df.to_sql('review', con=connection, if_exists='replace')

cursor = connection.cursor()

# number of rows in db
query = 'SELECT count(distinct user_id) FROM review'
result = cursor.execute(query).fetchall()
print(f'\nThe database has {result[0][0]} rows')

# how many users reviewed both nature and shopping at least than 100
query = '''
    SELECT
        count(distinct user_id)
    FROM
        review
    WHERE nature >= 100 and shopping >= 100 
'''
result = cursor.execute(query).fetchall()
print(f'{result[0][0]} users gave both nature and shopping a score of at least 100\n')