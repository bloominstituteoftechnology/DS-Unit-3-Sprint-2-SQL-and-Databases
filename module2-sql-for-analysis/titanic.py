# import appropriate modules
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# load contents of the .env file into the script's environment
load_dotenv()

# Read in the data from the local file path or website
df = pd.read_csv('C:/Users/kingf/Unit3/DS-Unit-3-Sprint-2-SQL-and-\
Databases/module2-sql-for-analysis/titanic.csv')
print(df.shape) # print the shape to ensure we have right rows and columns
print(df.head()) # print the head to ensure right format

print("----------")
# Open a connection to ElephantSQL postgreSQL database
DB_NAME = os.getenv('DB_NAME', default='OOPS')
DB_USER = os.getenv('DB_USER', default='OOPS')
DB_PASSWORD = os.getenv('DB_PASSWORD', default='OOPS')
DB_HOST = os.getenv('DB_HOST', default='OOPS')

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST)
print("CONNECTION: ", connection)


connection.commit()
connection.close