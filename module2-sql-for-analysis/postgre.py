import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("dbname"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host")
)
# A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
# An example query
cur.execute('SELECT * from test_table;')
# Note - nothing happened yet! We need to actually *fetch* from the cursor
print(cur.fetchone())
