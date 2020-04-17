import os
import psycopg2
import json
from dotenv import load_dotenv
from psycopg2.extras import execute_values 

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)


my_dict = {"a": 1, "b": ["dog", "cat", 42], "c": 'true'}

# insertion_query = "INSERT INTO test_table (name, data) VALUES (%s, %s)"
# cursor.execute(insertion_query, 
#     ('A rowww', 'null')
# )

# cursor.execute(insertion_query, 
#     ('Another rowww, with JSON', json.dumps(my_dict))
# )

rows_to_insert =[
    ('A rowww', 'null'),
    ('Another row, with JSON', json.dumps(my_dict))
] # list of tuples 


insertion_query = f"INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)



cursor.execute('SELECT * from test_table;')
print("-----------------")
all_results = cursor.fetchall()
print(all_result)

# actuall save the transactions 
# if creating tables or inserting data (changing db)

connection.commit()