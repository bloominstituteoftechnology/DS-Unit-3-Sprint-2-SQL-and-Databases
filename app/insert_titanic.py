import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

CSV_filepath = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
df = pd.read_csv(CSV_filepath)
print(df.head())

# Update column types so we can transfer data to a postgreSQL Database.
int_columns = ['Survived','Pclass', 'Siblings/Spouses Aboard', 'Parents/Children Aboard']

for col in int_columns:
  df[col] = df[col].astype(float)

# move the data to an iterable tuple list that we can insert to DB
titanic_list = df.to_records(index=False)

# Get the credentials from env to login to postgreSQL database
load_dotenv()
DB_NAME = os.getenv("DB_NAME_DB13_Unit3")
DB_USER = os.getenv("DB_USER__DB13_Unit3")
DB_PASSWORD = os.getenv("DB_PASSWORD__DB13_Unit3")
DB_HOST = os.getenv("DB_HOST__DB13_Unit3")

# create connection to PostgrSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

# create the cursor
cursor = connection.cursor()

# create the query to create a new titanic table in database
query = """
CREATE TABLE IF NOT EXISTS titanic_table(
  id SERIAL PRIMARY KEY,
  Survived INT CHECK (Survived = 0 OR Survived = 1),
  Pclass INT CHECK (Pclass > 0 AND Pclass <= 3 ),
  Name VARCHAR(100),
  Sex VARCHAR(10) CHECK (Sex in ('male', 'female')),
  Age FLOAT(8),
  Sibilings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare FLOAT(8)
);
"""

# execute the query and commit the table to the database
cursor.execute(query)
connection.commit()

# create an insertion query to populate the table
insert_query = """
INSERT INTO titanic_table 
(Survived, Pclass, Name, Sex, Age, Sibilings_Spouses_Aboard, Parents_Children_Aboard, Fare)
VALUES %s;
"""

# execute the insert query and save the data to the table in the DB
execute_values(cursor, insert_query, titanic_list)
connection.commit()

# Close the connection
cursor.close()
connection.close()