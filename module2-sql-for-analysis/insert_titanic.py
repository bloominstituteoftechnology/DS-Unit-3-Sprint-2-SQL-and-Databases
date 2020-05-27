import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
import os
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

# Loading csv to pandas dataframe
file_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(file_path)
print(df.shape)
print(df.head())

# Establishing connection and cursor to ElephantSQL

DB_NAME = os.getenv('DB_NAME2', default='Check env variables')
DB_USER = os.getenv('DB_USER2', default='Check env variables')
DB_PASSWORD = os.getenv('DB_PASSWORD2', default='Check env variables')
DB_HOST = os.getenv('DB_HOST2', default='Check env variables')

connection = psycopg2.connect(
    dbname = DB_NAME,
    user = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST)
print('CONNECTION :', connection)

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS titanic;')

# Creating table with query

table_query = 'CREATE TABLE titanic(Survived INT, Pclass INT, Name varchar(150), Sex varchar(10), Age INT, SiblingsSpouse INT, ParentsChildren INT, Fare INT);'

cursor.execute(table_query)

# Copying .csv file data into new table with query

import_query = "COPY titanic FROM 'titanic.csv' DELIMITER ',' CSV HEADER;"

cursor.execute(import_query)

connection.commit()

cursor.execute('SELECT * FROM titanic')
