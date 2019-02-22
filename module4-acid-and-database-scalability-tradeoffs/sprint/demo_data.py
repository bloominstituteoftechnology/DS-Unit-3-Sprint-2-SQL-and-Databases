#!/usr/bin/env python 

"""SQlite3 demo_data.db queries"""


# create database
conn = sqlite3.connect('demo_data.db')
c = conn.cursor()

# create demo table 
c.execute('''CREATE TABLE demo (s, x, y)''')

# insert data 
c.execute("INSERT INTO demo VALUES ('g', 3, 9)")
c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
c.execute("INSERT INTO demo VALUES ('f', 8, 7)")

# three rows 
c.execute("SELECT * FROM demo;")
c.execute("SELECT COUNT(*) FROM demo")

# 2 rows with more than or equal five in x and y 
c.execute("SELECT COUNT(*) FROM demo WHERE demo.x >= 5 AND demo.y >= 5")

# 2 distinct values in y row
c.execute("SELECT COUNT (DISTINCT demo.y) FROM demo")