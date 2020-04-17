import sqlite3

# Create connection and cursor
conn = sqlite3.connect('SprintChallenge/demo_data.sqlite3')
cur = conn.cursor()

# Create table
query = f'''
CREATE TABLE IF NOT EXISTS demo_data (
    s TEXT PRIMARY KEY,
    x INT,
    y INT
);
'''
cur.execute(query).fetchall()

# Insert data
query = f'''
INSERT INTO demo_data (s, x, y) VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7);
'''
cur.execute(query).fetchall()

# Number of rows -- should be 3
print('Number of rows:')
query = f'SELECT COUNT(s) FROM demo_data'
row_count = cur.execute(query).fetchall()
print(row_count[0][0])

# Rows where x and y are both at least 5
print('\nRows where x and y are equal to or greater than 5:')
query = f'''SELECT *
FROM demo_data
WHERE x >= 5 AND y >= 5'''
rows_with_5 = cur.execute(query).fetchall()
print(rows_with_5)

# Number of unique values in column y
print('\nNumber of unique values in column y:')
query = f'SELECT COUNT(DISTINCT y) FROM demo_data'
rows_with_5 = cur.execute(query).fetchall()
print(rows_with_5[0][0])
