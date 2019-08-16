import sqlite3

con = sqlite3.connect('demo_data.sqlite3')

cursor = con.cursor()

create1 = ''' CREATE TABLE demo (
            s TEXT,
            x INT,
            y INT);'''

cursor.execute(create1)

insert1 = ''' INSERT INTO demo
            (s, x, y)
            VALUES
            ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7);'''

cursor.execute(insert1)

cursor.close()
con.commit()

cursor2 = con.cursor()

query1 = '''SELECT COUNT(*) FROM demo'''
cursor2.execute(query1)
rows1 = cursor2.fetchall()
for row in rows1:
    print(f'Total number of rows: {row[0]}')

"""
ANSWER: Total number of rows: 3

"""

query2 = '''SELECT COUNT(*) FROM demo
         WHERE x>=5 AND y>=5'''

cursor2.execute(query2)
rows2 = cursor2.fetchall()
for row in rows2:
    print(f'Total number of rows where both x and y are at least 5: {row[0]}')

"""
ANSWER: Total number of rows where both x and y are at least 5: 2

"""

query3 = '''SELECT COUNT (DISTINCT y) FROM demo'''

cursor2.execute(query3)
rows3 = cursor2.fetchall()
for row in rows3:
    print(f'Total number of unique values of y: {row[0]}')

"""
ANSWER: Total number of unique values of y: 2

"""

cursor2.close()
con.commit()
