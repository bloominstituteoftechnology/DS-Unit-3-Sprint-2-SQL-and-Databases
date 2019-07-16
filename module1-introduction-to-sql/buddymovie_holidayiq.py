import pandas as pd
import sqlite3

conn = sqlite3.connect('database')

# df = pd.read_csv('buddymove_holidayiq.csv')
# df.to_sql('database',
#           conn,
#           if_exists='replace')

curr = conn.cursor()

# How many rows?
query = '''SELECT * FROM database'''
do_it = curr.execute(query)
print(f'Database contains {len(do_it.fetchall())} rows')

# How many users reviewed...
query = '''SELECT "User id" FROM database WHERE Nature > 100 AND Shopping > 100'''
do_it = curr.execute(query)
print(f'{len(do_it.fetchall())} reviewers reviewed Nature and Shopping > 100 times.')
