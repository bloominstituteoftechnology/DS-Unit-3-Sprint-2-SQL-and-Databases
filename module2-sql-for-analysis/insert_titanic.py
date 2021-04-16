# insert_titanic.py


# Imports

import os
import csv
import sqlite3
import psycopg2
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load titanic from path

titanic = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(titanic)


# Wrangle df to avoid problems in csv to sql conversion

df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')
df.Name = df.Name.str.replace("'", " ")


# Check df shape and null values

print(df.shape)
print(df.isnull().sum())


# Create sql engine and convert csv to sql

engine = create_engine('sqlite://', echo=False)
df.to_sql('titanic', con=engine)


# Load credentials for ElephantSQL

load_dotenv()
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")


# Connect to ElephantSQL server

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)


# Create SQL cursor

cursor = connection.cursor()
print("CURSOR:", cursor)


# Create titanic table

create_titanic_table = """
CREATE TABLE titanic(
    id SERIAL PRIMARY KEY,
    survived INT,
    p_class INT,
    name VARCHAR(100),
    sex VARCHAR(100),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare FLOAT
);"""

cursor.execute(create_titanic_table)


# Update the titanic data to avoid error in query below

engine.execute("""
UPDATE titanic SET name = REPLACE(name, "'", " ");
""")


# Query for passengers

passengers = engine.execute('SELECT * from titanic;').fetchall()


# For loop to insert passengers into titanic table

for passenger in passengers[1:]:
    insert_passenger = """
        INSERT INTO titanic
        VALUES""" + str(passenger) + ";"
    cursor.execute(insert_passenger)


# Commit the data so the changes to the table persist

connection.commit()


# Close the cursor and connection

cursor.close()
