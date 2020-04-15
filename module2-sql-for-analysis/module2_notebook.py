import os
from dotenv import load_dotenv
import psycopg2

# pipenv install psycopg2-binary

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = "pujosgiv"
DB_USER = "pujosgiv"
<<<<<<< HEAD
DB_PASSWORD = ""
=======
DB_PASSWORD = "***REMOVED***"
>>>>>>> cedd2009ed0ca6cc203939c93b5d606f605bff42
DB_HOST = "drona.db.elephantsql.com"

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

create_table_statement = '''
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
'''

# cursor = connection.cursor()
# print("CURSOR:", cursor)

# cursor.execute('SELECT * from test_table;')
# result = cursor.fetchall()
# print("RESULT:", type(result))
# print(result)

# connection