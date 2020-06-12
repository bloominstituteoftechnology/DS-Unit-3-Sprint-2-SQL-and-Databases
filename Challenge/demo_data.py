import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
'''
Create Table called demo ! - accidentally mispelled
'''
create = "CREATE TABLE demp(s VARCHAR,x INT, y INT);"
query = create
curs.execute(query)

'''
Fill in table:
'''
fill = '''
INSERT INTO demp (s, x, y) 
VALUES ('g', 3, 9),
 ('v', 5, 7),
 ('f', 8, 7)
 ;
 '''
curs.execute(fill)
conn.commit()

'''
Count number of rows:
'''
count_rows = '''SELECT COUNT(*) FROM demp'''
curs.execute(count_rows)

'''
How many rows are there where both `x` and `y` are at least 5?
'''
x_and_y='''
SELECT COUNT(*)
FROM demp
WHERE x>4 AND y>4
'''
curs.execute(x_and_y)

'''
How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
`DISTINCT`)?
'''
distincty = '''
SELECT COUNT (DISTINCT y) as d
FROM demp
'''
curs.execute(distincty)