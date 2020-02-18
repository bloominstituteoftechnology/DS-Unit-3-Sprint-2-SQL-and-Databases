"""Remotely access POstgreSql database"""

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

print('QUERYING THE DATABASE')

connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
)

print('Connection:', connection)

cursor = connection.cursor()
print('Cursor:', cursor)

# query = """
# INSERT INTO test_table (name, data) VALUES
# (
#   'Hi There',
#   '{"DS11": "yay", "Unit3": "yay again"}'
# );
# """

query = """
SELECT * FROM test_table
"""

cursor.execute(query)
# connection.commit()
result = cursor.fetchall()
print('Result:', type(result))
print(result)
