#!/usr/bin/env python

import psycopg2 as ps
import sqlite3 as sq
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("ELEPHANTSQL_USER")
password = os.getenv("ELEPHANTSQL_PASSWORD")
host = os.getenv("ELEPHANTSQL_HOST")
dbname = os.getenv("ELEPHANTSQL_DBNAME")

conn = ps.connect(database=dbname, user=user, password=password, host=host)

pg_cur = conn.cursor()

rpg_db = sq.connect('../module1-introduction-to-sql/rpg_db.sqlite3')


q = "SELECT * from charactercreator_character"
c = rpg_db.execute(q).fetchall()

print(c[0:2])

q = "DROP TABLE IF EXISTS charactercreator_character"
pg_cur.execute(q)

create_character_table = """
CREATE TABLE charactercreator_character
(
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

pg_cur.execute(create_character_table)

q = """INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """

for r in c[:-1]:
    q += f"{r[1:]},"
q += f"{c[-1][1:]};"

c = pg_cur.execute(q)

conn.commit()

pg_cur = conn.cursor()

q = "SELECT * FROM charactercreator_character LIMIT 2"
pg_cur.execute(q)
c = pg_cur.fetchall()

print(c)


q = "DROP TABLE IF EXISTS titanic"
pg_cur.execute(q)

df = pd.read_csv("titanic.csv")
q = "DROP TYPE IF EXISTS gender"
pg_cur.execute(q)
q = "CREATE TYPE gender AS ENUM ('male', 'female');"
pg_cur.execute(q)

create_titanic_table = """
CREATE TABLE titanic
(
character_id SERIAL PRIMARY KEY,
survived boolean,
pclass int,
name varchar(128),
sex gender,
age real,
siblings_spouses_aboard int,
parents_children_aboard int,
fare real
);"""
pg_cur.execute(create_titanic_table)

q = """INSERT INTO titanic(survived, pclass, name, sex, age,siblings_spouses_aboard,
parents_children_aboard, fare ) VALUES """

for l in df.values[:-1]:
    q += f"({l[0] == 1},{l[1]},$${l[2]}$$,$${l[3]}$$,{l[4]},{l[5]},{l[6]},{l[7]}),"
l = df.values[-1]
q += f"({l[0] == 1},{l[1]},$${l[2]}$$,$${l[3]}$$,{l[4]},{l[5]},{l[6]},{l[7]});"
pg_cur.execute(q)

conn.commit()

q = "SELECT * FROM titanic LIMIT 10"
pg_cur.execute(q)
c = pg_cur.fetchall()

print(c)
