import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file, verbose=False):
    """ create a database connection to a SQLite database

    Parameter
    --------------------------------------------------------
    db_file: str
                database file path
    verbose: bool
                prints detail output of connection        
     """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        if verbose:
            print(f'Using SQLite version: {sqlite3.version}')
            print(f'Creating Connection to {db_file}...')
        return conn
    except sqlite3.Error as e:
        print(e)


def select_all_query(db_file, query, verbose=False):
    """
    Query all rows in the database table

    Parameter
    -------------------------------------------------------

    db_file: str
                database file
    return: list
                returns results as list
    """
    conn = create_connection(db_file, verbose)
    with conn:
        cur = conn.cursor()
        if not query.startswith('SELECT'):
            raise ValueError('Query should begin with `SELECT`')

        cur.execute(query)
        rows = cur.fetchall()

        if verbose:
            for row in rows:
                print(row)

        return rows


def get_sql_tables(db_file, verbose=False):
    conn = create_connection(db_file, verbose)
    with conn:
        curs = conn.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return curs.fetchall()
    return None


if __name__ == '__main__':
    create_connection('rpg_db.sqlite3', verbose=True)
