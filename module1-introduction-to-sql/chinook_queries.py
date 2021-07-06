import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "module1-introduction-to-sql/chinook.db"
#DB_FILEPATH = os.path.join("module1-introduction-to-sql", "chinook.db")
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), ",,", "module2-0...", ""chinook.db")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row), row)






# many queries

query = "SELECT count(distinct CustomerId) as customer_count FROM Customers"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result3 = cursor.execute(query).fetchone()
print("RESULT 2", type(result3), result3)

for row in result2:
    print(type(row), row)