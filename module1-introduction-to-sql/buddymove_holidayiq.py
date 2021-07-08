import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn, if_exists='replace')

curs = conn.cursor()

query = 'SELECT COUNT(*) FROM review'
rows = curs.execute(query).fetchall()[0][0]
print (f'Number of rows in table is {rows}')

#print (df.head())

query2 = '''SELECT COUNT('User Id') FROM review 
            WHERE Nature == 100 AND Shopping == 100;'''

print (f'Number of Users who reviewed at least 100 for Nature and Shopping is {curs.execute(query2).fetchall()[0][0]}')


