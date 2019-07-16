import pandas as pd
import sqlite3

# print(df.info)
conn = sqlite3.connect('database')
df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('database',
          conn,
          if_exists='replace')

curr = conn.cursor()

# How many rows?
query = '''SELECT * FROM database'''
do_it = curr.execute(query)
print(len(do_it.fetchall()))

# How many users reviewed...
query = '''SELECT "User id" FROM database WHERE Nature > 100 AND Shopping > 100'''
do_it = curr.execute(query)
print(do_it.fetchall())
