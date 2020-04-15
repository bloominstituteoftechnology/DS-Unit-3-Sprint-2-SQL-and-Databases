import sqlite3
import os

DB_FILENAME= os.path.join(os.path.dirname(__file__),"..","data","chinook.db")
connection=sqlite3.connect(DB_FILENAME)
connection.row_factory = sqlite3.Row # lest reat our objects like dict nor tuples
curs=connection.cursor()
query="SELECT * FROM customers LIMIT 5;"
result=curs.execute(query).fetchall()
for row in result:
    print("_________")
    print(f"{row['LastName']}")
