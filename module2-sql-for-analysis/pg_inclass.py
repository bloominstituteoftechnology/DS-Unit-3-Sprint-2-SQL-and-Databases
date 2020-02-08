import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cur.fetchall()
print(results)

for row in results:
    print(row)