import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# Create table
query = """
CREATE TABLE IF NOT EXISTS titanic (
    survived integer,
    pclass integer,
    name varchar,
    sex varchar,
    age float8,
    sib_spouse_count integer,
    parent_child_count integer,
    fare float8
);
"""

# Write data
cursor.execute(query)
f = open(r"titanic.csv", "r")
next(f)
cursor.copy_from(f, "titanic", sep = ",", null = "")
f.close()

# Add ID to table (best way?)
query = "ALTER TABLE titanic ADD COLUMN id SERIAL PRIMARY KEY"
cursor.execute(query)

connection.commit()
