import sqlite3
import pandas as pd

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_table = """
CREATE TABLE demo (
    s varchar(5),
    x int,
    y int
 );"""

curs.execute(create_demo_table)
conn.commit()

curs.execute("""INSERT INTO demo (
    s, x, y) VALUES""" + str(('g', 3, 9)))
conn.commit()

curs.execute("""INSERT INTO demo (
    s, x, y) VALUES""" + str(('v', 5, 7)))
conn.commit()

curs.execute("""INSERT INTO demo (
    s, x, y) VALUES""" + str(('f', 8, 7)))
conn.commit()

# Queries for SC questions


# Count how many rows you have - it should be 3!
def row_count():
    print(pd.read_sql_query("""SELECT COUNT(*) as row_count
            FROM demo;""", conn))
#    row_count
# 0          3


# How many rows are there where both x and y are at least 5?
def row_xy5():
    print(pd.read_sql_query("""SELECT COUNT(*) as row_count
            FROM demo
            WHERE x >= 5
            AND y >= 5;""", conn))
#    row_count
# 0          2


# How many unique values of y are there (hint - COUNT() can accept
# a keyword DISTINCT)?
def y_values():
    print(pd.read_sql_query("""SELECT COUNT(distinct y) as y_values
            FROM demo;""", conn))
#    y_values
# 0         2
