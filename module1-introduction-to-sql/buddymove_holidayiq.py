import pandas as pd
import sqlite3
import os

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.head())
print(df.shape)
print(df.isnull().sum())

filepath = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(filepath)

df.to_sql("review", connection)
cursor = connection.cursor()
# queries

query = "SELECT * from review"
chars = cursor.execute(query).fetchall()
q1 = len(chars)

print(' # How many rows in the table?')
print(f'  {q1} rows in the table.')
