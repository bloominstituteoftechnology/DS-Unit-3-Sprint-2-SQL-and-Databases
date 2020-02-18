import sqlite3
import pandas as pd

DB_FILEPATH = "/Users/josephbell/Desktop/sql-practice/buddymove_holidayiq.csv"

df = pd.read_csv(DB_FILEPATH)
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql("buddymove_holidayiq", connection)
cursor = connection.cursor()
query = "SELECT * FROM buddymove_holidayiq"
result = cursor.execute(query).fetchall()
print(len(result), 'rows')
query = "SELECT * FROM buddymove_holidayiq WHERE Nature > 100 and Shopping > 100;"
result2 = cursor.execute(query).fetchall()
print(len(result2), "users reviewed both 100 Nature and 100 Shopping categories.")
query = """
SELECT
   avg(Sports)
  ,avg(Religious)
  ,avg(Nature)
  ,avg(Theatre)
  ,avg(Shopping)
  ,avg(Picnic) 
FROM buddymove_holidayiq
"""
result3 = cursor.execute(query).fetchall()
print('Avg Sports Reviews:', round(result3[0][0], 2))
print('Avg Religious Reviews:', round(result3[0][1], 2))
print('Avg Nature Reviews:', round(result3[0][2], 2))
print('Avg Theatre Reviews:', round(result3[0][3], 2))
print('Avg Shopping Reviews:', round(result3[0][4], 2))
print('Avg Picnic Reviews:', round(result3[0][5], 2))
