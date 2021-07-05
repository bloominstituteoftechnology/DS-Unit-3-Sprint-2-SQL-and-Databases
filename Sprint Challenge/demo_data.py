"""
The purpose of this program is to create a demo data
database in conjunction with the DS3 Unit-3 Sprint-2
Sprint Challenge. The instructions are as follows:

####################################################
Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE`
  statement to accept the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 3!
- How many rows are there where both `x` and `y` are at least 5?
- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
added to the repository along with the generated SQLite database.

#######################################################
I have also added a "run_all" function so that will run the entire file.
Once the file is loaded, just type run_all() in to your REPL.
"""

import sqlite3


# I want to create global variables for the connection and cursor objects.
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

def new_table():
    """
    Creates a new table if none exists with that name. No inputs, just needs to run.

    Assumes the cursor is connected ot the database already.

    :return: New table
    """

    new_table = (" CREATE TABLE IF NOT EXISTS demo (\n"
                 "                        s text PRIMARY KEY,\n"
                 "                        x integer,\n"
                 "                        y integer\n"
                 "                    ); ")

    curs.execute(new_table)


def insert_data():
    """
    This is a hard-coded query to insert data into the demo_data db. It can be refactored
    to be more generalized, but that is not necessary for the purposes of this assignment.
    :return:
    """

    insert_query = (" INSERT INTO demo(s, x, y)\n"
                    "                       VALUES\n"
                    "                       ('g',3,9),\n"
                    "                       ('v',5,7),\n"
                    "                       ('f',8,7);")

    curs.execute(insert_query)

    conn.commit()

# The answers to the requested queries.

def get_answers():
    """
    Prints Out the Answers.
    :return: All the Answers!!!
    """
    print('Question 1: \n',
        'Number of Rows:', curs.execute('SELECT COUNT(*) FROM demo;').fetchall()[0][0])

    print('Question 2: \n',
          'Number of Rows where x and y are both at least 5:',
           curs.execute("""SELECT COUNT(*)
                        FROM demo
                        WHERE 
                        x >= 5 AND y >= 5;""").fetchall()[0][0])

    print('Question 3: \n',
        'Number of Unique Y Values:',
        curs.execute("SELECT COUNT(DISTINCT(y)) FROM demo;").fetchall()[0][0])


def run_all():
    """
    For first time use. Creates the table, inserts the data and runs the queries.
    """

    new_table()
    insert_data()
    get_answers()


