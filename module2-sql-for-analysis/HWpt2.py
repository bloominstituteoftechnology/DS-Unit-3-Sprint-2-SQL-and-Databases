#import what we need
import pandas as pd
from sqlalchemy import create_engine

#Read in the Titanic df
df = pd.read_csv('module2-sql-for-analysis/titanic.csv')
#make sure we got it
df.head()
#See what the datatypes are
df.dtypes
df.info()

# Create engine for DF insertion 
engine = create_engine('postgres://ensbdkiv:s2-dWAkXkoJhwcZe1PQfHN9Tx6i7clv9@salt.db.elephantsql.com:5432/ensbdkiv')
df.to_sql('titanic_dataset', engine)

