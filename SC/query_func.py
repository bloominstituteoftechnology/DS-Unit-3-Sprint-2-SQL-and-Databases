'''
Func for running sqlite3 queries
'''

import sqlite3


def run_query(db, query, commit=True):
    """
    Function
    ----------------------------------
    Func to run a query in sqlite3 db
    Takes you from A-Z, connection-close

    Parameters
    ---------------------------------
    db: (str) name of database to connect to

    query: (str) query to run on database

    commit: (boolean, default=True)
    commits query to db. If just poking around
    and don't want to set changes, set to False

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
