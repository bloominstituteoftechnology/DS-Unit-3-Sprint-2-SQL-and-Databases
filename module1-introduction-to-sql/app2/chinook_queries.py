import sqlite3
import os

# Construct a path to where your DB exists 
# if DB IS IN "DATA" DIR AND THIS FILE IS IN THE 'APP' DIR
# DB_FILEPATH = "chinook.db"
# NOw we can run file from anywhere in our directory and also run w/o using '/'
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # let's treat our results like object/dict 
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers LIMIT 10;"

result2 = cursor.execute(query).fetchall()
# > a list of tuples 

# TO LOOP through the return list of tuples 
for row in result2:
    print("------------")
    # print(row)
    # print(row[2])  
    print(row["LastName"])

 