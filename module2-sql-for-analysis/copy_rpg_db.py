"""Example of moving data from rpg_db.sqlite3 to PostgreSQL."""

import sqlite3
import psycopg2 as pg


# Username and password to be set by user.
username = "SET_USERNAME_HERE"
password = "SET_PASSWORD_HERE"
host = "SET_HOST_ADDRESS_HERE"

# Get the data from sqlite3
sl_conn = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
results = sl_conn.execute("""SELECT *
                          FROM charactercreator_character;""").fetchall()

# Create table and insert data in PostgreSQL
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
pg_conn = pg.connect(host=host, dbname="postgres",
                     user=username, password=password)
pg_conn.set_isolation_level(pg.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
pg_curs = pg_conn.cursor()
pg_curs.execute("""SELECT datname
                FROM pg_database
                WHERE datistemplate = false;""")
if 'rpg' not in [X[0] for X in list(pg_curs.fetchall())]:
    pg_curs.execute('CREATE DATABASE rpg;')
    pg_conn.commit()
pg_conn.close()

pg_conn = pg.connect(host=host, dbname="rpg",
                     user=username, password=password)
pg_curs = pg_conn.cursor()
pg_curs.execute(create_character_table)

for result in results:
    insert_result = """INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES""" + str(result[1:])
    pg_curs.execute(insert_result)

pg_conn.commit()
