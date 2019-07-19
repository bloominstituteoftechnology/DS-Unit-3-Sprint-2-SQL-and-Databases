import sqlite3

# set up a connection stream to a new blank database file
conn = sqlite3.connect('demo_data.sqlite3')

# create a cursor
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE demo (
    s CHAR(1),
    x INT, 
    y INT
    )""")

# insert values
cursor.execute("""
INSERT INTO demo
VALUES ('g', 3, 9);
""")
cursor.execute("""
INSERT INTO demo
VALUES ('v', 5, 7);
""")
cursor.execute("""
INSERT INTO demo
VALUES ('f', 8, 7);
""")

conn.commit()

# count the number of rows
cursor.execute("""
SELECT COUNT(*) FROM demo""")
print()
print('Number of rows:')
print('-'*16)
print(cursor.fetchall())
print()

# count the number of rows where x >= 5 AND y >= 5
cursor.execute("""
SELECT COUNT(*) FROM demo
WHERE x >=5 AND y >= 5""")
print()
print('Number of rows where x >= 5 AND y >= 5:')
print('-'*40)
print(cursor.fetchall())
print()

# Unique values of y
cursor.execute("""
SELECT COUNT(DISTINCT y) FROM demo;
""")
print()
print('Unique values of y:')
print('-'*19)
print(cursor.fetchall())
print()

conn.close()

"""
$ python demo_data.py

Number of rows:
----------------
[(3,)]


Number of rows where x >= 5 AND y >= 5:
----------------------------------------
[(2,)]


Unique values of y:
-------------------
[(2,)]
"""