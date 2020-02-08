import sqlite3
import pandas as pd

# Read csv
df = pd.read_csv('buddymove_holidayiq.csv')

# Connect to database file
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
# df.to_sql('review', conn)
curs = conn.cursor()

# Count rows
query = 'SELECT COUNT(*) FROM review;'
num_rows = curs.execute(query).fetchall()
print("Total number of rows:", num_rows[0][0])

# How many users have > 100 Nature and > 100 Shopping?
query = 'SELECT COUNT(*) FROM review WHERE Shopping > 99 AND Nature > 99'
num_users = curs.execute(query).fetchall()
print("Users with >= 100 Nature and >= 100 Shopping:", num_users[0][0])