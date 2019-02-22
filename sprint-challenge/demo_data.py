"""Populate and query demo SQLite Database."""

import sqlite3


def check_table_exists(curs, table_name):
    """Queries database to see if table_name exists in tables.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to query
    Returns:
        (bool): if table_name exists in database"""
    return curs.execute("""SELECT COUNT(*)
    FROM sqlite_master
    WHERE type='table' AND name=?;""", (table_name,)).fetchone()[0] != 0


def create_table(curs, table_name):
    """Creates table in database.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to create
    Returns:
        None"""
    curs.execute("""CREATE TABLE {} (
        s TEXT PRIMARY KEY,
        x integer,
        y integer
    );""".format(table_name))


def input_values(curs, table_name, inputs):
    """Inputs values to table in database.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to input values
        inputs (list(tuple)): list of tuples of input to put into table
    Returns:
        None"""
    curs.executemany("""INSERT INTO {} (s, x, y)
    VALUES (?, ?, ?);""".format(table_name), inputs)


def num_rows(curs, table_name):
    """Queries to find number of rows in table in database.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to query
    Returns:
        (int): number of rows in table"""
    return curs.execute("""SELECT COUNT(*)
    FROM {}""".format(table_name)).fetchone()[0]


def count_rows_greater(curs, table_name, x_gte=5, y_gte=5):
    """Queries to find number of rows in table in database where x is greater
    than or equal to x_gte and y is greater than or equal to y_gte.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to query
        x_gte (int): minimum value of x for query (default 5)
        y_gte (int): minimum value of y for query (default 5)
    Returns:
        (int): number of rows with x greater than or equal to x_gte and y
            greater than or equal to y_gte"""
    assert x_gte is not None and y_gte is not None
    where_str = ""
    val = None
    if x_gte is None:
        where_str = "WHERE y >= ?"
        val = (y_gte)
    elif y_gte is None:
        where_str = "WHERE x >= ?"
        val = (x_gte)
    else:
        where_str = "WHERE x >= ? AND y >= ?"
        val = (x_gte, y_gte)
    return curs.execute("""SELECT COUNT(*)
    FROM {}
    {};""".format(table_name, where_str), val).fetchone()[0]


def count_distinct_col(curs, table_name, col='y'):
    """Queries to find number of distinct values of col column in table in
    database.

    Args:
        curs (sqlite3.Cursor): cursor to database
        table_name (str): name of table to query
        col (str): name of column to find number of distinct values for
    Returns:
        (int) number of distinct values for col"""
    return curs.execute("""SELECT COUNT(DISTINCT {})
    FROM {};""".format(col, table_name)).fetchone()[0]


if __name__ == "__main__":
    # Create connection to SQLite database and create cursor to database
    conn = sqlite3.connect('demo_data.sqlite3')
    curs = conn.cursor()

    # Check if table exists, and if not, create table and input values
    if not check_table_exists(curs, 'demo'):
        create_table(curs, 'demo')
        inputs = [
            ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7)
        ]
        input_values(curs, "demo", inputs)

        # Commit changes to database
        conn.commit()

    # Query table/database with above functions
    format_str = "{}:\t{}"
    num_str = "Number of rows"
    num_gte_str = "Number of rows w/ x >= 5 and y >= 5"
    num_dist_str = "Number of distinct y values"
    print(format_str.format(num_str, num_rows(curs, "demo")))
    print(format_str.format(num_gte_str, count_rows_greater(curs, "demo")))
    print(format_str.format(num_dist_str, count_distinct_col(curs, "demo")))

    # Close connection to database
    conn.close()
