import sqlite3

# Create connection and cursor
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_cur = sl_conn.cursor()

# Create table
query = f'''
CREATE TABLE IF NOT EXISTS sc_table (
    id SERIAL PRIMARY KEY,
    name varchar(40)NOT NULL,
    data JSONB
);
'''
sl_cur.execute(query).fetchall()

# Insert data
query = f'''
INSERT INTO demo_data (s, x, y)
VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7);
'''
sl_cur.execute(query).fetchall()

# Number of rows -- should be 3
print('Number of rows:')
query = f'SELECT ROW_COUNT(demo_data)'
row_count = sl_cur.execute(query).fetchall()
print(row_count[0][0])

# Rows where x and y are both at least 5
print('\nRows where x and y are equal to or greater than 5:')
query = f'SELECT ROWS WHERE x >= 5 AND y >= 5)'
rows_with_5 = sl_cur.execute(query).fetchall()
print(rows_with_5[0][0])

# Number of unique values in column y
print('\nNumber of unique values in column y:')
query = f'SELECT COUNT(DISTINCT(y))'
rows_with_5 = sl_cur.execute(query).fetchall()
print(rows_with_5[0][0])
