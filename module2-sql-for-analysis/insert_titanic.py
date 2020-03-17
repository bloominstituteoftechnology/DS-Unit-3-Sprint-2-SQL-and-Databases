import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic['Survived'] = titanic['Survived'] == 1
load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

#
# TABLE CREATION
#
query = """
CREATE TABLE IF NOT EXISTS titanic (
  survived boolean,
  pclass smallint,
  name varchar(81),
  sex varchar(6),
  age smallint,
  siblings_spouses_aboard smallint,
  parents_children_aboard smallint,
  fare numeric
);
"""
cursor.execute(query)
cursor.execute("SELECT * from titanic;")
result = cursor.fetchall()
print("RESULT:", len(result))

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = "INSERT INTO titanic (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

for row in titanic.itertuples(index=False, name=None):
    cursor.execute(insertion_query, row)
    
cursor.execute("SELECT * from titanic;")
result = cursor.fetchall()
print("RESULT:", len(result))
# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()