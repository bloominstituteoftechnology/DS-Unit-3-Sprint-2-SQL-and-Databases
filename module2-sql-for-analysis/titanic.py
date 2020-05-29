import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import json
import pandas as pd
import sqlalchemy

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_URL = os.getenv('DB_URL')


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cur = conn.cursor()

# create the dataframe
path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(path)

# creat table in database
engine = sqlalchemy.create_engine(DB_URL)

df.to_sql('titanic', con=engine, index=True, if_exists='replace')





conn.commit()
cur.close()
conn.close()