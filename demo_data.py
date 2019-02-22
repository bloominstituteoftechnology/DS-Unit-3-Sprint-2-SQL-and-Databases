#!/usr/bin/env python 3
'''
Module created for LSDS01 Sprint Challenge on 2019-02-22
'''
import pandas as pd
import sqlite3


def run_part_one():
    '''
    This function performs all required tasks for Part 1 of SC
    '''
    # Make connection object
    connection = sqlite3.connect('demo_data.sqlite3')
    c = connection.cursor()

    # Create table
    c.execute('''CREATE TABLE demo
              (s, x, y)''')

    # Insert data into table
    # three_tup_data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
    # for tup in three_tup_data:
    c.execute("INSERT INTO demo VALUES ('g', 3, 9)")
    c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
    c.execute("INSERT INTO demo VALUES ('f', 8, 7)")

    # Commit data
    connection.commit()
    return c
    # connection.close()


def part_one_queries(func):
    '''
    This function performs required queries in SC
    '''
    print('There are', c.execute("SELECT COUNT(*) from demo"),
          'rows in the demo table.')
    print('There are',
          c.execute("SELECT COUNT(*) from demo WHERE (x>=5 and y>=5)"),
          'rows where both x and y are at least 5.')
    print('There are', c.execute("SELECT COUNT(DISTINCT(y)) from demo"),  
          'unique values of y.')


if __name__ == '__main__':
    part_one_queries(run_part_one())
    connection.close()

