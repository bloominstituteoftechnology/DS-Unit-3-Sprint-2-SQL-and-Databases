import sqlite3

# Establish connection to sqlite db and create a cursor
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

create_table = """
    CREATE TABLE demo
    (
        s text,
        x int,
        y int
    );
    """
cur.execute(create_table)

insert_into_table = """
    INSERT INTO demo VALUES 
    ('g', 3, 9),
    ('v', 5 ,7),
    ('f', 8, 7);
"""
cur.execute(insert_into_table)

# Ensure that data is commited into sqlite DB
conn.commit()

# Cross check the data is present
cur.execute('SELECT * FROM demo;')
print(f'Check the insertion into table\n{cur.fetchall()}')

# Sprint challenge queries
cur.execute('SELECT COUNT(*) FROM demo;')
print(f'Number of rows: {cur.fetchall()[0][0]}')

command = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5;
    """
cur.execute(command)
print('Number of rows with where both x and y are at least 5:')
print(cur.fetchall()[0][0])

command = """
    SELECT COUNT(DISTINCT y) FROM demo;
    """
cur.execute(command)
print(f'Unique values of y: {cur.fetchall()[0][0]}')
