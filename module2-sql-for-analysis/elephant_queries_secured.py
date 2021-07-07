# app/elephant_queries.py

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()

print(result)


query = '''
CREATE TABLE if not exists titanic (
    id Serial Primary Key,
    Survived int,
    Pclass int,
    Name varchar,
    Sex varchar,
    Age int,
    Siblings_Spouses_Aboard int,
    Parents_Children_Aboard int,
    Fare int
);
'''

cursor.execute(query)

# inserting records (single)

insertion_query = """
INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
    Parents_Children_Aboard, Fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
record_to_insert = (0, 3, 'Mr. Owen Harris Brown', 'male', 22, 1, 0, 7.25)
cursor.execute(insertion_query, record_to_insert)

# save the transactions
connection.commit()

cursor.close()
connection.close()
