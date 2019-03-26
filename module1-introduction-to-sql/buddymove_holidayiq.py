import pandas as pd
import sqlite3

# Load data using pandas
df = pd.read_csv('buddymove_holidayiq.csv')

# Open a connection to the blank db file
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Insert data into a new table 'review' in sqlite3 db
# df.to_sql('review', conn)

# Count the number of rows
q = 'SELECT count(*) FROM review'
print('Number of rows:', conn.execute(q).fetchall())

# How many users who reviewed at least 100 Nature also reviewed
# at least 100 in the Shopping category?
q = "SELECT 'User Id' FROM review WHERE nature >= 100 and shopping >= 100"
print('Number of users who reviewed at least 100 in both Nature and Shopping:',
      len(curs.execute(q).fetchall()))

# What is the average number of reviews for each category?
sports = 'SELECT AVG(Sports) FROM review'
religious = 'SELECT AVG(religious) FROM review'
nature = 'SELECT AVG(nature) FROM review'
theatre = 'SELECT AVG(theatre) FROM review'
shopping = 'SELECT AVG(shopping) FROM review'
picnic = 'SELECT AVG(picnic) FROM review'
q = [sports, religious, nature, theatre, shopping, picnic]
n  = [i + ' avg:' for i in ['sports', 'religious', 'nature', 'theatre', 'shopping', 'picnic']]
for i, k in zip(n, q):
    print(i, curs.execute(k).fetchall())
