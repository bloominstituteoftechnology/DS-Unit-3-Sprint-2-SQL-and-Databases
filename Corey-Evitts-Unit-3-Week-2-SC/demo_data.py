import sqlite3

# connect to sqlite3
conn = sqlite3.connect('demo_data.sqlite')

# create a cursor
cur = conn.cursor()

# drop table demo if it exists
cur.execute("""
DROP TABLE IF EXISTS demo;
""")

# creating a table for demo data
cur.execute("""
CREATE TABLE IF NOT EXISTS demo (
        s TEXT,
        x INTEGER,
        y INTEGER
    )
""")

# insert demo data into demo table
cur.execute("""
INSERT INTO demo (s, x, y)
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
""")

# commit create and insert
conn.commit()

# count how many rows
query = """
SELECT COUNT(*)
FROM demo;
"""
cur.execute(query)
print(cur.fetchall())

# count how many rows where x and y are at least 5
query = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 AND y >= 5;
"""
cur.execute(query)
print(cur.fetchall())

# how many unique values of y
query = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
cur.execute(query)
print(cur.fetchall())
