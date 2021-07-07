#!/usr/bin/env python
""" Unit3 Sprint2 Challenge - Demo Data
"""


import sqlite3


data = [('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)]


def make_table(data):
    CONN = sqlite3.connect('demo_data2.sqlite3')
    cur = CONN.cursor()
    cur.execute("""CREATE TABLE demo
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, s text NOT NULL,
        x integer NOT NULL, y text NOT NULL)""")
    for demo in data:
        cur.execute("""INSERT INTO demo (s,
            x, y) VALUES """ + str(demo))

    cur.close()
    CONN.commit()


make_table(data)


CONN = sqlite3.connect('demo_data2.sqlite3')
cur = CONN.cursor()
cur.execute("""SELECT * FROM demo""")
# <sqlite3.Cursor at 0x7f1437e0a810>


cur.fetchall()
# [(1, 'g', 3, '9'), (2, 'v', 5, '7'), (3, 'f', 8, '7')]


cur.execute("SELECT max(rowid) FROM demo")
rows = cur.fetchone()[0]
print('Demo Table # of Rows = ', rows)
# Demo Table # of Rows =  3


cur.execute("SELECT count(*) FROM demo WHERE x>=5 AND y>=5")
results1 = cur.fetchall()
print('Number of Rows where both x and y are >=5 ', results1)
# Number of Rows where both x and y are >=5  [(2,)]


cur.execute("SELECT count(DISTINCT y) FROM demo")
results2 = cur.fetchall()
print('Unique values of y = ', results2)
# Unique values of y =  [(2,)]


cur.close()
CONN.close()
