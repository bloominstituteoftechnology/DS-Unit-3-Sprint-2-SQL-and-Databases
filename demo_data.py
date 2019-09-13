# -*- coding: utf-8 -*-

import sqlite3

# establish connection and make a cursor
conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

# create demo table
create_demo_table = '''
    CREATE TABLE demo (
        s VARCHAR(100),
        x INT,
        y INT
        )
    '''

c.execute(create_demo_table)

# insert data into the demo table
insert_table = '''
    INSERT INTO demo (s, x, y)
    VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 5, 7);
    '''

c.execute(insert_table)

# commit changes
conn.commit()

# Count how many rows you have
query1 = 'SELECT COUNT(*) FROM demo'
c.execute(query1)
print(c.fetchone())
# Answer: 3

# How many rows are there where both x and y are at least 5
query2 = 'SELECT COUNT(*) from demo WHERE x >= 5 AND y >= 5'
c.execute(query2)
print(c.fetchone())
# Answer: 2

# How many unique values of y are there (hint - COUNT() can accept 
# a keyword DISTINCT)?
query3 = 'SELECT COUNT(DISTINCT y) from demo '
c.execute(query3)
print(c.fetchone())
# Answer: 2
