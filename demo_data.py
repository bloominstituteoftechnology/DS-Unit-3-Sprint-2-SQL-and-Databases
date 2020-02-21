!#/usr/bin/env python

import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()
query='CREATE TABLE IF NOT EXISTS demo (s CHARACTER(1), x INT, y INT)'
curs.execute(query)

curs.execute('INSERT INTO demo (s,x,y) VALUES("g",3,9)')
curs.execute('INSERT INTO demo (s,x,y) VALUES("v",5,7)')
curs.execute('INSERT INTO demo (s,x,y) VALUES("f",8,7)')
conn.commit()

curs.execute('SELECT COUNT(*) FROM demo')
curs.fetchall()
[(3,)]

curs.execute('SELECT * FROM demo WHERE x >= 5 and y >= 5')
curs.fetchall()
[('v', 5, 7), ('f', 8, 7)]

curs.execute('SELECT COUNT(DISTINCT y) from demo')
curs.fetchall()
[(2,)]

