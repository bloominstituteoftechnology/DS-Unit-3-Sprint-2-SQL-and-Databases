# PART 1
# to create a new connection to a blank db
import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# create a new table name and columns in table
curs.execute("""CREATE TABLE demo (s, x, y)""")

# inserting the data into table
curs.execute("INSERT INTO demo VALUES('g', 3, 9), ('v', 5, 7), ('f', 8, 7)")

# commit the changes above, this saved the file so you can access later
conn.commit()

# close the connection to the table when done
conn.close()

# To reaccess the file again:
import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
curs.execute("""SELECT * FROM demo""")
curs.fetchall()

# Count how many rows you have - it should be 3!
curs.execute("""SELECT COUNT(*) FROM demo;""")
curs.fetchall()

# How many rows are there where both x and y are at least 5?
curs.execute("""SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;""")
curs.fetchall()

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
curs.execute("""SELECT COUNT (DISTINCT y) FROM demo;""")
curs.fetchall()

