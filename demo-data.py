import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
# Create demo table and insert data
curs.execute('''CREATE TABLE demo (
    s varchar(10),
    x int,
    y int
);''')

curs.execute('''INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);''')
curs.execute('''INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);''')
curs.execute('''INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);''')

# Count rows, rows with x and y at least 5, how many unique y values

curs.execute('''SELECT COUNT(*) FROM demo;''')
print('Number of Rows:')
print(curs.fetchall())

curs.execute('''SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;''')
print('Number of rows with x and y greater than 5:')
print(curs.fetchall())

curs.execute('''SELECT COUNT(DISTINCT y) FROM demo;''')
print('Number of Unique y values:')
print(curs.fetchall())

conn.commit()
conn.close()