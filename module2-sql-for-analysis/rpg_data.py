import psycopg2
import os
import sqlite3
# linting doesn't like this line, but working fine.
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)
print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)
#note slightly diff syntax here - psycopg2 is picky
cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)
