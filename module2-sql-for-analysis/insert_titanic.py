import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

TITANIC_NAME = os.getenv("TITANIC_NAME")
TITANIC_USER = os.getenv("TITANIC_USER")
TITANIC_PASS = os.getenv("TITANIC_PASS")
pghost = os.getenv("pghost")

conn = psycopg2.connect(
    dbname=TITANIC_NAME,
    user=TITANIC_USER,
    password=TITANIC_PASS,
    host=pghost
    )
cur = conn.cursor()

# Create the table titanic in postgres
query = """
    CREATE TABLE titanic(
        survived integer,
        pclass integer,
        name text,
        sex text,
        age NUMERIC(3,1),
        siblings_spouses_aboard integer,
        parents_children_aboard integer,
        fare NUMERIC(7,4)
    )
"""
cur.execute(query)
conn.commit()


with open('titanic.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'titanic', sep=',')
conn.commit()