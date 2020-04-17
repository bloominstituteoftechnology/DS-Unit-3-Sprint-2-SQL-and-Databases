# Goal is to insert titanic.csv into a table in a postgres database
import psycopg2
import os
import json
from psycopg2.extras import execute_values
import pandas as pd 
import numpy as np

# to get over errors about not being able to work with the numpy integer datatypes
# could alternatively change the datatypes of our dataframe,
# ... or do transformations on our list of tuples later (after reading from the dataframe, before inserting into the table)
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# Connect to DB
DBNAME = 'rsswtvhb'
DBUSER = "rsswtvhb"
DB_PASS = "qImj0x6_ofnmgQYeEY9VD2q-93dNW1pt"
DB_HOST = 'drona.db.elephantsql.com'

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DBNAME, user=DBUSER,
                        password=DB_PASS, 
                        host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()


# Make a table
table_name = 'passengers'
table_creation_query = f"""
DROP TABLE IF EXISTS {table_name};
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived bool,
    pclass integer,
    name varchar NOT NULL,
    gender VARCHAR NOT NULL,
    age float,
    sib_spouse_count integer,
    parents_children integer,
    fare float
);

"""

cursor.execute(table_creation_query)

# Read the CSV file and maybe wrangle data
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv" )
df = pd.read_csv(CSV_FILEPATH)

df.dtypes

# cast the survived column as a boolean.  
# need to use strings because psycopg2 can't handle numpy.bool values
# alternative would be to cast as a np.bool but this is easier
df['Survived'] = df['Survived'].replace({0:'False', 1:'True'})

# convert dataframe rows to a list of tuples
row_list = list(df.to_records(index = False))


# Insert data into table

insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parents_children, fare) VALUES %s"
execute_values(cursor, insertion_query, row_list)

connection.commit()

print("done")