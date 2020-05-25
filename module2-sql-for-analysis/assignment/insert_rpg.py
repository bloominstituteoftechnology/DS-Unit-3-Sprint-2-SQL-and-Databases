import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

RPG_DB_NAME = os.getenv('RPG_DB_NAME', default='oops')
RPG_DB_USER = os.getenv('RPG_DB_USER', default='oops')
RPG_DB_PASSWORD = os.getenv('RPG_DB_PASSWORD', default='oops')
RPG_DB_HOST = os.getenv('RPG_DB_HOST', default='oops')

connection = psycopg2.connect(dbname=RPG_DB_NAME, user=RPG_DB_USER, password=RPG_DB_PASSWORD, host=RPG_DB_HOST)
print('Connection:', connection)