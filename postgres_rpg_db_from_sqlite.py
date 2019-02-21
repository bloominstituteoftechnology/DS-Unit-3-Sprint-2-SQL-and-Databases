#!/usr/bin/env/python
# the above command is called shebang to tell the computer to execute
# the following code using avaialble python
""" Exmaple of moving data from rpg_db.sqlite3 to PostgreSQL"""

import sqlite3
import psycopg2 as pg

# get the data from sqlite3
sql_conn = sqlite3.connect("/home/mishraka/repos/manjulamishra/rpg_db.sqlite3")
results = sql_conn.execute(
    'SELECT * FROM charactercreator_character;').fetchall()


#  Create table and insert data in PostgreSQL
create_character_table = """CREATE TABLE charactercreator_character (
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

# Assume user defines database parameters
dbname = 'wywlalgk'
user = 'wywlalgk'
password = 'vb6ja9HHMnqH2QMzocJuuGSRxJEVKHaJ'
host = 'stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)


def make_and_populate_character_table():
    pg_curs = pg_conn.cursor()

    pg_curs.execute(create_character_table)

    for result in results:
        insert_result = """INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(result[1:])
        pg_curs.execute(insert_result)

    pg_conn.commit()
