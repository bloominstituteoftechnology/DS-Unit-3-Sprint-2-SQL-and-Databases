import sqlite3
import pandas as pd
from sqlalchemy import create_engine

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cur = conn.cursor()

df = pd.read_csv('https://raw.githubusercontent.com/lechemrc/DS-Unit-3-Sprint-2\
-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
df = df.rename(columns={'User Id':'User_id'})
df.head()

df.to_sql('buddymove_holidayiq', con=conn)

cur.execute('''
    SELECT * FROM buddymove_holidayiq
''')
cur.fetchall()

cur.execute('''
    SELECT COUNT(*)
    FROM buddymove_holidayiq
    WHERE Nature >= 100
    AND Shopping >= 100
''')
cur.fetchall()

cur.execute('''
    SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(), AVG(), AVG()
    FROM buddymove_holidayiq
''')
cur.fetchall()