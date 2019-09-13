"""
PART - 1 Making and Populating a Datbase of SC
"""
import sqlite3


print('PART - 1 Making and Populating a Datbase')
print('-'*80)

# Give database it's name or database file path
db_name = 'demo_data.sqlite3'

# Try connecting to it
try:
    conn = sqlite3.connect(db_name)
except Exception as e:
    print("Can't create or open database: ")
    print(e)

# Use context manager to manage connection to the database
with conn:
    # Make a cursor
    curs = conn.cursor()

    ############################################################
    # `CREATE TABLE` and `INSERT` values into it
    ############################################################
    drop_table_query = "DROP TABLE IF EXISTS demo;"
    create_table_query = """CREATE TABLE demo(
        s CHAR(1) PRIMARY KEY,
        x INT NOT NULL,
        y INT NOT NULL    
        );"""

    data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
    insert_query = """INSERT INTO demo VALUES(?, ?, ?);"""
    try:
        print('Dropping table `demo` if exists...')
        conn.execute(drop_table_query)
        print('Create table `demo`...')
        conn.execute(create_table_query)
        print('Insert values into `demo`...')
        conn.executemany(insert_query, data)
        conn.commit()
    except Exception as e:
        print("Can't DROP or CREATE TABLE, something happened...")
        print(e)

    ############################################################
    # `SELECT * FROM demo` to view the table
    ############################################################
    select_query = "SELECT * FROM demo;"
    try:
        print('=========++++ demo ++++=========')
        results = conn.execute(select_query).fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Can't do SELECT query something happened.")
        print(e)
    print('-'*80)
    """
    =========++++ demo ++++=========
    ('g', 3, 9)
    ('v', 5, 7)
    ('f', 8, 7)
    """
    ############################################################
    # Count how many rows you have - it should be 3!
    ############################################################
    select_query = "SELECT COUNT(*) FROM demo;"
    try:
        print('Count how many rows you have - it should be 3!')
        results = conn.execute(select_query).fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Can't do SELECT query something happened.")
        print(e)
    print('-'*80)
    """
    Count how many rows you have - it should be 3!
    (3,)
    """
    ############################################################
    # How many rows are there where both x and y are at least 5?
    ############################################################
    select_query = """SELECT COUNT(*) FROM demo
                        WHERE x >= 5 AND y >= 5;"""
    try:
        print('How many rows are there where both x and y are at least 5?')
        results = conn.execute(select_query).fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Can't do SELECT query something happened.")
        print(e)
    print('-'*80)
    """
    How many rows are there where both x and y are at least 5?
    (2,)
    """
    ############################################################
    # How many unique values of y are there (hint - COUNT()
    # can accept a keyword DISTINCT)?
    ############################################################
    select_query = "SELECT COUNT(DISTINCT y) FROM demo;"
    try:
        print('How many unique values of y are there?')
        results = conn.execute(select_query).fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Can't do SELECT query something happened.")
        print(e)
    print('-'*80)
    """
    How many unique values of y are there?
    (2,)
    """
