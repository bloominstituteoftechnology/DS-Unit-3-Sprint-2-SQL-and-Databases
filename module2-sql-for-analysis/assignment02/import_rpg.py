import os
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

# Connection details for the sqlite3 database
DB_FILEPATH = "../../module1-introduction-to-sql/rpg_db.sqlite3"
DB_SLT_TABLE = "charactercreator_character"

# Connection details for the Postgres database
DB_PG_HOST = os.getenv("DB_PG_HOST", default="missing")
DB_PG_NAME = os.getenv("DB_PG_NAME", default="missing")
DB_PG_USER = os.getenv("DB_PG_USER", default="missing")
DB_PG_PASSWORD = os.getenv("DB_PG_PASSWORD", default="missing")

conn = sqlite3.connect(DB_FILEPATH)

# Test that have connected to the database
rslts = conn.execute("SELECT 1").fetchall()

# Test the sqlite connection
if rslts[0][0] == 1:
    print(f'\nYou have connected successfully to {DB_FILEPATH}\n')
else:
    print(f'A connection error occurred\n')
    quit()

# Read a sqlite database table into a python object
csr = conn.cursor()                         # Create a cursor object
query = f'SELECT * FROM {DB_SLT_TABLE}'     # Define a query string 
csr.execute(query)                          # Execute the query
rows = csr.fetchall()                       # Fetch all of the rows from the query

# Connect to the Postgres database
conn_pg = psycopg2.connect(
    dbname=DB_PG_NAME, 
    user=DB_PG_USER, 
    password=DB_PG_PASSWORD, 
    host=DB_PG_HOST)

# Test that have connected to the database
query_pg = f'SELECT 1'
csr_pg = conn_pg.cursor()
rslts = conn_pg.execute("SELECT 1").fetchall()

# Test the sqlite connection
if rslts[0][0] == 1:
    print(f'\nYou have connected successfully to {DB_PG_HOST} > {DB_PG_NAME}\n')
else:
    print(f'A connection error occurred\n')
    quit()

PG_DROP_TABLE = "DROP TABLE charactercreator_character"
PG_CREATE_TABLE = """
CREATE TABLE charactercreator_character (
  character_id serial NOT NULL,
  "name" varchar(30) NOT NULL,
  "level" integer NOT NULL, 
  "exp" integer NOT NULL, 
  "hp" integer NOT NULL, 
  "strength" integer NOT NULL, 
  "intelligence" integer NOT NULL, 
  "dexterity" integer NOT NULL, 
  "wisdom" integer NOT NULL,
  PRIMARY KEY (character_id)
);
"""

# Connect to the Postgres database

csr_pg = conn_pg.cursor()



