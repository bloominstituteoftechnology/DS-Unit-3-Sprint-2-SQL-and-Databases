"""
### Part 1 - Making and populating a Database

Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 3!
- How many rows are there where both `x` and `y` are at least 5?
- How many unique values of `y` are there (hint - `COUNT()` can accept a
keyword `DISTINCT`)?

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
added to the repository along with the generated SQLite database.
"""

import sqlite3

# I made this file so that you can reproduce all the correct results by running
# `python demo_data.py` and it will print the results.
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

query_create_table = """
    CREATE TABLE demo (
        s VARCHAR(1) PRIMARY KEY,
        x INT,
        y INT
    );
    """
curs.execute(query_create_table)

list_demo = [['g', 3, 9],
             ['v', 5, 7],
             ['f', 8, 7]]
for list_i in list_demo:
    insert_list = """
    INSERT INTO demo
    (s, x, y)
    VALUES (""" + str(list_i)[1:-1] + ");"
    curs.execute(insert_list)

curs.close()
conn.commit()

curs = conn.cursor()

query_count_all = """
    SELECT COUNT(*)
    FROM demo;
    """
curs.execute(query_count_all)
count_all = curs.fetchall()[0][0]
print("The total number of rows in demo is: {}".format(count_all))

query_count_x_y = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5
    AND y >= 5;
    """
curs.execute(query_count_x_y)
count_x_y = curs.fetchall()[0][0]
print("The total number of rows where x and y is at least 5 in demo is: {}"
      .format(count_x_y))

query_count_unique_y = """
    SELECT COUNT(DISTINCT(y))
    FROM demo;
    """
curs.execute(query_count_unique_y)
count_unique_y = curs.fetchall()[0][0]
print("The total number of unique y values in demo is: {}"
      .format(count_unique_y))

curs.close()
conn.close()
