import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import json

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchall()
print(result)

print("---------------")
query = f'''
CREATE TABLE IF NOT EXISTS test_table2 (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
'''
print('SQL:', query)
cur.execute(query)

my_dict = {'a':1, 'b':['dog','cat',42], 'c':'true'}

insertion_query = 'INSERT INTO test_table2 (name, data) VALUES %s'
execute_values( cur, insertion_query, [
    ('A rowwwww', 'null'),
    ('Another row with JSON', json.dumps(my_dict)),
    ('Third row', '3')
])



# cur.execute(insertion_query, ('A rowwwwww', 'null'))

# cur.execute(insertion_query, ('Another row, with JSONNNNN', json.dumps(my_dict)))

conn.commit()

cur.close()
conn.close()