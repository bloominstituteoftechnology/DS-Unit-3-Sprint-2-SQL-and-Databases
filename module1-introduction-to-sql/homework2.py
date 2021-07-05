import pandas as pd
import sqlite3

# DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

# Create a new Database
conn = sqlite3.connect('buddymove_holiday.sqlite3')

# Use df as sql
df.to_sql('df', conn, if_exists="replace")


"""
Count how many rows
"""


print(pd.read_sql_query('SELECT COUNT(*) FROM df;', conn))


"""
How many users who reviewed at least 100 Nature in the category also reviewed
at least 100 in the Shopping category?
"""

print(pd.read_sql_query('SELECT COUNT(*) FROM df WHERE Nature>=100 AND Shopping >=100;', conn))


"""
What are the average number of reviews for each category?
"""

print(pd.read_sql_query('SELECT AVG(Sports) FROM df;', conn))
print(pd.read_sql_query('SELECT AVG(Religious) FROM df;', conn))
print(pd.read_sql_query('SELECT AVG(Nature) FROM df;', conn))
print(pd.read_sql_query('SELECT AVG(Theatre) FROM df;', conn))
print(pd.read_sql_query('SELECT AVG(Shopping) FROM df;', conn))
print(pd.read_sql_query('SELECT AVG(Picnic) FROM df;', conn))
