#!/usr/bin/env python

import psycopg2 as pg

dbname=''
user=''
password=''
host='.db..com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
cur=pg_conn.cursor()


import csv
with open('./titanic.csv', 'r') as f:
  next(f)
  cur.copy_from(f, 'titanic', sep=',',columns=('survived','pclass','name','sex','age','siblingSpouses','parentChildren','fare'))

pg_conn.commit()
