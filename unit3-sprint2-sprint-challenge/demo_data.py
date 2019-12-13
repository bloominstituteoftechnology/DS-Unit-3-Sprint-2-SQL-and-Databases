import sqlite3

""" Open connection to demo_data database"""
conn = sqlite3.connect('demo_data.sqlite3')

""" Make cursosr to read database """
curs = conn.cursor()

""" Create demo table """
demo = """
CREATE TABLE demo (
  s CHAR(1),
  x INT,
  y INT
)
"""

curs.execute(demo)
conn.commit()

""" Populate demo table """
insert = "INSERT INTO demo VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);"
curs.execute(insert)
conn.commit()

""" Count how many rows you have - it should be 3! """
print(curs.execute('SELECT COUNT(*) FROM demo;').fetchone())

""" How many rows are there where both x and y are at least 5? """
print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 and y>= 5;').fetchone())

""" How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)? """
print(curs.execute('SELECT COUNT(DISTINCT y)FROM  demo;').fetchone())

conn.commit()
