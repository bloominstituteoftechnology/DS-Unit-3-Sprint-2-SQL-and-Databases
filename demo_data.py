import sqlite3


CONN = sqlite3.connect('demo_data.sqlite3')

cursor1 = CONN.cursor()
query1 = 'CREATE TABLE demo (s VARCHAR(1), x INT, y INT);'
# cursor1.execute(query1).fetchall()

cursor1.close()
CONN.commit

cursor2 = CONN.cursor()
data = [
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)
]
for bits in data:
    cursor2.execute('INSERT INTO demo (s, x, y) VALUES' + str(bits))

cursor2.close()
CONN.commit

cursor3 = CONN.cursor()
cursor3.execute('SELECT * from demo').fetchall()
print(cursor3.execute('SELECT * from demo').fetchall())
'''[('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]'''

cursor4 = CONN.cursor()
query4 = '''SELECT COUNT() FROM demo;
            '''
cursor4.execute(query4).fetchall()
print(cursor4.execute(query4).fetchall())
'''[(3,)]'''

cursor5 = CONN.cursor()
query5 = '''SELECT COUNT() FROM demo
           WHERE demo.x >=5 AND demo.y >=5;'''
cursor5.execute(query5).fetchall()
print(cursor5.execute(query5).fetchall())
'''[(2,)]'''

cursor6 = CONN.cursor()
query6 = 'SELECT COUNT(DISTINCT y) FROM demo;'
cursor6.execute(query6).fetchall()
print(cursor6.execute(query6).fetchall())
'''[(2,)]'''
