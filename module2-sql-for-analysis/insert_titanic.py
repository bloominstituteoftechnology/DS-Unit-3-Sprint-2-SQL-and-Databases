# import appropriate modules
import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# load contents of the .env file into the script's environment
load_dotenv()

# Read in the data from the local file path or website
df = pd.read_csv('C:/Users/dougcohen/Repos/Unit-3/DS-Unit-3-Sprint-2-SQL-and-\
Databases/module2-sql-for-analysis/titanic.csv')
print(df.shape) # print the shape to ensure we have right rows and columns
print(df.head()) # print the head to ensure right format

print("----------")
# Open a connection to ElephantSQL postgreSQL database
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()

# Create engine to use for df.to_sql
engine = create_engine('postgres://dyuqpkft:flXZLz...@drona.db.elephantsql.com\
:5432/dyuqpkft')

# Use df.to_sql to insert the data into a new table 'titanic' in the PostgrSQL 
#. database
df.to_sql('titanic', engine)
conn = engine.raw_connection()

conn.commit()