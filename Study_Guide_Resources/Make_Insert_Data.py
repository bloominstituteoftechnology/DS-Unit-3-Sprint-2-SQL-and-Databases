import pandas as pd
import sqlite3

# Creating & Inserting Data W/ Sqlite
import sqlite3

conn = sqlite3.connect('example_db.sqlite')


def create_statement(conn):
    curs = conn.cursor()
    create_statement ="""
    CREATE TABLE if not exists students1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(30),
    favorite_number INTEGER,
    least_favorite_number INTEGER
    );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()

def insert_data(conn):
    # SIMILAR TO GETTING DATA OF ROWS USING SL_CURS.EXECUTE AND THEN
    # FETCHING
    my_data = [
        ('Jon', 7, 12),
        ('Alejandro', 77, 43),
        ('Rivera', 100, 137)
    ]
    for row in my_data:
        curs = conn.cursor()
        insert_row = """
        INSERT INTO students
        (name ,favorite_number, least_favorite_number)
        VALUES""" + str(row) + ";"
        curs.execute(insert_row)
        conn.commit()

# Creates student table
create_statement(conn)

# Insert data from my data into students
insert_data(conn)
# commit after all insert statements have been integrated into
# data
curs = conn.cursor()
print(curs.execute('SELECT * FROM students LIMIT 10;'))
print(curs.fetchall)


