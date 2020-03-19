import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import pandas as pd

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
  survived INT,
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

if len(result2) == 0:
# the next line is a more robust way to do it than just a string with filepath
# because path.join recognizes what os you're on and makes the slashes go
# the right way. / on mac, \ on windows. You can also be in a different
# directory (like if I actually organized this repo well) and it would still work.
    CSV_FILEPATH = os.path.join(os.path.dirname(__file__),'titanic.csv')
    print('FILE EXISTS:', os.path.isfile(CSV_FILEPATH))
    df = pd.read_csv(CSV_FILEPATH)
    print(df.head())

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
# this gets us our list of tuples. Pandas ftw
rows = list(df.itertuples(index=False, name=None))


insertion_query = "INSERT INTO titanic (survived, pclass, name, sex, age, sib_spouse_count, parents_children_aboard, fare) VALUES %s"
execute_values(cursor, insertion_query, rows)



# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()
