# /Users/masonnystrom/Desktop/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/Chinook_queries.pyimport 

import sqlite3

# construct a path to wherever your database exist
# if database is in same filepath as this script
DB_FILEPATH = "chinook.db"

# if it is not in the same directory/filepath
# DB_FILEPATH = os.path.join(os.path.dirname(__file__),chinoon.db")
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinoon.db")


connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # let's treat our results like objects/dictionaries
print('Connection:', connection)

cursor = connection.cursor()
print("Cursor", cursor)

query = "SELECT * FROM customers;"

result2 = cursor.execute(query).fetchall() 
# print("RESULT 2", result2)
#> a list of tuples 

for row in result2:
    print("-----------")
    print(row['LastName']) # with line 9 connection.rows
    # print(row) # remove line 9 connection.rows
    # print('Last name:', row[2]) #prints last name


# # only fetch first row
# result3 = cursor.execute(query).fetchone() 
# print("RESULT 2", result3)
