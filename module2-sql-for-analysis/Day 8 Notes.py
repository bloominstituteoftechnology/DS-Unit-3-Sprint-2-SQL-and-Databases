
# EXAMPLE OF inserting csv file into postgresql


import pandas as pd
import psycopg2
import json
import os
import sqlite3
from psycopg2.extras import execute_values
from dotenv import load_dotenv
!pip install psycopg2-binary
!pip install python-dotenv
load_dotenv()  # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)
# create postgress cursor
pc = connection.cursor()
# Pull the titanic csv from github
df = pd.read_csv('https://raw.githubusercontent.com/iesous-kurios/'
                 'DS-Unit-3-Sprint-2-SQL-and-Databases/master/'
                 'module2-sql-for-analysis/titanic.csv')
# replace ' with " " and use regex to pull info
df = df.replace("'", " ", regex=True)
#  Establish the connection
sql_conn = sqlite3.connect('titanic.sqlite3')
# create sqlite specific cursor
sql_curs = sql_conn.cursor()
# insert the data into a new table called "titanic" in the database
df.to_sql(name='titanic', con=sql_conn)
# Execute command from cursor to count how many rows in the table
sql_curs.execute('SELECT COUNT (*) FROM titanic;').fetchall()
# assign passengers from database into variable
passengers = sql_curs.execute('SELECT * FROM titanic;').fetchall()
# Used the following code to get the schema:
# sl_curs.execute('PRAGMA table_info(titanic);').fetchall()
# Change the types to import into postgres
create_blank_titanic_table = """
  CREATE TABLE titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(90),
    sex VARCHAR(10),
    age FLOAT,
    siblings_spouses_aboard INT,
    parents_children INT,
    fare FLOAT
  );
"""
# create empty table called titanic in elephantSQL
pc.execute(create_blank_titanic_table)
# remove id and perform slice before moving into postgres
str(passengers[1][1:])
# insert all passengers from sqlite3 to elephantSQL
for index, row in df.iterrows():
    insert_record = """
        INSERT INTO titanic
        (survived, pclass, name, sex, age, siblings_spouses_aboard,
        parents_children, fare)
        VALUES """ + str(tuple(row.values)) + ';'
    pc.execute(insert_record)
pc.execute('SELECT * FROM titanic;')
pc.fetchall()
pc.close()
connection.commit()

#OTHER EXAMPLE:

#--------------------------------------------------------------------------------------------------------------------------------------------#


# GOAL: insert titanic.csv file into a table in PG db
​
import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import pandas
​
# adds the contents of the .env file to our environment
# looking in the .env file for env vars
load_dotenv()
​
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
​
#
# CONNECT TO THE DB!
#
​
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>
​
cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>
​
#
# MAKE A TABLE!
#
# columns: Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare
​
table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived bool,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
# READ THE CSV FILE! AND MAYBE TRANSFORM THE DATA
#
​
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
​
df = pandas.read_csv(CSV_FILEPATH)
print(df.head())
​
#
# INSERT DATA INTO THE TABLE
#
#rows_to_insert = [
#    ('A rowwwww', 'null'),
#    ('Another row, with JSONNNNN', json.dumps(my_dict))
#] # list of tuples
#
# convert df into a list of tuples
​
# h/t: https://kite.com/python/answers/how-to-convert-a-pandas-dataframe-into-a-list-of-tuples-in-python
rows_to_insert = list(df.to_records(index=False))
​
#def converted(row):
#    return ()
#rows_to_insert = [converted(row) for row in rows_to_insert]
​
​
​
​
insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)
​
​
# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
