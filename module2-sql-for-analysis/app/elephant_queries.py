import os
import psycopg2
import json
from dotenv import load_dotenv
from psycopg2.extras import execute_values

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


#
# INSERT SOME DATA
#

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

# insertion_query = f"INSERT INTO test_table (name, data) VALUES (%s, %s)"
# cur.execute(insertion_query,
#  ('A rowwwww', 'null')
# )
# cur.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))
# )

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = f"INSERT INTO test_table (name, data) VALUES %s"
execute_values(cur, insertion_query, [
 ('A rowwwww', 'null'),
 ('Another row, with JSONNNNN', json.dumps(my_dict)),
 ('Third row', "3")
])


### An example query
cur.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
print('----------')
results = cur.fetchall()
print(results)

# ACTUALLY SAVE THE TRANSACTIONS
conn.commit()