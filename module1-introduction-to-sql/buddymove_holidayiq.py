import pandas as pd
import sqlite3

''' converts dataframe buddymove to sqlite3 database
    and answers some basic query questions '''

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
df.to_sql('buddymove_holidayiq', conn, index=True)
conn.commit()

'''does the number of rows in sqlite3 match dataframe?'''
rowquery = 'SELECT COUNT(*) from buddymove_holidayiq'
curs.execute(rowquery).fetchall()

''' How many users have made at least 100 reviews in Nature AND
    at least 100 reviews in Shopping?'''
 query = 'SELECT COUNT(*) FROM buddymove_holidayiq
             WHERE Nature >= 100 AND Shopping >= 100;'
 curs.execute(query).fetchall()
 
