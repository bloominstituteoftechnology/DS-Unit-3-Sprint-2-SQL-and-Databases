import pandas as pd
import sqlite3
from sqlalchemy import create_engine

r_columns = ['User_Id', 'Sports', 'Religious', 'Nature', 'Theatre', 'Shopping',
       'Picnic']

df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv', names=r_columns, header=0)
df.rename

print(df)

print(df.columns)

engine = create_engine('sqlite://', echo=False)

df.to_sql('review', con=engine)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
c = conn.cursor()
conn.commit()

df.to_sql('review', conn, if_exists='replace', index='false')

# queries
query_1 = 'SELECT * FROM review'
results_1 = c.execute(query_1).fetchone()
print('RESULTS_1', results_1)

query_2 = """SELECT count('User Id')
FROM review
WHERE Nature > 100 AND Shopping > 100"""
results_2 = c.execute(query_2).fetchone()
print('RESULTS_2', results_2)