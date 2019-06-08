
# coding: utf-8
import sqlite3

conn = sqlite3.connect('demo_data0.sqlite3')

# Create empty table demo_data

curs = conn.cursor()
curs.execute("CREATE TABLE demo(s TEXT, x INT, y INT);")

# Create/Insert Values
curs = conn.cursor()
curs.execute("INSERT INTO demo(s,x,y) VALUES ('g',3,9), ('f',8,7);")

# Count how many rows you have - it should be 3!
 
curs = conn.cursor()
curs.execute("""
SELECT COUNT(*)
FROM demo;""")
result = curs.fetchall()
print(result)


# How many rows are there where both x and y are least 5?
curs = conn.cursor()
curs.execute("""
SELECT COUNT(*)
FROM demo
WHERE x >=5 and y>=5;""")
result = curs.fetchall()
print(result)

# How many uniqute values of y 
#(hint - COUNT() can accept a keyword DISTINCT)
curs = conn.cursor()
curs.execute("""
SELECT COUNT(DISTINCT(y))
FROM demo;""")
result = curs.fetchall()
print(result)
