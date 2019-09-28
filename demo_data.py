"""Begin with the import"""

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

"""Defining the columns of the table, this will begin the foundation"""

print('Creating demo table:')
q1 = """
CREATE TABLE demo (
    s varchar(1),
    x int,
    y int
);
"""
print(curs.execute(q1).fetchall())

"""Beginning to fill the table with the pertinent information"""

q2 = """
INSERT INTO demo
(s, x, y)
VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
print(curs.execute(q2).fetchall())

"""Questions to be answered"""

print('Total number of rows:')
q3 = """
SELECT COUNT(*)
FROM demo;
"""
print(curs.execute(q3).fetchall())

print('How many rows are there where both x and y are at least 5?')
#include >= because of "at least"
q4 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 and y >= 5;
"""
print(curs.execute(q4).fetchall())

print('How many unique values of y are there?')
q5 = """
SELECT COUNT (DISTINCT y)
FROM demo
"""
print(curs.execute(q5).fetchall())
