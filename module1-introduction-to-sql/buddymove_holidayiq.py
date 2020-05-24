import pandas as pd
import sqlite3

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

df = pd.read_csv("buddymove_holidayiq.csv")
df.to_sql("review", conn)
c = conn.cursor()

print("""
Count how many rows you have - it should be 249! """)
c.execute("""
    SELECT COUNT(*)
    FROM review
""")
print(c.fetchone())

print("""
How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?""")
c.execute("""
    SELECT COUNT(*)
    FROM review 
    WHERE Nature >= 100 AND Shopping >= 100
""")
print(c.fetchone())

print("""
(Stretch) What are the average number of reviews for each category? """)
c.execute("""
    SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
    FROM review
""")
print(c.fetchone())