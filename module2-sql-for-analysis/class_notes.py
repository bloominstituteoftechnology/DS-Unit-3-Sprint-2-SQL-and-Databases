import os
import json
from dotenv import load_dotenv # python-dotenv
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

# print(DB_NAME)
# print(DB_USER)
# print(DB_PASSWORD)
# print(DB_HOST)
# exit() # or quit()

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>
cursor = connection.cursor()

# print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>
# cursor.execute("SELECT * from rpg_table;") #TODO: share links related to this two step process

##results = cursor.fetchone()
#results = cursor.fetchall()
#for row in results:
#    print(type(row), row)
#
# INSERT SOME DATA
#
my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }
### sql = f"""
### INSERT INTO test_table (name, data) VALUES
### ('A row name', null),
### ('Another row, with JSON', '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB);
### """
### insertion_query = f"INSERT INTO test_table (name, data) VALUES (%s, %s)"
### cursor.execute(insertion_query,
###   ('A rowwwww', 'null')
### )
### cursor.execute(insertion_query,
###   ('Another row, with JSONNNNN', json.dumps(my_dict)) # converting dict to string
### )
# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query

#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

insertion_query = f"INSERT INTO rpg_table (item_id, name, value, weight) VALUES %s"
execute_values(cursor, insertion_query, q1) # third param: data as a list of tuples!
connection.commit() # actually save the records / run the transaction to insert rows
cursor.close()
connection.close()