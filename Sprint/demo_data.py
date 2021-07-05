import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# IF NOT EXISTS lets me not have to comment out this query 
# so when I run it multiple times it doesn't yell at me
create_table = """
               CREATE TABLE IF NOT EXISTS demo(
                   s TEXT(30),
                   x INT,
                   y INT
               )
               """
curs.execute(create_table)

insert_data = """
              INSERT INTO demo(s, x, y)
              VALUES('g', 3, 9), ('v', 5, 7), ('f', 8, 7)
              """
# curs.execute(insert_data)
# conn.commit()

query = """
        SELECT COUNT(*)
        FROM demo
        """
result = curs.execute(query)
print('Number of rows', result.fetchall())

query = """
        SELECT COUNT(*)
        FROM demo
        WHERE x >= 5
        AND y >= 5;
        """
result = curs.execute(query)
print('Where x and y are at least 5', result.fetchall())

query = """
        SELECT COUNT(DISTINCT demo.y)
        FROM demo;
        """
result = curs.execute(query)
print('unique values of y', result.fetchall())
