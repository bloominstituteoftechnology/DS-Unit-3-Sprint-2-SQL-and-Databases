import sqlite3

connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
#how to get column names in this query?
#print(connection.execute("SELECT * FROM review LIMIT 10").fetchall())

connection.row_factory = sqlite3.Row
cursor = connection.cursor()
query = "SELECT count(*) FROM review"
result = cursor.execute(query).fetchall()
print(f"There are {result[0][0]} rows.")

query = """
SELECT
    count(distinct `User Id`)
FROM review
WHERE (Religious > 99) AND (Shopping > 99)
"""
result = cursor.execute(query).fetchall()
print(f"{result[0][0]} users who reviewed 100 of Nature and Shopping.")

query = """
SELECT avg(Sports)
    ,avg(Religious)
    ,avg(Nature)
    ,avg(Theatre)
    ,avg(Shopping)
    ,avg(Picnic)
FROM review
"""
result = cursor.execute(query).fetchall()
for row in result:
    print(dict(row))