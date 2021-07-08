import sqlite3
import pandas as pd

# Silence Pandas depreciation warnings re. spaces in column names
import warnings
warnings.filterwarnings('ignore')

# Import Data as DF
df = pd.read_csv('buddymove_holidayiq.csv')

# Convert to SQLite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql(name='review', con=conn, if_exists='replace')
curs = conn.cursor()

# Query 1 
query = """SELECT COUNT(*) FROM review"""
result = curs.execute(query)
print('Number of Rows:')
print(result.fetchall()[0][0])

# Query 2 
query = """SELECT COUNT(*)
           FROM review
           WHERE Nature >= 100 AND Shopping >= 100"""
result = curs.execute(query)
print('Number of Users Who have reviewed at least 100 nature and at least 100 shopping items:')
print(result.fetchall()[0][0])

# Query 3
query = """SELECT AVG(sports),  AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
            FROM review"""
result = pd.read_sql_query(query, conn)
print(result)