"""
@author: Harsh Desai
@date: 09/12/19
@description: Simple wrapper for python sqlite3 api
"""

import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file, verbose=False):
    """ 
    Create a database connection to a SQLite3 database

    Parameter
    --------------------------------------------------------
    db_file: str
                database file path
    verbose: bool
                prints detail output of connection

    Returns
    --------------------------------------------------------
    conn : sqlite3.Connection
                returns sqlite3 connection object
     """

    # Check if db_file path is valid
    if not os.path.isfile(db_file):
        raise IOError(f'Invalid database file path: {db_file}')

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        if verbose:
            print(f'Using SQLite version: {sqlite3.version}')
            print(f'Creating Connection to {db_file}...')
        return conn
    except sqlite3.Error as e:
        print(e)


def get_sql_tables(conn, verbose=False):
    """ 
    Returns list of SQL tables found in a database

    Parameter
    --------------------------------------------------------
    conn : sqlite3.Connection
                returns sqlite3 connection object
    verbose: bool
                prints detail output of connection

    Returns
    --------------------------------------------------------
    tables : list
                returns python lists of tables
     """
    try:
        curs = conn.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = curs.fetchall()

        if verbose:
            print('-------------- TABLES IN SQLITE3 DATABASE --------------')
            for row in tables:
                print(row)
        return tables
    except sqlite3.Error as e:
        print(e)


def get_table_info(conn, table_name, verbose=False):
    """
    Returns list of table info: like column name, data type, is_null, primary key

    Parameter
    -------------------------------------------------------
    conn : sqlite3.Connection
                returns sqlite3 connection object
    table_name : str
                name of table in sqlite3 database
    verbose: bool
                prints detail output of connection

    Returns
    --------------------------------------------------------
    results : list
                returns results as python list
    """

    # Sanity check if table exists in the database or not
    tables = get_sql_tables(conn, verbose=False)
    tables = [val[0] for val in tables]
    if not table_name in tables:
        raise ValueError(f'{table_name} not found in this database')

    # Query to find table info and return results as list
    try:
        curs = conn.cursor()
        results = curs.execute(f"PRAGMA table_info({table_name})").fetchall()

        if verbose:
            print(
                f'-------------- COLUMN INFO FOR {table_name} --------------')
            print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('cid', 'name',
                                                                'type', 'notnull', 'dflt_value', 'pk'))
            for row in results:
                for col in row:
                    if col is None:
                        col = ''
                    f_str = f'{col:<15}'
                    print(f_str, end='')
                print()
        return results

    except sqlite3.Error as e:
        print(e)


def select_query(conn, query, verbose=False):
    """
    Queries and returns results from the database

    Parameter
    -------------------------------------------------------
    conn : sqlite3.Connection
                returns sqlite3 connection object
    verbose: bool
                prints detail output of connection

    Returns
    --------------------------------------------------------
    results : list
                returns results as python list
    """
    cur = conn.cursor()
    if not query.startswith('SELECT'):
        raise ValueError('Query should begin with `SELECT`')

    cur.execute(query)
    rows = cur.fetchall()

    if verbose:
        for row in rows:
            print(row)

    return rows


if __name__ == '__main__':
    conn = create_connection('titanic.sqlite3', verbose=True)
    results = get_table_info(conn, 'titanic', verbose=True)
