import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import json
import numpy as np
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

### Connect to Elephant SQL

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

table_creation_query = """
DROP TABLE IF EXISTS charactercreator_character;
CREATE TABLE IF NOT EXISTS charactercreator_character (
    id SERIAL PRIMARY KEY,
    character_id integer,
    dexterity integer,
    exp integer,
    hp integer,
    intelligence integer,
    level integer,
    name varchar NOT NULL,
    strength integer,
    wisdom integer
);
"""

cursor.execute(table_creation_query)

JSON_FILEPATH = os.path.join(os.path.dirname(__file__), "charactercreator_character.json")
df = pd.read_json(JSON_FILEPATH)

# Convert to list of tuples
rows_to_insert = list(df.to_records(index=False))

insertion_query = """
INSERT INTO charactercreator_character (character_id, 
                                        dexterity, 
                                        exp, 
                                        hp, 
                                        intelligence, 
                                        level, 
                                        name, 
                                        strength,
                                        wisdom) VALUES %s
"""

execute_values(cursor, insertion_query, rows_to_insert)

connection.commit()
