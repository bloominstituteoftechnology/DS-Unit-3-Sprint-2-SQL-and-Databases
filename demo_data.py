# !env/bin/python

import sqlite3


query = """
CREATE TABLE demo(
	s TEXT,
	x INT,
	y INT
);"""

query1 = """
INSERT INTO demo
(s, x, y)
VALUES
('g',3,9);
"""
query2 = """
INSERT INTO demo
(s, x, y)
VALUES
('v',5,7);
"""
query3 = """
INSERT INTO demo
(s, x, y)
VALUES
('f',8,7);
"""


# create sqlite object demo_data and connect to it
conn = sqlite3.connect('demo_data.sqlite3')
# cursor
cur = conn.cursor()
# Create Table demo and Insert some data into it:
cur.execute(query)
cur.execute(query1)
cur.execute(query2)
cur.execute(query3)
cur.execute('SELECT * FROM demo;')
# display data
cur.fetchall()
# save table and data
conn.commit()

# Queries with demo data:

cur.execute('SELECT COUNT (*) FROM demo;')
# Returns 3
cur.fetchall()

query4 = """
SELECT x, y FROM demo
WHERE x >= 5 AND y >=5;
"""
cur.execute(query4)
cur.fetchall()
"""Answer:
[(5, 7), (8, 7)]"""


query5 = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
cur.execute(query5)
cur.fetchall()










