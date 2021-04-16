#!/usr/bin/env python3

import sqlite3
import os

# remove sqlite3 file if it already exists
os.system('rm demo_data.sqlite3')

# open connection
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# Create Table and Insert Data
## create table
create_table ="""
CREATE TABLE demo(
s VARCHAR(1),
x INT,
y INT);
"""
curs.execute(create_table)

## Insert rows
add_row1 ="""
INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9);
"""
add_row2 ="""
INSERT INTO demo (s, x, y)
VALUES ('v', 5, 7);
"""
add_row3 ="""
INSERT INTO demo (s, x, y)
VALUES ('f', 8, 7);
"""
curs.execute(add_row1)
curs.execute(add_row2)
curs.execute(add_row3)


# Verify proper table creation
count_rows = """
SELECT COUNT(*) FROM demo;
"""
at_least_5 = """
SELECT SUM(x >=5) AS "x" , SUM(y >=5) AS "y"
FROM demo;
"""
distinct_y = """
SELECT COUNT(DISTINCT y) FROM demo;
"""
print(curs.execute(count_rows).fetchone())
print(curs.execute(at_least_5).fetchall())
print(curs.execute(distinct_y).fetchall())

# Close connection
curs.close()
conn.commit()

