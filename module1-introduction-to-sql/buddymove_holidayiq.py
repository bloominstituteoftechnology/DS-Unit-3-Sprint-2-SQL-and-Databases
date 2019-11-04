import pandas as pd
import sqlite3

# load data from file
df = pd.read_csv('buddymove_holidayiq.csv')

# connect to database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# insert df as new table "review"
df.to_sql(name="review", con=conn, if_exists='replace')

curs = conn.cursor()

# Count how many rows you have - it should be 249!
q1 = "SELECT COUNT(*) FROM review;"

# How many users who reviewed at least 100 `Nature` in the category
# also reviewed at least 100 in the `Shopping` category?
q2 = "SELECT COUNT(*) FROM review WHERE Nature > 100 AND Shopping > 100;"

# What are the average number of reviews for each category?
q3_sport = "SELECT AVG(Sports) FROM review;"
q3_rel = "SELECT AVG(Religious) FROM review;"
q3_nat = "SELECT AVG(Nature) FROM review;"
q3_theat = "SELECT AVG(Theatre) FROM review;"
q3_shop = "SELECT AVG(Shopping) FROM review;"
q3_pic = "SELECT AVG(Picnic) FROM review;"

print("Number of rows:", curs.execute(q1).fetchall()[0][0])
print("Number of users with >100 Nature and Shopping:",
      curs.execute(q2).fetchall()[0][0])
print("Average sports reviews:", curs.execute(q3_sport).fetchall()[0][0])
print("Average religious reviews:", curs.execute(q3_rel).fetchall()[0][0])
print("Average nature reviews:", curs.execute(q3_nat).fetchall()[0][0])
print("Average theater reviews:", curs.execute(q3_theat).fetchall()[0][0])
print("Average shopping reviews:", curs.execute(q3_shop).fetchall()[0][0])
print("Average picnic reviews:", curs.execute(q3_pic).fetchall()[0][0])
