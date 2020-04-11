
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv() # This is to make the .env file 
              # contents be put into the enviro
              # variables

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
        host=DB_HOST, password=DB_PASSWORD)
print("Connection:", connection)

cur = connection.cursor()
print("Cursor:", cur)

cur.execute()

