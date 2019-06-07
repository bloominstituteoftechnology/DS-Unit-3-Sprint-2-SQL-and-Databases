import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = '''CREATE TABLE demo (
    s VARCHAR(1),
    x INT,
    y INT
)'''

curs.execute(create_demo_table)
demo_data_insert = '''INSERT INTO demo VALUES
                      ('g',3,9), ('v',5,7), ('f',8,7)'''

curs.execute(demo_data_insert)
conn.commit()

query = 'SELECT COUNT(*) FROM demo;'
result = curs.execute(query).fetchone()
print('How many rows are in demo?', result[0])

query = 'SELECT COUNT(*) FROM demo WHERE x >= 5 and y >= 5'
result = curs.execute(query).fetchone()
print('How many rows are there where both x and y are at least 5?', result[0])

query = 'SELECT COUNT(DISTINCT y) FROM demo'
result = curs.execute(query).fetchone()
print('How many unique values of y are there?', result[0])