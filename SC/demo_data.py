# Import SQLite
import sqlite3

# Create the connection
conn = sqlite3.connect('demo_data.sqlite3')


# Open the cursor for the connection
c = conn.cursor()
print('Connection Open')


# Create table in the DB
c.execute('''CREATE TABLE demo (
             s VARCHAR(9) PRIMARY KEY,
             x int,
             y int)''');

conn.commit()


# Insert data into table
c.execute('''INSERT INTO demo (s, x, y) VALUES
    ('g',3,9),
    ('v',5,7),
    ('f',8,7)''');

conn.commit()


# Count rows
for row in c.execute("SELECT count(*) from demo"):
    print('Total rows:', row[0])


# Count records where x and y are at least 5
for row in c.execute("SELECT count(*) from demo where x >= 5 AND y >=5"):
    print('Rows where both x and y are at least 5:', row[0])


# Count unique values in y
for row in c.execute("SELECT count(distinct(y)) from demo"):
    print('Unique values in y:', row[0])

