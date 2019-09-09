import pandas as pd
import helper
import sqlite3

'''
Load the data (use pandas) from the provided file buddymove_holidayiq.csv (the BuddyMove Data Set) - you should have 249 rows, 7 columns, and no missing values. The data reflects the number of place reviews by given users across a variety of categories (sports, parks, malls, etc.).

Using the standard sqlite3 module:

    Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
    Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
'''
print('-'*80)
print('Q1: Create database file and Insert review table into it...')
# Create database file if it doesn't exist
with sqlite3.connect('buddymove_holidayiq.sqlite3') as conn:

    # 1. Read csv file
    df = pd.read_csv('buddymove_holidayiq.csv')

    # 2. DROP TABLE review IF EXISTS
    drop_query = 'DROP TABLE IF EXISTS review'
    conn.cursor().execute(drop_query)

    # 3. INSERT TABLE review
    df.to_sql('review', conn, index=False)
    query = 'SELECT * FROM review'
    df = pd.read_sql(query, conn)

print(df.head())
print('-'*80)


print('Q2: Count how many rows you have - it should be 249!')
'''
Count how many rows you have - it should be 249!
'''
query = 'SELECT COUNT(*) FROM review;'
result = helper.select_all_query('buddymove_holidayiq.sqlite3', query)[0][0]
print(result)

print('-'*80)
print('How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
query = '''SELECT *
FROM review
WHERE `Nature` >= 100 AND `Shopping` >= 100
'''
conn = helper.create_connection('buddymove_holidayiq.sqlite3')
df = pd.read_sql(query, conn)
print(df.head())

print('-'*80)
print('(Stretch) What are the average number of reviews for each category?')
query = '''SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM review
'''
conn = helper.create_connection('buddymove_holidayiq.sqlite3')
df = pd.read_sql(query, conn)
print(df)
