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

# Counting how many rows; I should have 3
query1 = 'SELECT count(*) FROM demo;'
print ('Number of Rows:',conn.cursor().execute(query1).fetchone()[0], '\n')

# How many rows where both x and y are at least 5?
query2 = 'SELECT count(s) FROM demo WHERE x >= 5 AND y >= 5;'
print ('Number of Rows Where X and Y Are At Least 5:',conn.cursor().execute(query2).fetchone()[0], '\n')

# Counting unique values of y are there?
query3 = 'SELECT COUNT(DISTINCT y) FROM demo;'
print ('Number of Unique Y Values:',conn.cursor().execute(query3).fetchone()[0], '\n')

