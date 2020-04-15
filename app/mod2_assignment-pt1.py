import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import glob

load_dotenv()  # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_SAFEWORD")
DB_PORT = os.getenv("DB_PORT")

connection = psycopg2.connect(dbname=DB_NAME,
                              user=DB_USER,
                              password=DB_PASSWORD,
                              host=DB_HOST)
cursor = connection.cursor()
cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()


def finalize() -> None:
    connection.commit()
