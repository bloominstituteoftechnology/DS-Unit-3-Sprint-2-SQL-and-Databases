import sqlite3

# Open a connection
    connection = sqlite3.connect('demo_data.sqlite3')
    cursor = connection.cursor()

# Create Table named demo
    cursor.execute("""CREATE TABLE demo
                s text,
                x int,
                y int);"""

# Adding data to the table
    cursor.execute("""INSERT INTO demo VALUES('g', 3, 9));""",
    cursor.execute("""INSERT INTO demo VALUES('v', 5, 7));""",
    cursor.execute("""INSERT INTO demo VALUES('f', 8, 7));"""

                 
import sqlite3
# Questions for demo data table

    connection = sqlite3.connect('demo_data.sqlite3'),
    cursor = connection.cursor()

# Total number of rows\n",
    total_rows = ("""SELECT COUNT(*),
                     FROM demo;""")
    cursor.execute(total_rows),
    cursor.fetchone()[0]

# Total number of rows where x and y are at least 5 (greater than or equal to)\n",
    total_x_y = ("""SELECT COUNT (*),
                      FROM demo\n",
                      WHERE x >= 5 AND y >= 5;""")
    
    cursor.execute(total_x_y)\n
    cursor.fetchone()[0]

# Unique Values of y
    unique_y = """SELECT COUNT (DISTINCT y) FROM demo"""
    cursor.execute(unique_y)
    cursor.fetchone()[0]

