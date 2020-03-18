import psycopg2
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME= os.getenv("DB_NAME", default="oops")
DB_USER= os.getenv("DB_USER", default="oops")
DB_PASSWORD= os.getenv("DB_PASSWORD", default="oops")
DB_HOST= os.getenv("DB_HOST", default="oops")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

df = pd.read_csv('titanic.csv')
df['index_col'] = df.index
df['Name'] = df['Name'].str.replace("'", "")

query= """
CREATE TABLE IF NOT EXISTS titanic (
  Survived integer,
  Pclass integer,
  Name text,
  Sex text,
  Age real,
  Siblings_Spouses_Aboard integer,
  Parents_Children_Aboard integer,
  Fare real,
  index_col SERIAL PRIMARY KEY
);
"""
cursor.execute(query)

for i in range(len(df)):
    insertion_query = f"""
    INSERT INTO titanic (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare, index_col)
    VALUES
    {tuple(df.values[i])}
    """
    cursor.execute(insertion_query)


cursor.execute("SELECT * from titanic;")
result = cursor.fetchall()
print("RESULT:", len(result))

connection.commit()
connection.close()