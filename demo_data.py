import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

print('Creating table demo:')
query1 = """
CREATE TABLE demo (
    s varchar(1),
    x int,
    y int
);
"""
print(curs.execute(query1).fetchall())

query2 = """
INSERT INTO demo
(s, x, y)
VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
print(curs.execute(query2).fetchall())

print('Total number of rows:')
query3 = """
SELECT COUNT(*)
FROM demo;
"""
print(curs.execute(query3).fetchall())

print('How many rows are there where both x and y are at least 5?')
query4 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 and y >= 5;
"""
print(curs.execute(query4).fetchall())

print('How many unique values of y are there?')
query5 = """
SELECT COUNT (DISTINCT y)
FROM demo
"""
print(curs.execute(query5).fetchall())