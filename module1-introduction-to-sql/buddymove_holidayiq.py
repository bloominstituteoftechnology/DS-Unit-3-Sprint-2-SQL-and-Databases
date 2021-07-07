import pandas as pd
import sqlite3


buddymove_csv = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
buddymove_csv.to_sql('buddymove', con=conn, if_exists='replace')
curs = conn.cursor()

query = 'SELECT COUNT(*) FROM buddymove;'
result = curs.execute(query).fetchone()
print('\n\nNumber of Entries:', result[0])

query = 'SELECT COUNT(*) FROM buddymove \
         WHERE ((Nature >= 100) AND (Shopping >= 100));'
result = curs.execute(query).fetchone()
print('\nHow many users who reviewed at least 100 in Nature and',
      'Shopping categories?', result[0])
