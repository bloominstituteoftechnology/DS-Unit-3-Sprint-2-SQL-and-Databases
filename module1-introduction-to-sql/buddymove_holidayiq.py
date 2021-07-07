"""Code for buddymove_holidayiq queries"""

import sqlite3
import pandas as pd

df = pd.read_csv('C:/Users/Phatdeluxe/lamdata/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

df.shape

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

curs = conn.cursor()

df.to_sql('review', con=conn)

num_rows = 'SELECT COUNT(*) FROM review;'

curs.execute(num_rows)

results = curs.fetchall()
print(results)