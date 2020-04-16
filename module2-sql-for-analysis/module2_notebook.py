# module2-sql-for-analysis/module2_notebook.py

import os
from dotenv import load_dotenv
import psycopg2

# pipenv install psycopg2-binary

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("pujosgiv")
DB_USER = os.getenv("pujosgiv")
DB_PASSWORD = os.getenv("")
DB_HOST = os.getenv("drona.db.elephantsql.com")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

create_table_statement = '''
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
'''

# insert_statement = '''
# INSERT INTO test_table (name, data) VALUES
# (
#   'A row name',
#   null
# ),
# (
#   'Another row, with JSON',
#   '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
# );
# '''

# cursor.executemany(create_table_statement)
# cursor.commit()

# cursor.execute(create_table_statement)
# cursor.fetchone()

# cursor = connection.cursor()
# print("CURSOR:", cursor)

# cursor.execute('SELECT * from test_table;')
# result = cursor.fetchall()
# print("RESULT:", type(result))
# print(result)

# connection