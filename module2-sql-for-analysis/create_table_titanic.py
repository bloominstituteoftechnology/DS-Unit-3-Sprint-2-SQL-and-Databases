#!/usr/bin/env python

import psycopg2 as pg

dbname=''
user=''
password=''
host='.db..com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
cur=pg_conn.cursor()

create_titanic_table = """
DROP TABLE IF EXISTS titanic;

CREATE TABLE titanic(
id SERIAL PRIMARY KEY,
survived int,
pclass int,
name varchar(200),
sex varchar(10),
age numeric,
siblingSpouses int,
parentChildren int,
fare numeric
);"""

cur.execute(create_titanic_table)
pg_conn.commit()

