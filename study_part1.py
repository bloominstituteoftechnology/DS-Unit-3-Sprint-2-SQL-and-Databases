

import sqlite3
from sqlalchemy import create_engine

engine = create_engine('sqlite:///study_part1.sqlite3', echo=False)

conn = sqlite3.connect('study_part1.sqlite3')

curs = conn.cursor()

create_table = """
DROP TABLE IF EXISTS student_table;
CREATE TABLE IF NOT EXISTS student_table (
    student VARCHAR(100),
    studied VARCHAR(100),
    grade INT,
    age INT,
    sex VARCHAR(20)
  );
"""

# curs.execute(create_table)

insert = '''
INSERT OR REPLACE INTO student_table
 VALUES('Lion-O', 'True', 85, 24, 'Male'),
       ('Cheetara', 'True', 95, 22, 'Female'),
       ('Mumm-Ra', 'False', 65, 153, 'Male'),
       ('Snarf', 'False', 70, 15, 'Male'),
       ('Panthro', 'True', 80, 30, 'Male')'''


# IF YOU NEED TO DELETE:

# delete_query = '''
# DELETE FROM student_table
# '''

conn.execute(insert)

conn.commit()

conn.close()