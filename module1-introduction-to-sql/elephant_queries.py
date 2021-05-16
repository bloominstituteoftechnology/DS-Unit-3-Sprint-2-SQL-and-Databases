
import os
from dotenv import load_dotenv
import psycopg2


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()
print("CONNECTION", connection)

cursor.execute('SELECT * from test_table;')
print("CURSOR", cursor)

result = cursor.fetchall()
print(result)
