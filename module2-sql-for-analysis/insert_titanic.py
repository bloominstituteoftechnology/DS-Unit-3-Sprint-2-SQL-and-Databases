import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import numpy as np 

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# CONNEC TO DATABASE
load_dotenv() # looks inside the .env file for some env vars
# passes env var values to python var

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_PORT =  os.getenv("DB_PORT", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

# MAME A POSTGRES SQL TABLE
# comment out drop table the first time you run
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

# READ THE CSV AND TRANSFORM THE DATA 
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "data", "titanic.csv")

df = pd.read_csv(CSV_FILEPATH)
# print(df.head())

# INSERT THE DATA INTO THE TABLE
rows_to_insert = list(df.to_records(index=False)

insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

# SAVE THE TRANSACTIONS
connection.commit()