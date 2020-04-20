

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



- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.




conn.commit()
cur.close()
conn.close()


