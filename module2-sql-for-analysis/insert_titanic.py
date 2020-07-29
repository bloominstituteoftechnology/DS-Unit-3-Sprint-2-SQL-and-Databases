import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

# Loading csv to pandas dataframe
file_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(file_path)
print(df.shape)
print(df.head())

# Establishing variables to PostgreSQL

DB_NAME = os.getenv('DB_NAME2', default='Check env variables')
DB_USER = os.getenv('DB_USER2', default='Check env variables')
DB_PASSWORD = os.getenv('DB_PASSWORD2', default='Check env variables')
DB_HOST = os.getenv('DB_HOST2', default='Check env variables')

sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_engine(sql_url)

print('ENGINE :', engine)

# Inserting DF data to table

df.to_sql('titanic', engine, if_exists='replace')
