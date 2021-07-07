import sqlite3


# Create database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create table
create_demo_table = '''CREATE TABLE demo(
                       s VARCHAR(1),
                       x INT,
                       y INT
                       )'''

curs.execute(create_demo_table)

# Add data
data = '''INSERT INTO demo(s, x, y)
          VALUES ('g', 3, 9),
          ('v', 5, 7),
          ('f', 8, 7)'''

curs.execute(data)

# Commit changes
conn.commit()

# Count how many rows you have - it should be 3!
curs = conn.cursor()
curs.execute('SELECT COUNT(*) FROM demo;').fetchall()

# How many rows are there where both `x` and `y` are at least 5?
curs.execute('SELECT COUNT(*) \
              FROM demo \
              WHERE x >= 5 AND y >= 5;').fetchall()

# How many unique values of `y` are there?
curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall()
