import psycopg2
import os
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME', default='Check env variables')
DB_USER = os.getenv('DB_USER', default='Check env variables')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='Check env variables')
DB_HOST = os.getenv('DB_HOST', default='Check env variables')

connection = psycopg2.connect(dbname = DB_NAME, user = DB_USER,
                                password = DB_PASSWORD, host = DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)