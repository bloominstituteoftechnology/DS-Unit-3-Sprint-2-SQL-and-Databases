import sqlite3 as sql

demo_data = '/home/william/repos/wjarvis2/unit3_week2/demo_data.sqlite3'

conn = sql.connect(demo_data)
c = conn.cursor()

c.execute('''CREATE TABLE demo (
            s VARCHAR(20),
            x INT,
            y INT)''');

data_for_insert = [('g', 3, 9),
                  ('v', 5, 7),
                  ('f', 8, 7)]

c.executemany('INSERT INTO demo VALUES (?, ?, ?)', data_for_insert)

conn.commit()
c = conn.cursor()
c.execute('SELECT count(*) FROM demo')

print (c.fetchall())


c.execute('''SELECT count(*) FROM demo WHERE x >= 5 AND y >= 5''')

print (c.fetchall())

c = conn.cursor()

c.execute('''SELECT count(DISTINCT y) FROM demo''')

print (c.fetchall())

conn.commit()
conn.close()

