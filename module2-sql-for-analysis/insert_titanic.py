import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import sqlite3

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME= os.getenv("DB_NAME", default="oops")
DB_USER= os.getenv("DB_USER", default="oops")
DB_PASSWORD= os.getenv("DB_PASSWORD", default="oops")
DB_HOST= os.getenv("DB_HOST", default="oops")

# COPPIED FROM ABOVE IN THE HELP SECTION EXCEPT I ADDED HOST
pg_conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) # pg means POSTGRES

# CURSOR ALLOWS US TO USE A DB
pg_curs = pg_conn.cursor()

df = pd.read_csv('DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv')
df['Name'] = df['Name'].str.replace("'", "")
df['Survived'] = df['Survived'].replace({0: False, 1: True})

df = df.to_records(index=False)
print(df)

titnic_passenger_table = """
DROP TABLE titanic_passengers;
CREATE TABLE IF NOT EXISTS titanic_passengers (
    index SERIAL PRIMARY KEY,
    survived bool,
    pclass integer,
    name text,
    sex text,
    age real,
    ssa integer,
    pca integer,
    fare real
);
"""
# pg_conn.commit()

# makes the table
pg_curs.execute(titnic_passenger_table)
print('\nTABLE CREATED\n')

print('POPULATING TABLE')
print('. . . please hold . . .')
for i in range(len(df)):
  insert_passenger_data = f"""
    INSERT INTO titanic_passengers
    (survived, pclass, name, sex, age, ssa, pca, fare)
    VALUES {df[i]}"""
  pg_curs.execute(insert_passenger_data)

# THIS WORKS!!!(must comment out line 26)
# for i in range(len(df)):
#   insert_passenger_data = f"""
#     INSERT INTO titanic_passengers
#     (survived, pclass, name, sex, age, ssa, pca, fare)
#     VALUES 
#     {tuple(df.values[i])}"""
#   pg_curs.execute(insert_passenger_data)

print('\nTABLE IS POPULATED')
print('\n')

# SEE THE TABLE
pg_curs.execute('SELECT * FROM titanic_passengers;')
see = pg_curs.fetchall()
print('BEHOLD, THE TABLE IS POPULATED\n',see)
print('\nEVERYTHING WORKED!')

# COMMIT AND CLOSE
pg_conn.commit()
pg_curs.close()
print('\nWORK COMMITED AND CONNECTION CLOSED\n')