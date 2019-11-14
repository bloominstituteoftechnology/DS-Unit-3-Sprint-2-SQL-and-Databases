import sqlite3
import pandas as pd

# load in and check data
buddymoveDF = pd.read_csv('buddymove_holidayiq.csv')
print(buddymoveDF.shape)
print(buddymoveDF.isna().sum())
print(buddymoveDF.head())

# instantiate empty database, open connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# load DF into database
buddymoveDF.to_sql('review', conn)

# instantiate cursor
cur = conn.cursor()

# count rows
cur.execute("""SELECT COUNT(*) FROM review;""")
print(cur.fetchall())

# count users with nature > 100 and shopping > 100
cur.execute("""
SELECT COUNT('User Id') FROM review
WHERE Nature >=100 AND Shopping >= 100
""")
print(cur.fetchall())

# count averages per category
cur.execute("""
SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review
""")
print(cur.fetchall())