

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
import json

load_dotenv()

TITANIC_DB_NAME = os.getenv("TITANIC_DB_NAME")
TITANIC_DB_PW = os.getenv("TITANIC_DB_PW")
TITANIC_DB_HOST = os.getenv("TITANIC_DB_HOST")
TITANIC_DB_USER = os.getenv(TITANIC_"DB_USER")


### Connect to ElephantSQL-hosted PostgreSQL

conn = psycopg2.connect(dbname=TITANIC_DB_NAME, user=TITANIC_DB_USER,
                        password=TITANIC_DB_PW, host=TITANIC_DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries

cur = conn.cursor()

import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as f:
# Notice that we don't need the `csv` module.
next(f) # Skip the header row.
cur.copy_from(f, 'users', sep=',')
conn.commit()