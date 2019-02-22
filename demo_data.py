#!/usr/bin/env python 3
'''
Module created for LSDS01 Sprint Challenge on 2019-02-22
'''
import pandas as pd
import sqlite3


# Make connection object
connection = sqlite3.connect('demo_data.sqlite3')
c = connection.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS demo
          (s, x, y)''')

# Insert data into table
# three_tup_data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
# for tup in three_tup_data:
c.execute("INSERT INTO demo VALUES ('g', 3, 9)")
c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
c.execute("INSERT INTO demo VALUES ('f', 8, 7)")

# Commit data
connection.commit()


print('There are', c.execute("SELECT COUNT(*) from demo"),
      'rows in the demo table.')
print('There are',
      c.execute("SELECT COUNT(*) from demo WHERE (x>=5 and y>=5)"),
      'rows where both x and y are at least 5.')
print('There are', c.execute("SELECT COUNT(DISTINCT(y)) from demo"),  
      'unique values of y.')

