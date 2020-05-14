import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import sqlite3
import pandas as pd
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv()

CSV_NAME = os.getenv("CSV_NAME")
CSV_USER = os.getenv("CSV_USER")
CSV_PASSWORD = os.getenv("CSV_PASSWORD")
CSV_HOST = os.getenv("CSV_HOST")

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)
print(df.head())

connection = psycopg2.connect(dbname=CSV_NAME, user=CSV_USER, password=CSV_PASSWORD, host=CSV_HOST)
print(type(connection))

cursor = connection.cursor()
print("CURSOR", cursor)

table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
cursor.execute(table_creation_query)

insertion_query = """INSERT INTO passengers (survived, pclass, name, gender, age,
                     sib_spouse_count, parent_child_count, fare) VALUES %s"""

rows_to_insert = list(df.to_records(index=False))

execute_values(cursor, insertion_query, rows_to_insert)

connection.commit()
