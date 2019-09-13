#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Import sqlite3
import sqlite3

# Connect to database
conn = sqlite3.connect('demo_data.sqlite3')

# Create cursor
curs = conn.cursor()

# Create Table
curs.execute("""
               CREATE TABLE demo (
               s VARCHAR(1),
               x INT,
               y INT
    );
 """)

# Insert Values into table
curs.execute("""
               INSERT INTO demo
               (s, x, y)
               VALUES
               ('g', 3, 9),
               ('v', 5, 7),
               ('f', 8,7);
               """)
conn.commit()

# Number of Rows
query = """SELECT COUNT(s) FROM demo;"""
curs.execute(query)
results = curs.fetchall()
print("------ANSWERS-------")
print("Number of Rows:", results[0][0])

# Number of rows where x & y are at least 5
query = """SELECT COUNT(*) FROM demo
        WHERE x >=5 AND y >=5
        """
curs.execute(query)
results = curs.fetchall()
print('Number of rows where both x and y are at least 5:', results[0][0])

# Count unique values of y
query = """SELECT COUNT(DISTINCT Y) FROM demo"""
curs.execute(query)
results = curs.fetchall()
print('How many unique values of y are there:', results[0][0])

conn.commit()
conn.close()
