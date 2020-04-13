import os
import sys
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

# Connection details for the sqlite3 database
DB_FILEPATH = "../../module1-introduction-to-sql/rpg_db.sqlite3"
DB_SLT_TABLE = "charactercreator_character"

# Connection details for the Postgres database
DB_PG_HOST = os.getenv("DB_PG_HOST", default="missing")
DB_PG_DBNAME = os.getenv("DB_PG_DBNAME", default="missing")
DB_PG_USER = os.getenv("DB_PG_USER", default="missing")
DB_PG_PASSWORD = os.getenv("DB_PG_PASSWORD", default="missing")
print(f'{DB_PG_HOST}\n{DB_PG_DBNAME}\n{DB_PG_USER}\n{DB_PG_PASSWORD}\n')

# Connect to the sqlite3 database
conn_sl = sqlite3.connect(DB_FILEPATH)

# Test that the script has connected to the sqlite3 database
rslts_sl = conn_sl.execute("SELECT 1").fetchall()

# Test the sqlite connection
if rslts_sl[0][0] == 1:
    print(f'\nINFO: You have connected successfully to {DB_FILEPATH}\n')
else:
    print(f'ERROR: A connection error occurred\n')
    quit()

# Read a sqlite database table into a python object
csr_sl = conn_sl.cursor()                   # Create a cursor object
query_sl = f'SELECT * FROM {DB_SLT_TABLE}'  # Define a query string 
csr_sl.execute(query_sl)                    # Execute the query
rows = csr_sl.fetchall()                    # Fetch all of the rows from the query

# Connect to the Postgres database
conn_pg = psycopg2.connect(
    dbname=DB_PG_DBNAME, 
    user=DB_PG_USER, 
    password=DB_PG_PASSWORD, 
    host=DB_PG_HOST)

# Test that have connected to the database
query_pg = f'SELECT 1'
csr_pg = conn_pg.cursor()
csr_pg.execute(query_pg)
rslts_pg = csr_pg.fetchall()

# Test the Postgres connection
if rslts_pg[0][0] == 1:
    print(f'INFO: You have connected successfully to server: {DB_PG_HOST} database: {DB_PG_DBNAME}\n')
else:
    print(f'ERROR: A connection error occurred\n')
    quit()

PG_DROP_TABLE = "DROP TABLE IF EXISTS charactercreator_character"
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
)
"""

# Drop the Postgres table if it exists (so we can create it)
csr_pg.execute(PG_DROP_TABLE)
conn_pg.commit()                 # commit the drop transaction

# Create the new Postgres table
csr_pg.execute(PG_CREATE_TABLE)
conn_pg.commit()                 # commit the create transaction

# execute_values insert statement
PG_INSERT = """
INSERT INTO charactercreator_character 
  (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) 
  VALUES %s;
"""

# Insert the rows exported from the sqlite database into the Postgres database table 
execute_values(
    csr_pg, 
    PG_INSERT, 
    rows)
conn_pg.commit() 

# What's the count of the newly imported rows
csr_pg.execute("SELECT count(*) FROM charactercreator_character")
rslts_pg = csr_pg.fetchone()
print(f'Number of rows in the Postgres charactercreator_character table (expecting 302): {rslts_pg[0]}')

# Close the sqlite3 and Postgres cursors
csr_sl.close()
csr_pg.close()

# Close the sqlite3 and Postgres database connections
conn_sl.close()
conn_pg.close()


