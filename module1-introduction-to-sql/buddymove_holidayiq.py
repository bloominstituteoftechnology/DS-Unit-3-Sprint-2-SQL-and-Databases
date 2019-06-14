import sqlite3
import pandas as pd

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df = pd.read_csv('buddymove_holidayiq.csv')

df.to_sql('buddy', conn)

curs.execute('SELECT COUNT(*) FROM buddy')
print('1. ', curs.fetchall())

curs.execute('SELECT COUNT(*) FROM buddy WHERE Nature > 99 AND Shopping > 99')
print('2. ', curs.fetchall())