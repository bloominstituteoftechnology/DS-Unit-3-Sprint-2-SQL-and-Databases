import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('review', con=conn, if_exists='replace')

curs = conn.cursor()
query = '''SELECT count(*)
           FROM review;'''
total_rows = curs.execute(query).fetchall()[0][0]

query = '''SELECT count(*)
           FROM review
           WHERE Nature > 100
           AND Shopping > 100'''
reviewed_at_least_100_nature_shopping = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Sports)
           FROM review'''
sports_average = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Religious)
           FROM review'''
religious_average = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Nature)
           FROM review'''
nature_average = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Theatre)
           FROM review'''
theatre_average = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Shopping)
           FROM review'''
shopping_average = curs.execute(query).fetchall()[0][0]

query = '''SELECT avg(Picnic)
           FROM review'''
picnic_average = curs.execute(query).fetchall()[0][0]

print('Total number of rows:', total_rows,
      '\nNumber of users who reviewed at least 100 in nature & in shopping:',
      reviewed_at_least_100_nature_shopping,
      '\nAverage number of sports Reviews:', sports_average,
      '\nAverage number of religious Reviews:', religious_average,
      '\nAverage number of nature Reviews:', nature_average,
      '\nAverage number of theatre Reviews:', theatre_average,
      '\nAverage number of shopping Reviews:', shopping_average,
      '\nAverage number of picnic Reviews:', picnic_average)