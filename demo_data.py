"""
Populates a sqlite database and answers some basic questions
"""

import sqlite3

# initialize connection
connection = sqlite3.connect('demo_data.sqlite3')
curs = connection.cursor()

# drop table if it exists, and create new table
drop_query = 'DROP TABLE IF EXISTS demo;'
create_query = """CREATE TABLE demo (
    s string,
    x int,
    y int
);"""

connection.cursor().execute(drop_query)
connection.cursor().execute(create_query)

# insert data
insert_query = """INSERT INTO demo VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);"""

connection.cursor().execute(insert_query)

# commit changes
connection.commit()

# related questions
# 1. Count how many rows you have - it should be 3!
count_rows_query = 'SELECT COUNT(s) FROM demo'
total_rows = connection.cursor().execute(count_rows_query).fetchone()[0]
print ('Total Rows:', total_rows)

# 2. How many rows are there where both `x` and `y` are at least 5?
x_y_greater_than_5_query = """SELECT COUNT (s) FROM demo
    WHERE x >= 5
    AND y >= 5;"""
x_y_large_row_count = curs.execute(x_y_greater_than_5_query).fetchone()
print ('Rows where x and y are more than 5:', x_y_large_row_count[0])

# 3. How many unique values of `y` are there (hint - `COUNT()` can accept a
# keyword `DISTINCT`)?
unique_y_query = 'SELECT COUNT (DISTINCT y) FROM demo'
unique_y = curs.execute(unique_y_query).fetchone()[0]
print ('Unique y values:', unique_y)
