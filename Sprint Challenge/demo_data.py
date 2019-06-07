import sqlite3

conn = sqlite3.connect('demo_date.sqlite3')
curs = conn.cursor()

query = """CREATE TABLE demo (
    s charvar(1),
    x int, 
    y int
)"""

curs.execute(query)

query = """INSERT INTO demo (s, x, y)
           VALUES ('g', 3, 9)"""
curs.execute(query)

query = """INSERT INTO demo (s, x, y)
           VALUES ('v', 5, 7)"""
curs.execute(query)

query = """INSERT INTO demo (s, x, y)
           VALUES ('f', 8, 7)"""
curs.execute(query)

conn.commit()
curs = conn.cursor()

query = """SELECT COUNT(*) FROM demo;"""

result = curs.execute(query)
result = result.fetchall()[0][0]

# Output: 'Query 1: The demo table has 3 rows'
print(f'Query 1: The demo table has {result} rows')

query = """SELECT COUNT(*) 
           FROM demo
           WHERE x >= 5 AND y >= 5"""
result = curs.execute(query)
result = result.fetchall()[0][0]

# Output: 'Query 2: 2 rows have x and y values greater than or equal to 5'
print(f'Query 2: {result} rows have x and y values greater than or equal to 5')

query = """SELECT COUNT(DISTINCT(y))
           FROM demo"""
result = curs.execute(query)
result = result.fetchall()[0][0]

# Output: 'Query 3: Column y has 2 unique values'
print(f'Query 3: Column y has {result} unique values')