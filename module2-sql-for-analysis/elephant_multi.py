import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

print("-------------------")
query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall()[0:10]:
    print(row)



#
# CREATE THE TABLE
#

table_name = "test_table2"

print("-------------------")
query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
print("SQL:", query)
cursor.execute(query)

#
# INSERT SOME DATA
#

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

#insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
#cursor.execute(insertion_query,
#  ('A rowwwww', 'null')
#)
#cursor.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))
#)

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
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
# QUERY THE TABLE
#

print("-------------------")
query = f"SELECT * FROM {table_name};"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()

cursor.close()
connection.close()