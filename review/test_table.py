# creates a sqlite3 table in a new file 
import sqlite3

DB_FILEPATH = 'test.sqlite3'

conn = sqlite3.connect(DB_FILEPATH)

curs = conn.cursor()


# Make a table
table_query = """
CREATE TABLE IF NOT EXISTS test (
    EmployeeId SERIAL PRIMARY KEY,
    FirstName varchar NOT NULL,
    LastName varchar NOT NULL,
    ReportsTo integer
)
"""
curs.execute(table_query)
result = curs.fetchall()

#insert data into table
insertion_query = """
INSERT INTO test(
    EmployeeId,
    FirstName,
    LastName,
    ReportsTo
)
VALUES 
(3, 'Jack', 'Smith', 2),
(4, 'Sarah', 'Fink', 2),
(2, 'Gunnar', 'Jefferson', 1),
(1, 'Boss', 'Man', NULL)
"""
curs.execute(insertion_query)
result = curs.fetchall()
print(result)

# test
test = curs.execute('SELECT * FROM test').fetchall()
print(test)
conn.commit()