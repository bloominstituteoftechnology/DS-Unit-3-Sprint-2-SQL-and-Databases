'''Sprint Challenge  U3S2 - Part 1'''

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create table
query = 'CREATE TABLE demo (s varchar(1), x int, y int);'
curs.execute(query)

# Insert values into table
insert_query = "INSERT INTO demo VALUES ('g',3,9)"
curs.execute(insert_query)
insert_query = "INSERT INTO demo VALUES ('v',5,7)"
curs.execute(insert_query)
insert_query = "INSERT INTO demo VALUES ('f',8,7)"
curs.execute(insert_query)

# Save table
conn.commit()


#Query table

# How many rows?
query = 'SELECT COUNT(*) FROM demo'
print(curs.execute(query).fetchall())

# How many rows where both x and y are at least 5?
query = '''SELECT COUNT(*) FROM demo
           WHERE x>= 5 AND y>=5'''
print(curs.execute(query).fetchall())

# How many unique values of y are there?
query = '''SELECT COUNT(distinct y) FROM demo'''
print(curs.execute(query).fetchall())
