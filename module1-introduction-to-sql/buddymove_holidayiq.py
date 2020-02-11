import pandas as pd 
import sqlite3
import os 

os.getcwd()
os.listdir(os.getcwd())

# Load the file
df = pd.read_csv('buddymove_holidayiq.csv', index_col= 'User Id')

# Create a blank sqlite file
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Convert file to sql one
df.to_sql('review', con=conn, if_exists='replace')

curs = conn.cursor()

# Count total rows
query = """
           SELECT COUNT(*)
           FROM review
        """

total_rows = curs.execute(query).fetchall()[0][0]
print(f'Total rows: {total_rows}')

# Count total users who reviewed both 100 nature 
# And 100 Shopping categories
query = """
           SELECT COUNT(*)
           FROM review
           WHERE Nature >=100 AND Shopping >=100
        """
Users = curs.execute(query).fetchall()[0][0]
print(f'User numbers: {Users}')