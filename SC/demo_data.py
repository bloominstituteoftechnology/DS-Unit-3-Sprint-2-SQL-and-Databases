import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Make table
create_table = """
    CREATE TABLE demo
    (
        s TEXT,
        x INTEGER,
        y INTEGER
    );
    """
curs.execute(create_table)
curs.close()

# Add data to table


def add_row(connection, row):
    insert_statement = 'INSERT INTO demo (s, x, y) VALUES ' + str(row) + ';'
    curs = conn.cursor()  # get cursor
    curs.execute(insert_statement)
    curs.close()
    conn.commit()
    return

rows = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
for row in rows:
    add_row(conn, row)

# Query the table
curs = conn.cursor()

num_rows = curs.execute('SELECT COUNT(*) FROM demo;').fetchone()[0]
print(f'\nThe demo table has {num_rows} rows.')

"""Output:
The demo table has 3 rows.
"""

# Number of rows with x and y both above 5
at_least_five_query = """
    SELECT COUNT(*) FROM demo
     WHERE x >= 5 AND y >= 5;
    """

at_least_five = curs.execute(at_least_five_query).fetchone()[0]
print('The number of rows where both x and y are five or more '
      f'is {at_least_five}.')

"""Output:
The number of rows where both x and y are five or more is 2.
"""

# Number of unique y values
unique_ys = curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchone()[0]
print(f'There are {unique_ys} unique y values.\n')

"""Output:
There are 2 unique y values.
"""

curs.close()
conn.close()
