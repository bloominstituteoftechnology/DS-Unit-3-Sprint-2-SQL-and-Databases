import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)
print(df.isnull().sum())

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
#df.to_sql('review', conn)

#Count how many rows you have - it should be 249!
curs.execute("""
    SELECT COUNT('User ID')
    FROM review;
    """)
answer = curs.fetchall()[0][0]
print('There are', answer, 'rows')

#How many users who reviewed at least 100 Nature in the category 
#also reviewed at least 100 in the Shopping category?
curs.execute("""
    SELECT COUNT('User Id')
    FROM review
    WHERE Nature >= 100
    AND Shopping >= 100;
    """)
answer = curs.fetchall()[0][0]
print(answer, 'Users have reviewed at least 100 for Nature and Shopping')

#Commit and close
curs.close()
conn.commit()