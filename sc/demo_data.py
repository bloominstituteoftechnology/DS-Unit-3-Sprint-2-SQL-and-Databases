import sqlite3

conn = sqlite3.connect('sc/demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = """
CREATE TABLE demo (
    s varchar(1),
    x INT,
    y INT
);
"""

curs.execute(create_demo_table)

insert_data = """
INSERT INTO demo (s, x, y)
VALUES ('g', '3', '9')
"""
curs.execute(insert_data)

insert_data_2 = """
INSERT INTO demo (s, x, y)
VALUES ('v', '5', '7')
"""
curs.execute(insert_data_2)

insert_data_3 = """
INSERT INTO demo (s, x, y)
VALUES ('f', '8', '7')
"""
curs.execute(insert_data_3)

query = 'SELECT count(*) FROM demo;'
curs.execute(query)
rows = curs.fetchall()
print(f'The number of rows is {rows[0][0]}')

print()

query = 'SELECT count(*) FROM demo WHERE x > 4 AND y > 4;'
curs.execute(query)
rows = curs.fetchall()
print(f'The number of great values is {rows[0][0]}')

print()

query = 'SELECT COUNT(DISTINCT(y)) FROM demo;'
curs.execute(query)
rows = curs.fetchall()
print(f'The number of distinct y is {rows[0][0]}')
