# GOAL: insert titanic.csv file into a table in PG db

import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import pandas
import numpy as np

# to get over errors about not being able to work with the numpy integer datatypes
# could alternatively change the datatypes of our dataframe,
# ... or do transformations on our list of tuples later (after reading from the dataframe, before inserting into the table)
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# adds the contents of the .env file to our environment
# looking in the .env file for env vars
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#
# CONNECT TO THE DB!
#

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

#
# MAKE A TABLE!
#
# columns: Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
cursor.execute(table_creation_query)

#
# READ THE CSV FILE! AND MAYBE TRANSFORM THE DATA
#

df = pandas.read_csv('C:/Users/dougcohen/Repos/Unit-3/DS-Unit-3-Sprint-2-SQL-and-\
Databases/module2-sql-for-analysis/titanic.csv')
print(df.head())

#
# INSERT DATA INTO THE TABLE
#
#rows_to_insert = [
#    ('A rowwwww', 'null'),
#    ('Another row, with JSONNNNN', json.dumps(my_dict))
#] # list of tuples
#
# convert df into a list of tuples

# h/t: https://kite.com/python/answers/how-to-convert-a-pandas-dataframe-into-a-list-of-tuples-in-python
rows_to_insert = list(df.to_records(index=False))

#def converted(row):
#    return ()
#rows_to_insert = [converted(row) for row in rows_to_insert]

insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)


# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
connection.commit()