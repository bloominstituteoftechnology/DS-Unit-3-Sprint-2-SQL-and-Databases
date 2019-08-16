import sqlite3


# Create empty sqlite3 file
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create empty table
create__table = """
CREATE TABLE demo (
    s TEXT,
    x INT,
    y INT
);
"""
curs.execute(create__table)

# Insert data into empty table
insert_data = """
INSERT INTO demo (s, x, y) 
VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7);"""
curs.execute(insert_data)
conn.commit()

print(curs.execute('SELECT * FROM demo;').fetchall())

# Count how many rows you have - it should be 3!
print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())

# How many rows are there where both x and y are at least 5?
# 2 rows
print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;').fetchall())

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
# 2 unique values
print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())
