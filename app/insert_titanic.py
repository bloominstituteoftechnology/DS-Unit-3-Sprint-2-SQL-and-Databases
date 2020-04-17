#  insert the titanic.csv file into a table in PG db

import os
import psycopg2
import json
from dotenv import load_dotenv
from psycopg2.extras import execute_values 
import pandas 
import numpy as np

psycopg2.extensions.register_adapter(np.int64,psycopg2._psycopg.AsIs)

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# make a table !
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

# read csv file and transform data if possible 
CSV_FILEPATH = DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")

df = pandas.read_csv(CSV_FILEPATH)
print(df.head())

# convert df to list of tuples 
rows_to_insert = list(df.to_records(index=False))

# insert data into the table 
insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count,parent_child_count,fare) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

connection.commit()

