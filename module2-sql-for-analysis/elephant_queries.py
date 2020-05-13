import os
import psycopg2 as psyco
from dotenv import load_dotenv

load_dotenv()   # loads contents of the .env file

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PW = os.getenv("DB_PW")
DB_HOST = os.getenv("DB_HOST")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psyco.connect(dbname=DB_NAME, user=DB_USER,
        password=DB_PW, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()
for row in results:
    print(type(row), row)