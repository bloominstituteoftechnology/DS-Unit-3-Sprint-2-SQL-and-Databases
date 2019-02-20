#!/usr/bin/env python

import sqlite3
import psycopy2 as pg

dbname=postgres://oljqozut:vtGp1NOnMDgalZrLt54C1_z4DunXeqXm@stampy.db.elephantsql.com:5432/oljqozut
user=oljqozut
password=vtGp1NOnMDgalZrLt54C1_z4DunXeqXm
host=stampy.db.elephantsql.com
pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)

cur=pg_conn.cursor()
cur.execute('SELECT * from test_table;')
results=cur.fetchall()
df=pd.DataFrame(results[1][2])
df.to_sql

import sqlite3
rpg_db_conn=sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
sl_cur = rpg_db_conn.cursor()
pg_cur = pg.conn.cursor()

sl_cur.execute('SELECT * FROM charactercreator_character LIMIT 5;')
results = sl_cur.fetchall()

create_character_table = """
CREATE TABLE charactercreator_character(
character_id SERIAL PRIMARY KEY,
name varchar(30),
level int,
exp int,
hp int,
strength int,
intelligence int,
dexterity int,
wisdom int
);"""

results=pg_cur.execute(create_character_table)
for result in results:
  insert_result = """INSERT INTO charactercreator_character
  (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
  VALUES""" + str(result[1:])

pg_cur.execute(insert_result)

pg_cur.execue('SELECT * FROM charactercreator_character;')
pg_cur.fetchall()

