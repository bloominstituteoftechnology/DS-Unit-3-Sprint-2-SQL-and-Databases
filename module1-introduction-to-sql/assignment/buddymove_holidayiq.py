import sqlite3
import pandas as pd

!wget https://raw.githubusercontent.com/jonathanmendoza-tx/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cur = conn.cursor()

df = pd.read_csv('/content/buddymove_holidayiq.csv', index_col= 'User Id')

df.to_sql(name = 'review', con = conn)

query_rows = """
SELECT COUNT(*)
FROM review
"""

cur.execute(query_rows)
total_people = cur.fetchall()
print(f'There are a total of {total_people[0][0]} rows')

query_nature_shopping = """
SELECT COUNT(*)
FROM review
WHERE Nature >= 100 AND Shopping >= 100
"""

cur.execute(query_nature_shopping)
nature_shop = cur.fetchall()

print(f'There are {nature_shop[0][0]} people who reviewed nature and shopping at least 100 times')

columns = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
for ii in range(len(columns)):
  query = """
  SELECT AVG(%s)
  FROM review 
  """

  cur.execute(query %columns[ii])
  avg = cur.fetchall()

  print(f'Average number of reviews for {columns[ii]} is {avg[0][0]}')