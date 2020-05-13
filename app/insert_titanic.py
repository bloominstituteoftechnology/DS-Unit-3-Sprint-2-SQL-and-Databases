# app/insert_titanic.py

# connect to the db
# make a table
# read the csv file, transform the data
#insert data into the table

import os
import json
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
load_dotenv()
import pandas as pd
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

#1 connect to the db
#Postgre connection

RPGE_NAME = os.getenv("RPGE_NAME")
RPGE_USER = os.getenv("RPGE_USER")
RPGE_PASSWORD = os.getenv("RPGE_PASSWORD")
RPGE_HOST = os.getenv("RPGE_HOST")

pg_connection = psycopg2.connect(dbname=RPGE_NAME, user=RPGE_USER, password=RPGE_PASSWORD, host=RPGE_HOST)
#print("CONNECTION:", pg_connection)

pg_cursor = pg_connection.cursor()
#print("CURSOR:", pg_cursor)

# titanic csv filepath

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")

#2 make a table

# creating a new table

create_table = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers(
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR NOT NULL,
    gender VARCHAR NOT NULL,
    age FLOAT,
    sib_spouse_count INT,
    parent_child_count INT,
    fare FLOAT
);
"""

pg_cursor.execute(create_table)
pg_connection.commit()

# read the csv file, transform the data

df = pd.read_csv(CSV_FILEPATH)
#print(df.head())

#insert data into the table


insert = """
INSERT INTO passengers
(survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare)
VALUES %s
"""
rows_to_insert =  df.to_records(index=False)

execute_values(pg_cursor, insert, rows_to_insert)