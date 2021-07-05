import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

connection = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con=connection, if_exists='replace')

c = connection.cursor()

c.execute('SELECT COUNT(*) FROM review;')
print('Number of Rows: ', c.fetchone()[0])

c.execute('SELECT COUNT(*) FROM review '
          'WHERE Nature >= 100 '
          'AND Shopping >= 100;')
print('Users who Reviewed Greater than 100 in both '
      'Nature and Shopping', c.fetchone()[0])