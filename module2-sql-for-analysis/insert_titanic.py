import csv
import sqlite3
import psycopg2
import credentials
import pandas as pd
from sqlalchemy import create_engine

# Create a postgres db on sqelephant using SQL Alchemy and pandas
df = pd.read_csv('titanic.csv')
engine = create_engine('postgres://dqsrsnzf:d6ciiKCSJSRR4a-jqmd8ecVF5m4VGNZc@isilo.db.elephantsql.com:5432/dqsrsnzf')
df.to_sql('titanic_table', engine)

# Use psychopig and sqlite query all the rows
# Credentials are in a separate file, Credentials.py
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic_table;')
print("Titanic table worked, here's the number of rows:", len(pg_curs.fetchall()))

# Create enum type for sex
# pg_curs.execute("CREATE TYPE sex_binary AS ENUM ('male', 'female');")

# Create another table with a schema using psychopig
# should add primary key in the future
pg_curs.execute("""
    CREATE TABLE another_titanic(
    Survived bytea,
    Pclass smallint,
    Name varchar(100),
    Sex sex_binary,
    Age decimal,
    Siblings_Spouses_Abroad smallint,
    Parents_Children_Abroad smallint,
    Fare decimal)
""")

# Load the csv into table
with open('titanic.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        pg_curs.execute(
            "INSERT INTO another_titanic VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

pg_conn.commit()

pg_curs.execute('SELECT * FROM another_titanic;')
print("Another_titanic table worked, here's the number of rows:", len(pg_curs.fetchall()))
