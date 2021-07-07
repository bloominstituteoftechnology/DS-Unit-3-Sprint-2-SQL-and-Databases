import sqlite3


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Count how many rows you have - it should be 249!
query = """SELECT count(0) FROM review"""
print(curs.execute(query).fetchall()[0][0])

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
query = """
SELECT count(Sports)
FROM review
WHERE Nature >= 100
AND Shopping >= 100
"""
print(curs.execute(query).fetchall()[0][0])

# What are the average number of reviews for each category?
query = """
SELECT avg(Sports),
avg(Religious),
avg(Nature),
avg(Theatre),
avg(Shopping),
avg(Picnic)
FROM review
"""
print(curs.execute(query).fetchall())
