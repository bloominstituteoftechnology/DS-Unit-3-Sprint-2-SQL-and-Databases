

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
import json

load_dotenv()

TITANIC_DB_NAME = os.getenv("TITANIC_DB_NAME")
TITANIC_DB_PW = os.getenv("TITANIC_DB_PW")
TITANIC_DB_HOST = os.getenv("TITANIC_DB_HOST")
TITANIC_DB_USER = os.getenv("TITANIC_DB_USER")






### Connect to ElephantSQL-hosted PostgreSQL

conn = psycopg2.connect(dbname=TITANIC_DB_NAME, user=TITANIC_DB_USER,
                        password=TITANIC_DB_PW, host=TITANIC_DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries

cur = conn.cursor()

titanic_csv = os.path.join(os.path.dirname(__file__), 'titanic.csv')

with open(titanic_csv, 'r') as titanic:
    next(titanic)
    cur.copy_from(titanic, 'titable', sep=',')

conn.commit()
cur.close()
conn.close()


