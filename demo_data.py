import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

curs.execute('''CREATE TABLE demo
(s varchar(1),
x int,
y int)
''')

curs.execute('''INSERT INTO demo(s, x, y)
VALUES ('g', 3, 9)
''')

curs.execute('''INSERT INTO demo(s, x, y)
VALUES ('v', 5, 7)
''')

curs.execute('''INSERT INTO demo(s, x, y)
VALUES ('f', 8, 7)
''')

conn.commit()

curs.execute('SELECT COUNT(*) FROM demo')
print('Row count: ', curs.fetchall())

curs.execute('SELECT * FROM demo WHERE x >=5 AND y >= 5')
print('2. ', curs.fetchall())

curs.execute('SELECT COUNT(DISTINCT  y) FROM demo')
print('3. ', curs.fetchall())