import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

TITANIC_DB_NAME = os.getenv('TITANIC_DB_NAME', default='oops')
TITANIC_DB_USER = os.getenv('TITANIC_DB_USER', default='oops')
TITANIC_DB_PASSWORD = os.getenv('TITANIC_DB_PASSWORD', default='oops')
TITANIC_DB_HOST = os.getenv('TITANIC_DB_HOST', default='oops')

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'titanic.csv')

connection = psycopg2.connect(dbname=TITANIC_DB_NAME, host=TITANIC_DB_HOST, password=TITANIC_DB_PASSWORD, user=TITANIC_DB_USER)
print('Connection:', connection)

df = pd.read_csv(CSV_FILEPATH)
df.columns = [item.lower().replace(' ', '_') for item in df.columns.tolist()]

df.to_sql('titanic', con=connection, if_exists='replace')