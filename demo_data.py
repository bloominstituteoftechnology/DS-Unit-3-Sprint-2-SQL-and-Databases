import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

query1 = """

CREATE TABLE sxy (

    s varchar(1),
    x int,
    y int

);

"""

curs.execute(query1)
conn.commit()

curs = conn.cursor()

query2 = """

INSERT INTO sxy(s,x,y)
VALUES

    ('g',3,9),
    ('v',5,7),
    ('f',8,7);

"""

curs.execute(query2)
conn.commit()

'''
Count how many rows you have - it should be 3!
How many rows are there where both x and y are at least 5?
How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
'''

query3 = """

SELECT COUNT(*) FROM sxy

"""

print(curs.execute(query3).fetchall())
conn.commit()

query4 = """

SELECT COUNT(*) FROM sxy WHERE x >= 5 AND y >= 5

"""

print(curs.execute(query4).fetchall())
conn.commit()

query5 = """

SELECT COUNT (DISTINCT y) from sxy

"""

print(curs.execute(query5).fetchall())
conn.commit()
