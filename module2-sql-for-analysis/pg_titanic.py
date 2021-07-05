# app/pg_titanic.py
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd


load_dotenv() 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor()

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
print("Current passenger count:", len(result))
if len(result) == 0:
    print("No passengers in database, adding from CSV.")
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
    df = pd.read_csv(CSV_FILEPATH)
    rows = list(df.itertuples(index=False, name=None))
    insertion_query = """
    INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s
    """
    execute_values(cursor, insertion_query, rows)

connection.commit()