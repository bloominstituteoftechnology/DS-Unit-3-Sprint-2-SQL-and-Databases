import sqlite3


con = sqlite3.connect('demo_data.sqlite3')
curs = con.cursor()

q1 = '''
CREATE TABLE demo_data
(s, x, y);
'''

curs.execute(q1)

q2 = '''
INSERT INTO demo_data
VALUES ("g", 3, 9), ("v", 5, 7), ("f", 8, 7);
'''

curs.execute(q2)
con.commit()

q3 = '''
SELECT
VALUES ("g", 3, 9), ("v", 5, 7), ("f", 8, 7);
'''

# Not sure why this returns -1
curs.execute('SELECT * FROM demo_data').rowcount

rows1 = len(curs.execute('SELECT * FROM demo_data').fetchall())

q4 = '''
SELECT *
FROM demo_data
WHERE x >= 5 AND y >= 5;'''
rows2 = len(curs.execute(q4).fetchall())

q5 = '''
SELECT COUNT(DISTINCT y)
FROM demo_data
'''
rows3 = curs.execute(q5).fetchall()[0][0]

con.close()

print(f'There are {rows1} rows in demo_data\n')
print(f'{rows2} rows have both x and y greater or equal to 5\n')
print(f'There are {rows3} unique values for y\n')
