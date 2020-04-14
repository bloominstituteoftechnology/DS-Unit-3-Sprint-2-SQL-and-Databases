# /elephant_queries.py
import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values 
# adds the contents of the .env file to our environment
# looking in the .env file for env vars
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

#insertion_query = """
#INSERT INTO test_table (name, data) VALUES
#('A row name', null),
#('Another row, with JSON', '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB);
#"""
#cursor.execute(insertion_query)

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }
#insertion_query = "INSERT INTO test_table (name, data) VALUES (%s, %s)"
#cursor.execute(insertion_query,
#  ('A rowwwww', 'null')
#)
#cursor.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))
#)

rows_to_insert = [
    ('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict))
] # list of tuples

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

cursor.execute("SELECT * from test_table;")
#first_result = cursor.fetchone()
#print(first_result)
print("--------")
all_results = cursor.fetchall()
print(all_results)

# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
connection.commit()