import os
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

# Connection details for the sqlite3 database
DB_FILEPATH = "../../module1-introduction-to-sql/rpg_db.sqlite3"
DB_SLT_TABLE = "charactercreator_character"

# Connection details for the Postgres database
DB_PG_HOST = "localhost"
DB_PG_NAME = "lambda_dev"
DB_PG_USER = ""
DB_PG_PASSWORD = ""
print(f'{DB_PG_HOST}\n{DB_PG_NAME}\n{DB_PG_USER}\n{DB_PG_PASSWORD}\n')

# Connect to the Postgres database
conn_pg = psycopg2.connect(
    dbname=DB_PG_NAME, 
    user=DB_PG_USER, 
    password=DB_PG_PASSWORD, 
    host=DB_PG_HOST)

# Test that have connected to the database
query_pg = f'SELECT 1'
csr_pg = conn_pg.cursor()
csr_pg.execute(query_pg)
rslts_pg = csr_pg.fetchall()

# Test the sqlite connection
if rslts_pg[0][0] == 1:
    print(f'INFO: You have connected successfully to server: {DB_PG_HOST} database: {DB_PG_NAME}\n')
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
# Create the new Postgres table
csr_pg.execute(PG_CREATE_TABLE)
# Select 
csr_pg.execute("SELECT count(*) FROM charactercreator_character")
rslts_pg = csr_pg.fetchall()
print("My SELECT...", rslts_pg)

#PG_INSERT_ROW = ""
#
#execute_values(cur,
#... "INSERT INTO test (id, v1, v2) VALUES %s",
#... [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
#
#print(type(rows))



