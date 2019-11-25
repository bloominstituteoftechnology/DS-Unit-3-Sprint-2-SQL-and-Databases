# Importing the SQLite.

import sqlite3

# Creating the connection to the database and the cursor to manipulate it.

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Creating the table.

query = "CREATE TABLE demo (s TEXT, x INTEGER, y INTEGER)"
curs.execute(query)
conn.commit()

# Inserting values into our database.

curs.execute("INSERT INTO demo VALUES ('g', 3, 9)")
curs.execute("INSERT INTO demo VALUES ('v', 5, 7)")
curs.execute("INSERT INTO demo VALUES ('f', 8, 7)")
conn.commit()

"""## **Questions to Part 1**

- Count how many rows you have - it should be 3!
- How many rows are there where both `x` and `y` are at least 5?
- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?
"""

# Answer to Question 1.

queryQ1 = "SELECT COUNT (*) FROM demo"
answerQ1 = curs.execute(queryQ1).fetchall()

print(f'There is a total of {answerQ1[0][0]} rows in this database.')

# Answer to Question 2.

queryQ2 = "SELECT COUNT(x), COUNT(y) FROM demo WHERE x >= 5 AND y >=5"
answerQ2 = curs.execute(queryQ2).fetchall()

print(f'There is a total of {answerQ2[0][0]} values in x column above 5.')
print(f'There is a total of {answerQ2[0][1]} values in y column above 5.')

# Answer to Question 3.

queryQ3 = "SELECT COUNT(DISTINCT(y)) FROM demo"
answerQ3 = curs.execute(queryQ3).fetchall()

print(f'There is a total of {answerQ3[0][0]} unique y values.')
