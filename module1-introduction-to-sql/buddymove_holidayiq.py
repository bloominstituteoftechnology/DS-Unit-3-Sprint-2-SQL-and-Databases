# buddymove_holidayiq.py


import pandas as pd
import sqlite3
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)


# df - pd.read_csv("buddymove_holidayiq.csv")
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')


# print(df)
# 249 rows, 7 columns, and no missing values


# Use df.to_sql to insert the data into a new table review in the SQLite3 database
df.to_sql(name='review', con=engine)

# Count how many rows you have - it should be 249!
rows = engine.execute("SELECT COUNT (*) FROM review").fetchall()[0][0]
print("review has " + str(rows), "rows")

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
nature = engine.execute("SELECT COUNT (*) FROM review WHERE Nature > 99 AND Shopping > 99").fetchall()[0][0]
print(str(nature), "users reviewed at least 100 for Nature and Shopping")
