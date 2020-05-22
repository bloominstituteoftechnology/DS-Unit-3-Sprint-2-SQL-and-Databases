# app/elephant_queries.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME", defaults="OOPS")
DB_USER = os.getenv("DB_USER", defaults="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", defaults="OOPS")
DB_HOST = os.getenv("DB_HOST", defaults="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

# Use this configuration to refer to the rows as dictionaries
# cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)