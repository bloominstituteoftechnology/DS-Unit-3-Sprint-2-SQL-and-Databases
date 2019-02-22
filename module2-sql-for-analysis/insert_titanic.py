#!/usr/bin/env python 3

import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

df = pd.read_csv('titanic.csv')

# Define db parameters
dbname = some_name
user = some_user
password = some_password
host = some_host

# Create table then insert data into PostgreSQL
engine = create_engine('')
df.to_sql('table_name', engine)

# Make connection object
pg_connxn = pg.connect(dbname=dbname, user=user, password=password, host=host)

# Populate table
def make_and_populate_table():
    pg_curs = pg_connxn.cursor()
    pg_curs.execute('table_name')

    for something in some_results_sequence:
        insert_something = """INSERT INTO
        <table_name> (a tuple of values) VALUES""" + str(tuple(something))
    
    pg_curs.execute(insert_something)

# Commit
pg_connxn.commit()

