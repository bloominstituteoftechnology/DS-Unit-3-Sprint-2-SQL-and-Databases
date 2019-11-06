#!/usr/bin/env python
"""Demo Data"""

import sqlite3


# Create File with Empty Table
conn = sqlite3.connect('demo_data.sqlite3')

# Create Cursor
curs = curs = conn.cursor()

# Create Table
create_table = """
CREATE TABLE demo_data (
  id SERIAL PRIMARY KEY,
  s varchar(30),
  x int,
  y int);
"""
curs.execute(create_table)

# Add to Table
dict_demo = {'s': ['g','v','f'], 'x': [3,5,8], 'y': [9,7,7]}
import pandas as pd
results = pd.DataFrame(dict_demo)

for i in range(len(results)):
  insert_result = """INSERT INTO demo_data
  (s, x, y
  ) VALUES """ + str(result[i])
  curs.execute(insert_result)


conn.commit() 

print(curs.fetchall())


# Questions

# Question 1
query1 = """
SELECT COUNT(*)
FROM demo_data AS demo
"""
curs.execute(query1)
print (curs.fetchone()[0]))

# Question 2
query2 = """
SELECT COUNT(*)
FROM demo_data AS demo
WHERE demo.x > 5, demo.y > 5
"""
curs.execute(query2)
print (curs.fetchone()[0]))

# Question 3
query3 = """
SELECT COUNT(DISTINCT demo.y)
FROM demo_data AS demo
"""
curs.execute(query3)
print (curs.fetchone()[0]))
