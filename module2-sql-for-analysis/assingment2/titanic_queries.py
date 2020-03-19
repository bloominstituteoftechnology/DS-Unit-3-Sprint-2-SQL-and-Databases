import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values

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


# TABLE CREATION

titanic_creation_query = '''
CREATE TABLE IF NOT EXISTS titanic (
  id SERIAL PRIMARY KEY,
  survived BOOL,
  pclass INT,
  name varchar,
  sex varchar,
  age INT,
  sib_spouse_count INT,
  parents_children_aboard INT,
  fare FLOAT8
);
'''
cursor.execute(titanic_creation_query)

# Test query
cursor.execute('SELECT * from titanic;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result2 = cursor.fetchall()
print('TITANIC: ', len(result2))

# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()
