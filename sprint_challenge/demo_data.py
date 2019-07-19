import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curr = conn.cursor()

curr.execute('''
DROP TABLE demo;''')
curr.execute('''
CREATE TABLE demo (
s TEXT,
x INTEGER,
y INTEGER)''')
curr.execute('''
INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9);''')
curr.execute('''
INSERT INTO demo (s, x, y)
VALUES  ('v', 5, 7);''')
curr.execute('''
INSERT INTO  demo (s, x, y)
VALUES ('f', 8, 7)
''')
conn.commit()

row_count = curr.execute('''
SELECT COUNT(*) FROM demo;''').fetchall()
print(f'Number of rows: {list(row_count)}')

row_min_five = curr.execute('''
SELECT COUNT(*) FROM demo
WHERE x >= 5 AND y >= 5;''').fetchall()
print(f'Rows with x and y >= 5 {list(row_min_five)}')

unique = curr.execute('''
SELECT DISTINCT y FROM demo;''').fetchall()
print(f'{len(list(unique))} number of distinct "y" values.')
