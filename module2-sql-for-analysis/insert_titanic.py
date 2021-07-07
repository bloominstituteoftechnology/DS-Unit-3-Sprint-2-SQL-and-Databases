import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

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

df = pd.read_csv('titanic.csv')
print(df.head())

list_of_tuples = []
for row in df.iterrows():
    list_of_tuples.append(row)
# print(list_of_tuples)

lines = []
for i in range(1, len(df)):
    result = []
    for j in range(0, 8):
        result.append(list_of_tuples[i][1][j])
    lines.append(tuple(result))
print(lines)

# INSERTING RECORDS (MULTIPLE)

multi_insertion_query = """
INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
    Parents_Children_Aboard, Fare) VALUES %s
"""
execute_values(cursor, multi_insertion_query, lines) # third param: data as a list of tuples!

# save the transactions
connection.commit()

cursor.close()
connection.close()
