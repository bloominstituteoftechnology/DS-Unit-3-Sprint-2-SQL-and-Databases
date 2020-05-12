import sqlite3
import os
# DATABASE_FILEPATH = "chinook.db"
#DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "chinook.db")
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")
connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row
print(type(connection))
cursor = connection.cursor()
print(type(cursor))
#print(dir(cursor))
query = "SELECT * FROM customers LIMIT 3"
#result = cursor.execute(query) #> NOTHING
result = cursor.execute(query).fetchall() #> LIST
for row in result:
    print("-----")
    # default:
    #print(row) #> TUPLE
    #print(row[1])
    # using row factories:
    print(row["FirstName"], row["LastName"])