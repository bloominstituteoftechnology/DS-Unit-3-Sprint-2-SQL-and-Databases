
#insert_titanic

import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import pandas as pd
import pymysql

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

#GOAL: load data/titanic.csv file into a PG database
# discern which columns (pandas?)


# CREATE THE TABLE
query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name varchar,
  sex varchar,
  age int,
  sib_spouse_count int,
  parent_child_count int,
  fare float8  
);
"""
cursor.execute(query)

cursor.execute("SELECT * from passengers;")
result = cursor.fetchall()
print("RESULT:", len(result))

if len(result) == 0:

    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
    print("file exists?", os.path.isfile(CSV_FILEPATH))
    df = pd.read_csv(CSV_FILEPATH)
    print(df.head())

    rows = list(df.itertuples(index=False, name=None))

    insertion_query = "INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
    execute_values(cursor, insertion_query, rows)

# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()
