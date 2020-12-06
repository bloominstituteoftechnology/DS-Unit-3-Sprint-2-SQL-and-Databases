import os
import sqlite3
import pandas as pd

# Load the data (use `pandas`) from the provided file `buddymove_holidayiq.csv`

df = pd.read_csv('https://raw.githubusercontent.com/KristineYW/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

print(df.head())
print(df.shape)
print(df.isnull().sum())

# Open a connection to a new (blank) database file `buddymove_holidayiq.sqlite3`

filepath = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(filepath)

# Use `df.to_sql` to insert the data into a new table `review` in the SQLite3 database

df.to_sql("review", connection)

# Count how many rows you have - it should be 249!

query = "SELECT COUNT (*) FROM review;"
cursor = connection.cursor()

result1 = cursor.execute(query).fetchall()
print("NUMBER OF REVIEWERS:", result1)


#   How many users who reviewed at least 100 `Nature` in the category also
#   reviewed at least 100 in the `Shopping` category?

query2 = "SELECT COUNT(*) FROM review WHERE Nature > 100 AND Shopping > 100"
result2 = cursor.execute(query2).fetchall()
print("NUMBER OF REVIEWERS WHO REVIEWED OVER 100 NATURE AND OVER 100 SHOPPING CATEGORIES:",result2)


