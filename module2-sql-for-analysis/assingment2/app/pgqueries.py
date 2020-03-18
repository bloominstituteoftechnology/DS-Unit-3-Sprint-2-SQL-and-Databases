import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() # look in the .env file for env vars, add them to the env

DB_NAME = os.getenv('DB_NAME', default='OOPS')
DB_USER = os.getenv('DB_USER', default='OOPS')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='OOPS')
DB_HOST = os.getenv('DB_HOST', default='OOPS')

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST)
print("CONNECTION: ", connection)

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print('CURSOR: ', cursor)

#
### TABLE CREATION
#
# query = '''
# CREATE TABLE test_table (
#   id        SERIAL PRIMARY KEY,
#   name  varchar(40) NOT NULL,
#   data    JSONB
# );
# '''
# cursor.execute(query)

# Test query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
print('RESULT: ', len(result))

#
### DATA INSERTION
#

insertion_query = '''
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
'''

cursor.execute(insertion_query)

# Test query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
print('RESULT: ', len(result))

# ACTUALLY SAVE THE TRANSACTIONS ACCORDING TO MIKE
connection.commit()