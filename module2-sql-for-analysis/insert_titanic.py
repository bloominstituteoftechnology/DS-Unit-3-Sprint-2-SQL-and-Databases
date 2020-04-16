import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import numpy as np
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
import pandas as pd
import json

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, 
                              user=DB_USER,    
                              password=DB_PASSWORD, 
                              host=DB_HOST)

cursor = connection.cursor()

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)

# Convert to list of tuples
rows_to_insert = list(df.to_records(index=False))
#import pdb; pdb.set_trace()

table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived integer,
    pclass integer,
    name varchar NOT NULL,
    gender varchar NOT NULL,
    age float,
    sib_spouse_count integer,
    parent_child_count integer,
    fare float
);

"""

cursor.execute(table_creation_query)


insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"

execute_values(cursor, insertion_query, rows_to_insert)

connection.commit()
