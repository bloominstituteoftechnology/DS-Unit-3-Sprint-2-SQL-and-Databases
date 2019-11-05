# imports
from password import password
import psycopg2
import pandas as pd
import sqlalchemy

# parameters for connect method
dbname = 'jrzitwbn'
user = 'jrzitwbn'
host = 'salt.db.elephantsql.com'

# read csv into pandas dataframe
df = pd.read_csv('titanic.csv')

# clean column names
df.columns = [c.lower().replace('/', '_').replace(' ', '_')
              for c in df.columns]

# connect to database
connection_details = f'postgresql://{user}:{password}@{host}/{dbname}'
engine = sqlalchemy.create_engine(connection_details)
conn = engine.connect()

# check existing tables
print(engine.table_names())

# # store the dataframe as table in postgresql
# table_name = 'titanic'
# df.to_sql(table_name, conn)

# close connection
conn.close()
