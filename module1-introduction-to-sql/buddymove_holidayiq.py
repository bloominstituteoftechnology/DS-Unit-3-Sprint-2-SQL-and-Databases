import os
import sqlite3
import pandas as pd


df = pd.read_csv('buddymove_holidayiq.csv')
assert df.shape() = (249, 7)

CONN = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con=CONN)

cursor = CONN.cursor()

query1 = 'SELECT COUNT() FROM review;'
count1 = cursor.execute(query1).fetchall()
print(count1)

query2 = '''SELECT COUNT(User Id) FROM review 
            WHERE review.Nature >= 100 AND review.Shopping >= 100;'''
count2 = cursor.execute(query2).fetchall()
print(count2)