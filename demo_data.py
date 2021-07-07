import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


curs.execute(
"""
CREATE TABLE demo (
s str,
x int,
y int
);
"""
)

conn.commit()

curs.execute(
"""
INSERT INTO demo
VALUES
 ('g',3,9),
 ('v',5,7),
 ('f',8,7);
""")

conn.commit()

# Count how many rows you have - it should be 3!
query = 'SELECT count(*) FROM demo;'
print ('Rows:',conn.cursor().execute(query).fetchone()[0], '\n')

# How many rows are there where both x and y are at least 5?
query2 = 'SELECT count(s) FROM demo WHERE x >= 5 AND y >= 5;'
print ('Rows X and Y at least 5:',conn.cursor().execute(query2).fetchone()[0], '\n')

# How many unique values of y are there?
query3 = 'SELECT COUNT(DISTINCT y) FROM demo;'
print ('Unique Y Values:',conn.cursor().execute(query3).fetchone()[0], '\n')

