import psycopg2
from psycopg2.extras import execute_values
import json
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv() # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASS = os.getenv("DB_PASS", default="OOPS")
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST
)
cursor = connection.cursor()
#
#
#
print("------------")
#insert_query = """
#INSERT INTO test_table (name, data) VALUES
#(
#  'A row name',
#  null
#),
#(
#  'Another row, with JSON',
#  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
#);
#"""
#print(insert_query)
#cursor.execute(insert_query)
my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }
table_name = "test_table"
#insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
#cursor.execute(insertion_query,
#  ('A rowwwww', 'null')
#)
#cursor.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))
#)
#print(insertion_query)
#cursor.execute(insertion_query)
insertion_query = f"INSERT INTO {table_name} (name, data) VALUES %s"
#execute_values(cursor, insertion_query, [
#  ('A rowwwww', 'null'),
#  ('Another row, with JSONNNNN', json.dumps(my_dict)),
#  ('Third row', "3")
#])
df = pd.DataFrame([
  ['A rowwwww', 'null'],
  ['Another row, with JSONNNNN', json.dumps(my_dict)],
  ['Third row', "null"],
  ["Pandas Row", "null"]
])
records = df.to_dict("records") #> [{0: 'A rowwwww', 1: 'null'}, {0: 'Another row, with JSONNNNN', 1: '{"a": 1, "b": ["dog", "cat", 42], "c": "true"}'}, {0: 'Third row', 1: '3'}, {0: 'Pandas Row', 1: 'YOOO!'}]
list_of_tuples = [(r[0], r[1]) for r in records]
execute_values(cursor, insertion_query, list_of_tuples)
#
#
#
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