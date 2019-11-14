import sqlite3
import pandas as pd
import numpy as np

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
print(df.head())  # make sure data is correctly loaded
print(df.shape)  # make sure there are 249 rows and 7 columns
print(df.isnull().sum())  # make sure there are no null values

# connect to sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite')

# create a cursor
cur = conn.cursor()

# create a new table 'review' using df
df.to_sql('review', conn)

# query to count how many rows
query = """
    SELECT COUNT(*)
    FROM review;
"""
cur.execute(query)
cur.fetchall()

# query how many users reviewed at least 100 nature and shopping
query = """
    SELECT COUNT(*)
    FROM review
    WHERE Nature >= 100
    AND Shopping >= 100;
"""
cur.execute(query)
cur.fetchall()

# query avg number of reviews for each category
query = """
    SELECT AVG(Sports), 
           AVG(Religious), 
           AVG(Nature), 
           AVG(Theatre), 
           AVG(Shopping), 
           AVG(Picnic)
    FROM review;
"""
cur.execute(query)
cur.fetchall()

# take results of last query and make new df
df2 = pd.read_sql_query(query, conn)
print(df2)
