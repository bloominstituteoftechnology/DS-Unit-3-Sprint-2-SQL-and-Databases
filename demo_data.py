import sqlite3


# Open a connection to a new db file
# Make a cursor, and execute an appropriate CREATE TABLE statement
conn = sqlite3.Connection('demo_data.sqlite3')
curs = conn.cursor()

query = '''CREATE TABLE demo (
            s TEXT NOT NULL PRIMARY KEY,
            x INTEGER,
            y INTEGER);'''
curs.execute(query)

# Write and execute appropriate INSERT INTO statements to add the data
query = '''INSERT INTO demo (s, x, y)
            VALUES ('g', 3, 9),
                   ('v', 5, 7),
                   ('f', 8, 7);'''
curs.execute(query)

# Commit changes to file
conn.commit()

# Query db to test CREATE and INSERT
curs = conn.cursor()
print(list(curs.execute('SELECT COUNT(*) FROM demo;').fetchall()))
print(list(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;').fetchall()))
print(list(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall()))
