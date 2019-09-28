"""Begin with the import"""

import sqlite3

conn = sqlite3.connect('demo_data1.sqlite3')
curs = conn.cursor()

"""Defining the columns of the table, this will begin the foundation"""

print('Creating demo table:')
def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS demo(s VARCHAR(1), x INTEGER, y INTEGER)')

"""Beginning to fill the table with the pertinent information"""
def data_entry():
    curs.execute("INSERT INTO demo VALUES ('g', 3, 9)")
    curs.execute("INSERT INTO demo VALUES ('v', 5, 7)")
    curs.execute("INSERT INTO demo VALUES ('f', 8, 7)")
    conn.commit()
    curs.close()
    conn.close()


create_table()
data_entry()


"""Questions to be answered"""

print('Total number of rows:')
q3 = 'SELECT COUNT(*) FROM demo;'
print(curs.execute(q3).fetchall())
"""[(3,)]"""

print('How many rows are there where both x and y are at least 5?')
#include >= because of "at least"
q4 = 'SELECT COUNT (*) FROM demo WHERE x >= 5 and y >= 5;'
print(curs.execute(q4).fetchall())
"""[(2,)]"""

print('How many unique values of y are there?')
q5 = 'SELECT COUNT (DISTINCT y) FROM demo'
print(curs.execute(q5).fetchall())
"""[(2,)]"""
