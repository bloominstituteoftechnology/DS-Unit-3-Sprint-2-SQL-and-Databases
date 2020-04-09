#app/buddymove_holidyiq.py

import pandas as pd
import sqlite3
import os

HTML = "https://raw.githubusercontent.com/mahoryu/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..","data","buddymove_holidayiq.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

df = pd.read_csv(HTML)

df.to_sql("buddymove_holidayiq", con=conn, if_exists='replace')

# Number of Rows
query1 = """
SELECT
	count(distinct "User Id") as Rows 
FROM buddymove_holidayiq
"""
r = curs.execute(query1).fetchone()
print ("Total Number of Rows:")
print(r[0])


# How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?
query2 = """
SELECT
	count(distinct "User Id") as Rows 
FROM buddymove_holidayiq
WHERE Nature >= 100 AND Shopping >= 100
"""
r = curs.execute(query2).fetchone()
print ("Number of Nature/Shopping Lovers:")
print(r[0])


# What are the average number of reviews for each category?
query2 = """
SELECT
	AVG(Sports) as "Sports Average"
	, AVG(Religious) as "Religious Average"
	, AVG(Nature) as "Nature Average"
	, AVG(Theatre) as "Theatre Average"
	, AVG(Shopping) as "Shopping Average"
	, AVG(Picnic) as "Picnic Average"
FROM buddymove_holidayiq
"""
r = curs.execute(query2).fetchall()
print ("Averages:")
categories = ['Sports','Religious','Nature','Theatre','Shopping','Picnic']
for i in range(6):
    print(categories[i], ":", r[0][i])