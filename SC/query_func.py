'''
Func for running sqlite3 queries
'''

import sqlite3


def run_query(db, query, commit=False):
    """
    Function
    ----------------------------------
    Func to run a query in sqlite3 db
    Takes you from A-Z, connection-close

    Parameters
    ---------------------------------
    db: (str) name of database to connect to

    query: (str) query to run on database

    commit: (boolean, default=False)
    Set to True to commit changes to db

    Returns
    ----------------------------------
    Result of query
    """

    conn = sqlite3.connect(db)
    curs = conn.cursor()

    result = curs.execute(query).fetchall()
    if commit:
        conn.commit()
    curs.close()
    conn.close()

    return result
