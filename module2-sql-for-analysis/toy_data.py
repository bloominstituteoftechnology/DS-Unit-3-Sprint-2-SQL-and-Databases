"""set up a new table for the Titanic data """
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv() # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

conn= psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)

# # A "cursor", a structure to iterate over db record to perform queries
cur = conn.cursor()

# ### An example query
cur.execute ('SELECT * from test_table;')

# # fetch the query
result = cur.fetchall()
print(result)
for row in results:
    print(row)


print("------------")
insert_query = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""
print(insert_query)
cursor.execute(insert_query)

print("------------")
query = "SELECT * from test_table;"
print(query)
cursor.execute(query)
#results = cursor.fetchone()
results = cursor.fetchall()
#print(results)
for row in results:
    print(row)
# committing the transaction:
connection.commit()

