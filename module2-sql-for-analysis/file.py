import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('titanic.csv')
engine = create_engine('postgres://vbmmjeoc:qiPPfJeCLmtX5-yUZcV27SmlTz75PQka@isilo.db.elephantsql.com:5432/vbmmjeoc')
df.to_sql('titanic2', con=engine)