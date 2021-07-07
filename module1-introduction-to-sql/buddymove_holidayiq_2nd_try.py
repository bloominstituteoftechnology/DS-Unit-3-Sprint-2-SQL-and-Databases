import pandas as pd
import sqlite3 as sq


# The thing that's unique about doing SQL commands on a pandas dataframe is that you have to convert it to sql
# using the .to_sql command as demonstrated below

df = pd.read_csv('buddymove_holidayiq.csv')
# opening a connection to a new (blank) database file below
conn = sq.connect('buddymove_holidayiq.sqlite3')

df.to_sql('review', con=conn)

# The following is to check if a DB has already been created. If it has, then pass
try:
    df.to_sql('review', conn)
except:
    pass

r = conn.cursor()

print('How many rows are there? \n    ', r.execute('SELECT COUNT("User_id") FROM review').fetchall()[0])

print('How many users are super reviewers? \n     ',
r.execute('SELECT COUNT(DISTINCT "User ID") FROM review \
WHERE Nature >= 100 AND Shopping >= 100').fetchall()[0])
