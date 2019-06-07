import sqlite3
conn = sqlite3.connect("""/Users/mattkirby/Desktop/demo_data.sqlite3""")
curs = conn.cursor()

create_table = """CREATE TABLE demo(
                    s VARCHAR(5),
                    x INT,
                    y INT,
                    PRIMARY KEY(s)
                    );"""

curs.execute(create_table)

insert_values = """INSERT INTO demo (s, x, y)
                    VALUES
                    ('g', 3, 9),
                    ('v', 5, 7),
                    ('f', 8, 7);"""

curs.execute(insert_values)
conn.commit()

# 1. Count how many rows you have - it should be 3!

count_query = """SELECT COUNT(x)
                 FROM demo;"""

count_result = curs.execute(count_query)

print('1. ')
print('There are',count_result.fetchall()[0][0],'rows in the table.')
print('\n')


# 2. How many rows are there where both x and y are at least 5?

rows_query = """SELECT COUNT(*)
                 FROM demo
                 WHERE x >= 5 AND y >= 5;"""

rows_result = curs.execute(rows_query )

print('2. ')
print('There are', rows_result.fetchall()[0][0],
      'rows where both x and y are at least 5.')
print('\n')


# 3. How many unique values of y are there
#    (hint - COUNT() can accept a keyword DISTINCT)?

y_query = """SELECT COUNT(DISTINCT y)
             FROM demo;"""

y_result = curs.execute(y_query )

print('3. ')
print('There are', y_result.fetchall()[0][0], 'unique values of y.')
print('\n')
