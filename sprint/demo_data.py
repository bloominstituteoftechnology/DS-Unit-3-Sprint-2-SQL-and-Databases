import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
table = '''CREATE TABLE demo(
    s VARCHAR(1),
    x NUMERIC,
    y NUMERIC
    )'''

curs.execute(table)

insert = ''' INSERT INTO demo VALUES ("g",3,9),("v",5,7),("f",8,7);'''

curs.execute(insert)

#Count how many rows you have 
query = 'SELECT COUNT(*) FROM demo'
result = curs.execute(query)
result.fetchall()

#How many rows are there where both x and y are at least 5?
query = 'SELECT COUNT(x) + COUNT(y) FROM demo WHERE x >= 5 and y >= 5'
result = curs.execute(query)
result.fetchall()

#How many unique values of y are there?
query = 'SELECT COUNT(DISTINCT(Y)) FROM demo'
result = curs.execute(query)
result.fetchall()