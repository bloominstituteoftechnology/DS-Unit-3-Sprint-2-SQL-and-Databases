import sqlite3
import pandas as pd

connect = sqlite3.connect('buddymove_holidayiq.sqlite3')
cursor = connect.cursor()

df = pd.read_csv('buddymove_holidayiq.csv')

df.to_sql('buddy', connect)

cursor.execute('SELECT COUNT(*) FROM buddy')
print('1. ', cursor.fetchall())

cursor.execute('SELECT COUNT(*) FROM buddy WHERE Nature > 99 AND Shopping > 99')
print('2. ', cursor.fetchall())
