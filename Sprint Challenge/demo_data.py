import sqlite3

# Connect to a database
conn = sqlite3.connect('demo_data.sqlite3')

# Make a cursor to read the database
curs = conn.cursor()

# Create a table
demo = '''
CREATE TABLE demo (
    s CHAR(1),
    x INT,
    y INT
)
'''


# Execute to create demo data
curs.execute(demo)

# INSERT INTO demo VALUES to create new values of columns
insert = "INSERT INTO demo VALUES ('g', 3, 9), ('v', 5, 7),('f', 8, 7);"

# Execute to insert into demo table
curs.execute(insert)
conn.commit()

# Count how many rows
result_count = curs.execute('SELECT COUNT(*) FROM demo;').fetchone()
print('Number of rows', result_count[0], 'rows')

# How many rows where both x and y are >= 5
result_count_5 = curs.execute('SELECT COUNT(*) FROM demo WHERE x >=5 AND y >= 5;').fetchone()
print('Number of rows:', result_count_5[0], 'rows of x and y is >= 5')

# How many unique values of y are there?
result_unique_y = curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchone()
print('Number of unique values:', result_unique_y[0], 'unique values')
