# app/elephant_queries.py

import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

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