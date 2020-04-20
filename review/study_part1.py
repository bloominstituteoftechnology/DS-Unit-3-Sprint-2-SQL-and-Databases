import sqlite3
from sqlalchemy import create_engine
import pandas as pd 

df = pd.DataFrame(
    {"student": ["Lion-O", "Cheetara", "Mumm-Ra", "Snarf", "Panthro"],
    "studied": ["True", "True", "False", "False", "True"],
    "grade": [85, 95, 65, 70, 80],
    "age": [24, 22, 153, 15, 30],
    "sex": ["Male", "Female", "Male", "Male", "Male"]
    }
)
DB_FILEPATH = 'study_part1.sqlite3'

conn =sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()
print(type(conn))

df.to_sql('study_table', con=conn, if_exists='replace')

print("--------------")
query = """SELECT Avg(age) FROM study_table;"""
curs.execute(query)
results = curs.fetchall()
print("Average age:", results[0])

print("--------------")
query = """ SELECT student FROM study_table
WHERE sex = "Female";
"""
curs.execute(query)
result = curs.fetchall()
print("Female Students:", result)

print("--------------")
query = """ SELECT COUNT(student) FROM study_table
WHERE studied = "True";
"""
curs.execute(query)
result = curs.fetchall() 
print("Students who studied:", result)

print("--------------")
query = """ SELECT * FROM study_table
ORDER BY student 
"""
curs.execute(query)
result = curs.fetchall()
print("Students in alphabetical order:", result)

print("--------------")
