"""answers to part one of the sprint challenge!"""


import os
import sqlite3

os.system("rm demo_data.sqlite3")

conn = sqlite3.connect('demo_data.sqlite3')

conn

import os
os.listdir()

query = 'CREATE TABLE demo (s varchar(2), x INT, y INT)'

curs = conn.cursor()

curs.execute(query)

insert_query = "INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);"

curs.execute(insert_query)

insert_query = "INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);"
curs.execute(insert_query)

insert_query = "INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);"
curs.execute(insert_query)

query = 'SELECT COUNT(*) FROM demo;'
print('\nThis is how may rows are in the demo dataset:')
print(curs.execute(query).fetchall()[0][0])

query = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;'
print('\nHow many rows are there where both x and y are greater than 5?')
print(curs.execute(query).fetchall()[0][0])

query = 'SELECT COUNT(DISTINCT y) FROM demo;'
print('\nHow many unique values of `y` are there?')
print(curs.execute(query).fetchall()[0][0])

curs.close()
conn.commit()
