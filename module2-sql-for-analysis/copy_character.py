#!/usr/bin/env python

import psycopg2 as pg

dbname='oljqozut'
user='oljqozut'
password='vtGp1NOnMDgalZrLt54C1_z4DunXeqXm'
host='stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
cur=pg_conn.cursor()

copy_character_table = """
with open('./character.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'charactercreator_character', sep='|')

"""


cur.execute(copy_character_table)
pg_conn.commit()

