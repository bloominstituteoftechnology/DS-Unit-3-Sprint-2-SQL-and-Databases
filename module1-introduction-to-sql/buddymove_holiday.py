import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

delete_review = 'DROP TABLE IF EXISTS review'
curs.execute(delete_review)

df.to_sql('review', conn, index = False) #Insert new table called # REVIEW
curs.execute('SELECT * FROM review').fetchall()

print('Size of the table', df.shape)

q1 = 'SELECT COUNT(*) FROM review;'

print('From the Query:how many rows ?',
       curs.execute(q1).fetchall()[0][0])

q2 = 'SELECT COUNT(*) FROM review WHERE "Nature" >= 100 AND "Shopping" >= 100'

print('How many users who reviewed at least 100 ?', curs.execute(q2).fetchall()[0][0])

q3 = 'SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)\
      FROM review'

print('What are the average number of reviews for each category?\
        Sports, Religious , Nature, Theatre, Shopping,Picnic',
        curs.execute(q3).fetchall())

curs.close()
conn.commit()