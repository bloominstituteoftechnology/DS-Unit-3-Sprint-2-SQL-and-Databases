#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('part1_db.sqlite3')


def create_table_cols():
    """Creates table for database"""
    create_statement =  """
    CREATE TABLE part1 (
    s varchar(30), 
    X INTEGER, 
    y INTEGER)"""
    curs = conn.cursor()
    result = curs.execute(create_statement)
    commit = conn.commit

    return result, commit


def insert_values():
    """Adds 3 rows of values to table"""
    insert = (
        "INSERT INTO part1 (s, X, y) VALUES "
        "('g', 'v', 'f'), "
        "(3, 5, 8), "
        "(9, 7, 7)"
    )
    curs = conn.cursor()
    result = curs.execute(insert)
    commit = conn.commit

    return result, commit
