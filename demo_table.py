import pandas as pd 
import sqlite3 

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

"Create demo table"
table = """
           CREATE TABLE demo (
               s varchar(5) NOT NULL,
               x INT,
               y INT
           );
        """

curs.execute(table)

"Insert data"
insert = """
           INSERT INTO demo (s, x, y)
           VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
        """

curs.execute(insert)
conn.commit()

"Count rows of demo table"
query = """
           SELECT COUNT(*)
           FROM demo;
        """

count = curs.execute(query).fetchall()[0][0]
print(f'There are {count} rows')

"Count rows when x and y are at least 5"
query = """
           SELECT COUNT(*)
           FROM demo
           WHERE x >= 5
           AND y >= 5;
        """
new_count = curs.execute(query).fetchall()[0][0]
print(f'There are {new_count} rows when x and y are at least 5')

"Count unique values of y"
query = """
           SELECT COUNT(DISTINCT y)
           FROM demo;
        """
distinct = curs.execute(query).fetchall()[0][0]
print(f'There are {distinct} unique values of y')