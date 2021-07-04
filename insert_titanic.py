import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# elephantSQL details
dbname = 'kvobzcdf'
user = 'kvobzcdf'
password = ''
host = 'raja.db.elephantsql.com'

# create connection to postgres
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

DATA = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
df = pd.read_csv(DATA)
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces


engine = create_engine('postgres://kvobzcdf:Z6GcK2XttNxPBRVoCVBM-_FgYLdfDJst@raja.db.elephantsql.com:5432/kvobzcdf')

df.to_sql("titanic", engine)
