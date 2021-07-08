import sqlite3
import pandas as pd

# Import data
df = pd.read_csv('buddymove_holidayiq.csv')

# Replace space in column name with underscore
df.columns = df.columns.str.replace(' ', '_')

# Create new database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Export DataFrame to database
df.to_sql('review', con=conn)

# Create a cursor
curs = conn.cursor()

# Run test queries:
# query 1
print('Count how many rows you have - it should be 249!')
query1 = '''SELECT COUNT(*) FROM review;'''
result1 = curs.execute(query1)
print(result1.fetchall())

# query 2
print('How many users who reviewed at least 100 Nature in the category also reviewed'
      ' at least 100 in the Shopping category?')
query2 = '''SELECT COUNT()
            FROM review
            WHERE Nature >= 100 AND Shopping >= 100;'''
result2 = curs.execute(query2)
print(result2.fetchall())
