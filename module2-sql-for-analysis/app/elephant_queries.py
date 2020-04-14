import os
import psycopg2
from dotenv import load_dotenv

# adds contents of the .env file to our enviornment
# looking in the .env file for env variables
load_dotenv()

### Connect to ElephantSQL-hosted PostgreSQL

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print(type(conn))

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print(type(cur))

### An example query
cur.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cur.fetchone()
print(results)