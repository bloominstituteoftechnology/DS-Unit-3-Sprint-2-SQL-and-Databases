# ./usr/bin/env python

import psycopg2 as pg
import csv

titanic_table = """CREATE TABLE titanic(
  Survived INT,
  Pclass INT,
  Name TEXT,
  Sex TEXT,
  Age NUMERIC(4, 2),
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare NUMERIC(7, 4)
);"""

dbname = 'dbname'
user = 'user'
password = 'password'
host = 'host'

pg_conn = pg.connect(dbname=dbname, user=user,
                     password=password, host=host)
cur = pg_conn.cursor()

cur.execute(titanic_table)

with open('titanic.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    initial = ((int(row[0]),
              int(row[1]),
              row[2],
              row[3],
              float(row[4]),
              int(row[5]),
              int(row[6]),
              float(row[7]))
              for row in reader
              )
    for item in initial:
        insert_result = """INSERT INTO titanic VALUES""" + str(item) + ';'
        cur.execute(insert_result)

pg_conn.commit()
cur.close()
pg_conn.close()
