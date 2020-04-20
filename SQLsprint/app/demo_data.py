import sqlite3
import os


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "demo_data.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# make a table !
# DROP TABLE IF EXISTS demo_data
drop_table_query = """
DROP TABLE IF EXISTS demo_data;
"""
cursor.execute(drop_table_query)

# query creates a new table
table_creation_query = """
CREATE TABLE IF NOT EXISTS demo_data (
    S NOT NULL,
    X integer,
    Y integer
);
"""
cursor.execute(table_creation_query)


# insert data into the table 
insertion_query = """
INSERT INTO demo_data(
        S, X, Y
)
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
"""
cursor.execute(insertion_query)
result = cursor.fetchall()


# query to count the rows
print("----------")
query = """
SELECT COUNT(S) FROM demo_data
"""
result = cursor.execute(query).fetchall()
print("Number of rows:", result)

# query where x and y > 5
print("-----------")
query = """
SELECT X, Y
FROM demo_data
WHERE X AND Y >= 5
"""
result = cursor.execute(query).fetchall()
print("Rows greater/equal to 5:", result)

# query unique values in y 
print("--------------")
query = """
SELECT COUNT(Distinct Y)
FROM demo_data
"""
result = cursor.execute(query).fetchall()
print("Unique values in Y:", result)


connection.commit()
connection.close()



