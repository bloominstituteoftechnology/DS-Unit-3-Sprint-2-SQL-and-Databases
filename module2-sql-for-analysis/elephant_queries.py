

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
import json



load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_PW = os.getenv("DB_PW")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")



### Connect to ElephantSQL-hosted PostgreSQL

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)


### A "cursor", a structure to iterate over db records to perform queries

cur = conn.cursor()

## An example query
result1 = cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result2 = cur.fetchall()

print(result1)
print("--------")
print(result2)
print("--------")


#functional approach to inserting data:

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

rows_to_insert = [
        ('A row', 'null'),
        ('Another row, with JSON', json.dumps(my_dict))
]

# the %$ is a placeholder that gets carried out in the execute_values
# positionally? so in this case %$ gets replaced by "rows_to_insert",
# if we were to insert more than one variable we would need another %$

insertion_query = "INSERT INTO test_table (name, data) VALUES %s"

execute_values(cur, insertion_query, rows_to_insert)

# OOP approach to inserting data: 

# insertion_query = f"INSERT INTO test_table (name, data) VALUES %s, %s)"

# cur.execute(insertion_query,
#  ('A rowwwww', 'null')
# )
# cur.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))


# ACTUALLY SAVE THE TRANSACTIONS

conn.commit()

cur.close()
conn.close()