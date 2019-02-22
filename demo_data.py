import sqlite3


conn = sqlite3.connect('p1.db')
curs = conn.cursor()

query = """
CREATE TABLE sxy (
    s varchar(1),
    x int,
    y int
);
"""
curs.execute(query)
conn.commit()


curs = conn.cursor()

query = """
INSERT INTO sxy(s,x,y)
VALUES 
    ('g',3,9),
    ('v',5,7),
    ('f',8,7);
"""
curs.execute(query)
conn.commit()
