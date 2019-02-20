#!/usr/bin/env python
"""Example of moving data from titanic.csv to PostgreSQL."""

import sqlite3
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

# load data into pandas df
titanic = pd.read_csv('titanic.csv')
print (titanic.dtypes)

# initialize postgres connection
dbname = 'TODO'
user = 'TODO'
password = 'TODO'
host = 'TODO'

pg_conn = pg.connect(dbname=dbname, user=user,
                     password=password, host=host)

# drop table if it exists, and create new table
pg_curs = pg_conn.cursor()
pg_curs.execute('DROP TABLE IF EXISTS titanic')

titanic_table_create = """CREATE TABLE titanic (
  id SERIAL PRIMARY KEY,
  survived int,
  pclass int,
  name VARCHAR(50),
  sex VARCHAR(7),
  age float,
  siblings_spouses_aboard int,
  parents_children_aboard int,
  fare float
)"""

pg_curs.execute(titanic_table_create)

# insert titanic table into postgres db
# titanic.to_sql(name='titanic', con=pg_conn, schema=None, if_exists='replace',
#                index=True)
engine = create_engine('postgres://' + dbname + ':' + password + '@'
                       + host + ':5432/' + user)
titanic.to_sql('titanic', engine, if_exists='replace')

# commit changes
pg_conn.commit()
