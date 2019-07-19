import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE demo (
                s VARCHAR(1),
                x INT,
                y INT
                )''')

cursor.execute('''INSERT INTO demo VALUES
                ('g', 3, 9),
                ('v', 5, 7),
                ('f', 8, 7)''')

conn.commit()

query1 = 'SELECT COUNT(*) FROM demo;'
answer1 = cursor.execute(query1).fetchone()
print('How many rows are in demo?', answer1[0])

query2 = 'SELECT COUNT(*) FROM demo \
          WHERE x >= 5 AND y >= 5;'
answer2 = cursor.execute(query2).fetchone()
print(answer2[0], 'rows where both x and y are at least 5.')

query3 = 'SELECT COUNT (DISTINCT y) FROM demo;'
answer3 = cursor.execute(query3).fetchone()
print(answer3[0], 'unique y values')

conn.commit()
conn.close()
