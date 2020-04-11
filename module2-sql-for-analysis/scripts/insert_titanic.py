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

cur = con.cursor()

# sanity checks comment out later
print('Con:', con)
print('Cur:', cur)

# set up the os agnostic path
TITANIC_PATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')

# Load into pandas
df = pd.read_csv(TITANIC_PATH)

# for MVP, just dump all the titanic CSV into your postgres db
# TODO

# Stretch actually split this up into appropriate tables
# like a passenger table, survivors table, class tables, etc
# TODO 