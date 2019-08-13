# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import psycopg2


dbname = 'bndoemhv'
user = 'bndoemhv'
password = ''  # Dont commit this
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_conn

pg_curs = pg_conn.cursor()


df = pd.read_csv("titanic.csv")

conn = sqlite3.connect("titanic.sqlite3")
df.to_sql(name='titanic_database', con=conn, if_exists='replace')

df.columns

curs = conn.cursor()

print(curs.execute("SELECT COUNT(*) FROM titanic_database;").fetchall())
