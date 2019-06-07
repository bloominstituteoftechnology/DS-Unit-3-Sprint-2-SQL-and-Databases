import sqlite3

# Part 1

# Create demo_data database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create demo table
create_demo_table = """
CREATE TABLE demo (
    s VARCHAR(1),
    x INT,
    y INT)
"""

# Add demo table to demo_data
curs.execute(create_demo_table)

# Insert data
insert = """INSERT INTO demo(s, x, y)
            VALUES('g', 3, 9),
                    ('v', 5, 7),
                    ('f', 8, 7)"""
curs.execute(insert)

# Commit changes
conn.commit()

# Test queries
# Count how many rows you have - it should be 3!
curs = conn.cursor()
curs.execute('SELECT COUNT(*) FROM demo;')
curs.fetchall()
# Output: [(3,)]

# How many rows are there where both x and y are at least 5?
curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;')
curs.fetchall()
# Output: [(2,)]

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
curs.execute('SELECT COUNT(DISTINCT y) FROM demo;')
curs.fetchall()
# Output: [(2,)]
