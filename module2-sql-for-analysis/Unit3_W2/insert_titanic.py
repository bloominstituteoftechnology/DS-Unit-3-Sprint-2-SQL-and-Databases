
#insert_titanic

import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import pandas as pd
import pymysql

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

DB_FILEPATH = 'titanic.csv'
connect = pd.read_csv(r'titanic.csv')
titanic = connect.cursor()
print("CURSOR", titanic)