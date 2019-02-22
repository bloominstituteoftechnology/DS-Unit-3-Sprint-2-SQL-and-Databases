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

    # Commit data and close connection
    connection.commit()
    connection.close()


if __name__ == '__main__':
    run_part_one()

