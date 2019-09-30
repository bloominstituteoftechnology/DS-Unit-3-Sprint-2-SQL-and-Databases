# Part 1 - Making and populating a database.

import sqlite3

FIELD_NAMES = ['s', 'x', 'y']
ROWS = [
    ['g', 3, 9],
    ['v', 5, 7],
    ['f', 8, 7]
]

# Create (and connect to) database.
CONN = sqlite3.connect('demo_data.sqlite3')


def create_demo(conn):
    """Create empty demo table."""
    curs = conn.cursor()
    create_demo = ('CREATE TABLE demo ('
                   's CHAR(1), '
                   'x INT, '
                   'y INT);')
    curs.execute(create_demo)
    conn.commit()


def insert_demo(conn):
    """Fill demo table with sample data."""
    curs = conn.cursor()
    for row in ROWS:
        insert_demo = 'INSERT INTO demo VALUES("{}", {}, {});'.format(*row)
        curs.execute(insert_demo)
    conn.commit()


def select_demo(conn):
    """Select all rows from demo table."""
    curs = conn.cursor()
    select_demo = ('SELECT * FROM demo;')
    curs.execute(select_demo)
    print('Table:')
    print(FIELD_NAMES)
    print('\n'.join([str(row) for row in curs]), '\n')


def count_demo(conn):
    """Count total number of rows in demo table."""
    curs = conn.cursor()
    count_demo = ('SELECT COUNT(*) FROM demo;')
    print('Count how many rows you have - it should be 3!')
    print(curs.execute(count_demo).fetchall(), '\n')


def gt_demo(conn):
    """Count rows in demo table where both x and y are at least 5."""
    curs = conn.cursor()
    gt_demo = ('SELECT COUNT(*) FROM demo '
               'WHERE x >= 5 AND y >= 5;')
    print('How many rows are there where both x and y are at least 5?')
    print(curs.execute(gt_demo).fetchall(), '\n')


def distinct_demo(conn):
    """Count distinct values of y in demo table."""
    curs = conn.cursor()
    print('How many unique values of y are there (hint - COUNT() can accept a '
          'keyword DISTINCT)?')
    distinct_demo = ('SELECT COUNT(DISTINCT y) FROM demo;')
    print(curs.execute(distinct_demo).fetchall(), '\n')


if __name__ == '__main__':
    create_demo(CONN)

    insert_demo(CONN)

    select_demo(CONN)
    # Query returns:
    # [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

    count_demo(CONN)
    # Query returns:
    # [(3,)]

    gt_demo(CONN)
    # Query returns:
    # [(2,)]

    distinct_demo(CONN)
    # Query returns:
    # [(2,)]

    CONN.close()
