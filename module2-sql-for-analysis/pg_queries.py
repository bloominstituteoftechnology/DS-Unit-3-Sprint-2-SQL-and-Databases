import psycopg2
import os
from dotenv import load_dotenv


load_dotenv() 


DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()
cur.execute('SELECT * from test_table;')
cur.fetchone()