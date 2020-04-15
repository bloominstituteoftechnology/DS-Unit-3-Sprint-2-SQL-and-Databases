import os
from sqlalchemy import create_engine
import sqlite3
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


# get titanic data from csv
df = pd.read_csv('titanic.csv')

# Change the columns to be more sql friendly
df.columns = ['survived', 'pclass', 'name', 'sex', 'age',
'sibling_spouse_aboard', 'parent_children_aboard', 'fare']
print(df.columns)
# print(df.head())

# Set up .env variables to connect to postgres later
envpath = os.path.join(os.getcwd(),'..', '.env')
# print(envpath)
load_dotenv(envpath)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

# set up the connection to postgres
sql_url = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
engine = create_engine(sql_url)
print('ENGINE:', engine)

df.to_sql('titanic_data', engine, if_exists='replace')

print('Test 1: Average Fare')

query = '''
SELECT
    AVG(fare)
FROM titanic_data
'''

print(pd.read_sql(query, engine), '\n')

print('Test 2: Ratio of Males to Females')

query = '''
SELECT
    sex as SexId
    ,count(sex) as SexCount
FROM titanic_data
GROUP BY sex
'''

print(pd.read_sql(query, engine), '\n')
