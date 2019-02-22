# import sqlite3 and create a file 'demo_data.sqlite3'
# open a connection

import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')

# create a cursor
curs = conn.cursor()

# create a table
curs.execute('''CREATE TABLE demo
(s text, x INT, y INT)''')

# insert the data into the table
curs.execute("INSERT INTO demo VALUES ('g', 3, 9),('v', 5, 7), ('f', 8, 7)")

conn.commit()
conn.close()

# How many rows are there where both x and y are at least 5?
total_xy_query = """SELECT COUNT(*)
FROM demo WHERE x >= 5 AND y >=  5;"""
curs.execute(total_xy_query)
print(curs.fetchall())

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?

distinct_y_query = """SELECT COUNT(DISTINCT y)
FROM demo;"""
curs.execute(distinct_y_query)
print(curs.fetchall())
