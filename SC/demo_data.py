import sqlite3

conn = sqlite3.connect('SC/demo_data.sqlite3')

# conn.close()

curs = conn.cursor()

drop_table = 'DROP TABLE IF EXISTS demo'
curs.execute(drop_table)
new_table = '''
CREATE TABLE IF NOT EXISTS demo (
    s TEXT,
    x INT,
    y INT
);
'''

curs.execute(new_table)
insert_1 = '''
INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9)
'''
insert_2 = '''
INSERT INTO demo (s, x, y)
VALUES ('v', 5, 7)
'''

insert_3 = '''
INSERT INTO demo (s, x, y)
VALUES ('f', 8, 7)
'''

curs.execute(insert_1)
curs.execute(insert_2)
curs.execute(insert_3)

show = 'SELECT * FROM demo'
print(curs.execute(show).fetchall())

# Number of rows
count = 'SELECT COUNT(*) FROM demo'
print(curs.execute(count).fetchone())

# Rows in which x and y are both over 5
rows_over_5 = 'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5'
print(curs.execute(rows_over_5).fetchall())

distinct = 'SELECT COUNT(DISTINCT y) FROM demo'
print(curs.execute(distinct).fetchall())
