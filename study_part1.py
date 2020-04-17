

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

# FOR INSERTING THE VALUES INTO TABLE/
# ONLY RUN ONCE UNLESS YOU WANT DUPLICATES:

insert = '''
INSERT OR REPLACE INTO student_table
 VALUES('Lion-O', 'True', 85, 24, 'Male'),
       ('Cheetara', 'True', 95, 22, 'Female'),
       ('Mumm-Ra', 'False', 65, 153, 'Male'),
       ('Snarf', 'False', 70, 15, 'Male'),
       ('Panthro', 'True', 80, 30, 'Male')'''


# IF YOU NEED TO DELETE THE VALUES FROM TABLE:

# delete_query = '''
# DELETE FROM student_table
# '''



# What is the average age? Expected Result - 48.8

query1 = """
SELECT 
AVG(age)
FROM student_table
;
"""
print ("-----------------------------------------------")
results1 = conn.execute(query1).fetchall()
print ("What is the average age? Expected Result - 48.8")
print("average age:", results1)
print ("-----------------------------------------------")


# What are the name of the female students? Expected Result - 'Cheetara'

query2 = """
SELECT student
FROM student_table
WHERE sex = 'Female'
;
"""
print ("----------------------------------------------------------------------")
results2 = conn.execute(query2).fetchall()
print ("What are the name of the female students? Expected Result - 'Cheetara'")
print("Names of female students:", results2)
print ("----------------------------------------------------------------------")


# How many students studied? Expected Results - 3


query3 = """
SELECT student
FROM student_table
WHERE studied = 'True'
;
"""
print ("----------------------------------------------------------------------")
results3 = conn.execute(query3).fetchall()
print ("How many students studied? Expected Results - 3")
print("Students who studied:", results3)
print ("----------------------------------------------------------------------")


# Return all students and all columns, sorted by student names in alphabetical order.

query4 = """
SELECT *
FROM student_table
ORDER BY student
;
"""
print ("----------------------------------------------------------------------")
results4 = conn.execute(query4).fetchall()
print ("Return all students and all columns, sorted by student names in alphabetical order.")
print(results4)
print ("----------------------------------------------------------------------")


conn.commit()

conn.close()