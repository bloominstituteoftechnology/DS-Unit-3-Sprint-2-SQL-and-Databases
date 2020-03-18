import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env vars, add them to the env

DB_NAME = os.getenv('DB_NAME', default='OOPS')
DB_USER = os.getenv('DB_USER', default='OOPS')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='OOPS')
DB_HOST = os.getenv('DB_HOST', default='OOPS')

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST)
print("CONNECTION: ", conn)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print('CURSOR: ', cur)


### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchone()
print('RESULT: ', result)