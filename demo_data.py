# imports
import sqlite3

# connect to sqlite database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# create table
create_table = '''
CREATE TABLE demo (
    s VARCHAR(30),
    x INT,
    y INT
);'''

crs.execute(create_table)

# commit table
conn.commit()

# insert values
curs.execute('''
INSERT INTO demo VALUES('g', 3, 9);''')

curs.execute('''
INSERT INTO demo VALUES('v', 5, 7);''')

curs.execute('''
INSERT INTO demo VALUES('f', 8, 7);''')

conn.commit()

# count number of rows
curs.execute('SELECT count(*) FROM demo').fetchall()

# count how many rows have x and y > 5
curs.execute('''
    SELECT count(*)
    FROM demo
    WHERE x>5
    AND y>5
    ''').fetchall()

# count how many distinct y values exist
curs.execute('''SELECT COUNT(distinct y) FROM demo''').fetchall()
