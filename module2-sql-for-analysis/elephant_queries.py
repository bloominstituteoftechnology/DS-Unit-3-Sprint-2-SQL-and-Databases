

import psycopg2
import dotenv

DB_NAME = os.getenv("DB_NAME")
DB_PW = os.getenv("DB_PW")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")

load_dotenv()

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)


### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
result1 = cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result2 = cur.fetchone()

print(result1)
print(result2)

