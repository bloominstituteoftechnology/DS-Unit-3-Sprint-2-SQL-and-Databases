# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3


'''#load csv file to create db with'''

df = pd.read_csv('https://raw.githubusercontent.com/iesous-kurios/'
                    'DS-Unit-3-Sprint-2-SQL-and-Databases/master/'
                    'module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape)
df.head()

df.isnull().sum()

"""#establish connection to new empty db to fill with csv file
"""

# Establish a connection to a new database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

#Inserted the data into a new table called "test" in the database
df.to_sql(name = 'test', con = conn)

"""### Counting how many rows"""

# Create a cursor.
curs1 = conn.cursor()

# Write a query
query1 = 'SELECT COUNT(*) FROM test;'

# Execute the query
total_rows = curs1.execute(query1).fetchall()

# Print Answer
print(total_rows)

"""### How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?"""
print('How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')

#Create a cursor.
curs2 = conn.cursor()

#Write a query.
query2 = """
SELECT COUNT(*)
FROM test
WHERE Nature >= 100 AND Shopping >= 100;
"""

#Execute the query.
users = curs2.execute(query2).fetchall()

print(users)

"""### (Stretch) What are the average number of reviews for each category?"""

#Create a cursor.
curs3 = conn.cursor()

#Write a query.
query3 = """
SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre),
AVG(Shopping), AVG(Picnic)
FROM test;"""

#Execute the query()
avg_reviews_column = curs3.execute(query3).fetchall()

print(avg_reviews_column)