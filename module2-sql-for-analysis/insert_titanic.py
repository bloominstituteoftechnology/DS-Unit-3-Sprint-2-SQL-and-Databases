# python module2-sql-for-analysis/insert_titanic.py
import os
import pandas
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
# pipenv install psycopg2-binary

load_dotenv() #> loads contents of the .env file into the script's environment

#
# CONNECT to the database
#

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

#
# CREATE the table
#

table_creation_query = '''
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passenger (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  sex varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
'''

cursor.execute(table_creation_query)

#
# COMMIT the transactions
#

connection.commit()

#
# 
#