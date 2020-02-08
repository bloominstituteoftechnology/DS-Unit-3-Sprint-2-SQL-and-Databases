import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

query = '''CREATE TABLE demo
            (s TEXT, x INTEGER, y INTEGER)'''
curs.execute(query)
query = '''INSERT INTO demo (s, x, y)
            VALUES
            ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7)'''
curs.execute(query)
conn.commit()

query = '''SELECT COUNT(*) FROM demo'''
result = curs.execute(query).fetchone()
print(query, result)

query = '''SELECT COUNT(*) FROM demo WHERE x > 4 AND y > 4'''
result = curs.execute(query).fetchone()
print(query, result)

query = '''SELECT COUNT(DISTINCT y) FROM demo'''
result = curs.execute(query).fetchone()
print(query, result)