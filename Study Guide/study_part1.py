"""
Study guide practicing importing data to sqlite file
"""

import sqlite3

# directions

sl_conn = sqlite3.connect('study_part1.sqlite3')

sl_curs = sl_conn.cursor()

"""
 student - string
    studied - string
    grade - int
    age - int
    sex - string
    """

sl_curs.execute("DROP TABLE IF EXISTS students;")
sl_conn.commit()

create_table = """
CREATE TABLE students (
    student TEXT,
    studied TEXT,
    grade INT,
    age INT,
    sex TEXT
);
"""

sl_curs.execute(create_table)

sl_conn.commit()

students = [
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male')
]

for student in students:
    insert = f"""
        INSERT INTO students (student, studied, grade, age, sex)
        VALUES {student};"""
    sl_curs.execute(insert)

sl_conn.commit()

sl_curs.execute('SELECT * FROM students;')
results = sl_curs.fetchall()

print(results)
