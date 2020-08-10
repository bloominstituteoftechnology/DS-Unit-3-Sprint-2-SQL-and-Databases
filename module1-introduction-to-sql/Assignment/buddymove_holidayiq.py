import pandas as pd
import sqlite3
df = pd.read_csv("Assignment/buddymove_holidayiq.csv")
df.columns = ['user_id', 'sports', 'religious', 'nature', 'theatre', 'shopping', 'picnic']
"""
connecting to the database
"""
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
"""
cursor
"""
cursor = connection.cursor()
"""
insert data into new table
"""
df.to_sql('review', connection, index=False)
cursor.execute('SELECT * FROM review').fetchall()
print(df.shape)
print(df.head)
"""
Count how many rows you have
"""
query = "SELECT COUNT(*) FROM review"
print(cursor.execute(query).fetchall()[0][0])
"""
How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
"""
query2 = "SELECT COUNT(*) FROM review WHERE (Nature) >= 100 AND (Shopping) >= 100"
print(cursor.execute(query2).fetchall()[0][0])
