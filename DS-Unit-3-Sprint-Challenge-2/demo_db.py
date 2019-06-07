#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('demo_db.sqlite3')
create_statement = """
CREATE TABLE part1 (
s varchar, 
X INTEGER, 
y INTEGER
);"""

curs = conn.cursor()
result = curs.execute(create_statement)
commit = conn.commit

curs
result
commit


def insert_values():
    insert = (
        "INSERT INTO part1 VALUES "
        "('g', 3, 9), "
        "('v', 5, 7), "
        "('f', 8, 7)"
        )
    rows = curs.execute(insert)

    return conn.cursor(), rows, conn.commit()


def count_rows():
    """Count part1 table rows."""
    conn = sqlite3.connect('demo_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM part1;'
    result = curs.execute(query)
    total_rows = result.fetchall()

    return print('Total Rows:', total_rows[0][0])


def find_five():
    """Find the at least the value
     of five in x and y."""
    conn = sqlite3.connect('demo_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM part1 ' \
            'WHERE X = 5 OR y = 5;'
    result = curs.execute(query)
    five = result.fetchall()

    return print('Total Rows with a value of 5:', five[0][0])


def unique_y():
    """Queries and outputs the unique
     values of the y column"""
    conn = sqlite3.connect('demo_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (DISTINCT y) FROM part1;'
    result = curs.execute(query)
    unique = result.fetchall()

    return print("'y' unique value count:", unique[0][0])
