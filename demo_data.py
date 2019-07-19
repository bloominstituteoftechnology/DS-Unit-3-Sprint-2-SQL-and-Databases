import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()

create_table = '''CREATE TABLE demo (s VARCHAR (255), x INT, y INT);'''
cursor.execute(create_table)

cursor.execute('''INSERT INTO demo VALUES ('g', 3, 9);''')
cursor.execute('''INSERT INTO demo VALUES ('v', 5, 7);''')
cursor.execute('''INSERT INTO demo VALUES ('f', 8, 7);''')
conn.commit()

cursor.execute('''SELECT COUNT(*) FROM demo''').fetchall()
#Number of rows is 3

cursor.execute('''SELECT COUNT(*) FROM demo
                WHERE (x >= 5) AND (y >= 5)
               ''').fetchall()
#2 rows where both x and y are at least 5

cursor.execute('''SELECT COUNT(DISTINCT y) FROM demo''').fetchall()
#2 unique values of y
