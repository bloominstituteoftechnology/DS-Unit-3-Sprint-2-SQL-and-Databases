import pandas as pd
import sqlite3 as sq

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sq.connect('buddymove_holidayiq.sqlite3')

try:
    df.to_sql('review', conn)
except:
    pass

r = conn.cursor()


print("How many users?\n   ", r.execute('SELECT COUNT("User Id") FROM review').fetchall()[0])
print("How many users who meet the conditions?\n   ",
         r.execute('SELECT COUNT(DISTINCT "User ID") FROM review \
         WHERE Nature >= 100 AND Shopping >= 100').fetchall()[0])
