import os
import sqlite3
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KristineYW/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

print(df.head())
print(df.shape)
print(df.isnull().sum())

filepath = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(filepath)

df.to_sql("review",connection)
