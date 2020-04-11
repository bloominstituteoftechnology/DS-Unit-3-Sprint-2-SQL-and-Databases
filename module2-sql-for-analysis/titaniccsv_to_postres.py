import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

#connect to titanic db
load_dotenv()

HOST = os.getenv('TITANIC_HOST')
NAME = os.getenv('TITANIC_NAME')
USER = os.getenv('TITANIC_USER')
PASSWORD = os.getenv('TITANIC_PASSWORD')

con = psycopg2.connect(dbname = NAME, 
                        user = USER, 
                        password = PASSWORD, 
                        host = HOST)

cur = connection.cursor()

# sanity checks comment out later
print('Con:', con)
print('Cur:', cur)

# set up the os agnostic path
# TODO

# Load into pandas
# TODO

# inspect and evaluate tables to be made
# TODO