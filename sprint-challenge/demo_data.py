import sqlite3

TABLE = "part_one"
DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

# Connect to the database
northwind = sqlite3.connect('../db/northwind_small.sqlite3')

# Remove the table 
northwind.execute("drop table if exists {}".format(TABLE))

# Create the table 
northwind.execute("create table {}(s varchar(1), x int, y int)".format(TABLE))

# Insert the data
northwind.executemany('insert into {} values (?, ?, ?)'.format(TABLE), DATA)

# Save changes
northwind.commit()

print("Q:", "Count how many rows you have - it should be 3!")
print("A:", northwind.execute("select count(*) from {}".format(TABLE)).fetchall()[0])

print("Q:", "How many rows are there where both x and y are at least 5?")
print("A:", northwind.execute("select count(*) from {} where x >= 5 and y >= 5".format(TABLE)).fetchall()[0])

print("Q:", "How many unique values of y are there?")
print("A:", northwind.execute("select count(distinct  y) from {}".format(TABLE)).fetchall()[0])

