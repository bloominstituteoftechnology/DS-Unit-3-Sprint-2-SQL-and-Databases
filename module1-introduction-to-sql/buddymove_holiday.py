import sqlite3
import os
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

df.columns = ['UserId', 'Sports', 'Religious',
'Nature', 'Theatre', 'Shopping', 'Picnic']

df.set_index('UserId')

conn = sqlite3.connect('buddymove_holiday.sqlite3')

curs = conn.cursor()

if not os.path.isfile('buddymove_holiday.sqlite3'):
    df.to_sql('review', conn)

def qa(query):
    return curs.execute(query).fetchall()

def q1(query):
    return curs.execute(query).fetchone()

# ---------------------------------------
print('1. How many users do you have?')

query = '''
SELECT
    count('User Id') as NumUsers
FROM review
'''

print(q1(query),'\n')

# ----------------------------------------
print('2. How many users reviewed at least 100 in nature and shopping?')

query = '''
SELECT
	count(UserId)
FROM review
WHERE Nature >= 100 and Shopping >= 100
'''

print (q1(query))