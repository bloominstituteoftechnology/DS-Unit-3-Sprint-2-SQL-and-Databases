import os
import sqlite3
import pandas as pd 

"""Creating an SQLite database with queries."""

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.head)

"""Checking for null values."""
nulls = df.isnull().sum().sum()
print("There are", nulls, "null values.")

CONN = sqlite3.connect('buddymove_holidayiq.db')

cursor = CONN.cursor()

delete_table = "DROP TABLE IF EXISTS buddy"
cursor.execute(delete_table)

df.to_sql('buddy', con = CONN, index=True)

query = 'SELECT COUNT(Sports) FROM buddy;'
rows = cursor.execute(query).fetchall()
print ("There are" , rows, "rows.")

query2 ='SELECT COUNT(User) FROM buddy WHERE Nature > 100 AND Shopping > 100;'
user_count = cursor.execute(query2).fetchall()
print("There are", user_count, "users who have reviewed at least 100 in the nature and shopping categories")

cat_list = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

def mean_review(cat_list):
    score_list = []
    for i in cat_list:
        query = 'SELECT AVG (' + (i) + ') FROM buddy'
        score = cursor.execute(query).fetchall()
        score = str(score).strip('()[],')
        print("The average for", i, "is" , score)
        score_list.append(score)
    return score_list
  
    
mean_review(cat_list)   