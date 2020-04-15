import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()


DB_NAME = os.getenv("DB_NAME_DB13_Unit3")
DB_USER = os.getenv("DB_USER__DB13_Unit3")
DB_PASSWORD = os.getenv("DB_PASSWORD__DB13_Unit3")
DB_HOST = os.getenv("DB_HOST__DB13_Unit3")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)


# create the table for using the columns from the titanic dataset
table_name = "test_table2"

query = """
  CREATE TABLE IF NOT EXISTS table_name(
    id SERIAL PRIMARY KEY,
    Survived BOOLEAN,
    Pclass INTEGER CHECK (Pclass > 0 AND Pclass <= 3 ),
    Name VARCHAR(100),
    Sex VARCHAR(10) CHECK (Sex in ('male', 'female')),
    Age FLOAT(8),
    Sibilings_Spouses_Aboard INTEGER,
    Parents_Children_Aboard INTEGER,
    Fare FLOAT(8)
  );
  """
