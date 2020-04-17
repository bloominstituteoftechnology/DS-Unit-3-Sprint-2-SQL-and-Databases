# python module1-introduction-to-sql/chinook_queries02.py

import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#query = "SELECT * FROM customers;"
query01 = """
SELECT
  Country
  ,count(distinct CustomerId) as CustomerCount -- > 59
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""

query02 = """
SELECT tracks.Name, albums.Title
FROM albums
INNER JOIN tracks ON tracks.AlbumId = albums.AlbumId WHERE albums.AlbumId IN ('16', '17');
"""

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query02).fetchall()
print("RESULT 2", result2)

print("-----")
for row in result2:
    # print(type(row))
    print(row)
    # print(row[0])
    # print(row[1])
    # print("-----")
print("-----")