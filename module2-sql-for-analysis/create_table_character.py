#!/usr/bin/env python

import psycopg2 as pg

dbname='oljqozut'
user='oljqozut'
password='vtGp1NOnMDgalZrLt54C1_z4DunXeqXm'
host='stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
cur=pg_conn.cursor()

create_character_table = """
DROP TABLE IF EXISTS charactercreator_character;

CREATE TABLE charactercreator_character(
character_id SERIAL PRIMARY KEY,
name varchar(60),
level int,
exp int,
hp int,
strength int,
intelligence int,
dexterity int,
wisdom int
);"""

cur.execute(create_character_table)
pg_conn.commit()

