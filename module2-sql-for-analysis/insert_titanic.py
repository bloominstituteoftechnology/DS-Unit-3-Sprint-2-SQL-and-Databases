!pip install psycopg2-binary
import psycopg2
import pandas as pd

# import dataset
df = pd.read_csv('titanic.csv')

# replace apostraphes with accent (this becomes a problem later)
df['Name'] = df['Name'].str.replace("'", '`')

# PostgreSQL server information
dbname = 'rbdyjzel'
user = 'rbdyjzel'
password = 'PqamaH9-y5MGtTxPP__tkNvls9Nj0WWQ' # Don't commit this!
host = 'raja.db.elephantsql.com'

# Connect to PostgreSQL
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()


# Transform Pandas Dataframe into SQL
import sqlite3
# Convert to SQLite3
sl_conn = sqlite3.connect('titanic.sqlite3')
df.to_sql(name='titanic', con=sl_conn, if_exists='replace')
sl_curs = sl_conn.cursor()

create_titanic_table = """
CREATE TABLE titanic (
  id SERIAL PRIMARY KEY,
  survived INT,
  pclass INT,
  name VARCHAR(100),
  sex VARCHAR(10),
  age INT,
  siblings_or_spouses_aboard INT,
  parents_children_aboard INT,
  fare FLOAT
)
"""
# Creates table on PostgreSQL server
pg_curs.execute(create_titanic_table)

# Inserts values from local sqlite table to postgreSQL server
attempted_insert = """
  INSERT INTO titanic
  VALUES""" + str(human[0])
attempted_insert

# Attempt to insert first line of data into PostgreSQL server
pg_curs.execute(attempted_insert)

# inserting the rest of the table
for humans in human[1:]:
    insert_human = """
    INSERT INTO titanic
    VALUES """ + str(humans)
    pg_curs.execute(insert_human)
pg_conn.commit()

