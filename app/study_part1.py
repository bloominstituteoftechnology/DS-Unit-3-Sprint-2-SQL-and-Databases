# Starting from scratch

import sqlite3
import os

# create the connection and cursor to sqlite
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", 'data', "study_part1.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


# Create a table for students
table_create = """
CREATE TABLE IF NOT EXISTS students(
  id SERIAL PRIMARY KEY,
  student VARCHAR(50),
  studied VARCHAR(40),
  grade INTEGER,
  age INTEGER,
  Sex VARCHAR(10)
  );
"""

# insert data into the student table
insert_data = """
INSERT INTO students 
(student, studied, grade, age, sex)
VALUES (?, ?, ?, ?, ?);
"""

# data to insert into student table
# need some list of tuples
Lion_O = ('Lion-O', 'True', 85, 24, 'Male')
Cheetara = ('Cheetara', 'True', 95, 22, 'Female')
Mumm_Ra = ('Mumm-Ra', 'False', 65, 153, 'Male')
Snarf = ('Snarf', 'False', 70, 15, 'Male')
Panthro = ('Panthro', 'True', 80, 30, 'Male')

list_to_insert = [Lion_O, Cheetara, Mumm_Ra, Snarf, Panthro]

# execute and save query to create table
cursor.execute(table_create)
connection.commit()

# execute and commit query to insert data to table
cursor.executemany(insert_data, list_to_insert)
connection.commit()
print('We have inserted', cursor.rowcount, 'records to the table.')
