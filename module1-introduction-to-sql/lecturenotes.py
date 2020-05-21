# lecturenotes.py


import os
import sqlite3


# construct a path to wherever your database exists
# DB_FILEPATH = "data/chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dicts
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers LIMIT 3;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
#print("RESULT 2", result2)

for row in result2:
    #print(row[0], row[1], row[2])
    print(row["CustomerId"], row["FirstName"], row["LastName"])