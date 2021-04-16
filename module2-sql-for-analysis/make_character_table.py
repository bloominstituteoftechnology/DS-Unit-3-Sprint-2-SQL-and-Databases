#!/usr/bin/env python3

import psycopg2

dbname = 'nsvybuvb'
user = 'nsvybuvb' # same as dbname
password= 'ZSQQPpNjrb78uZJLGrGliTLdiTaWCAK5' # not my real password
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user, 
        password = password, host = host)

pg_curs = pg_conn.cursor()

pg_curs.execute('select * from test_table')

print(pg_curs.fetchall())


import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

print(sl_curs.execute('select count(*) from charactercreator_character').fetchall())
print(sl_curs.execute('select count(distinct name) from charactercreator_character').fetchall())
characters = sl_curs.execute('select * from charactercreator_character').fetchall()

print(characters[-1])


print(sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())


create_character_table = """
create table charactercreator_character (
character_id serial primary key,
name varchar(30),
level int,
exp int,
hp int,
strength int,
intelligence int,
dexterity int,
wisdom int);
"""

pg_curs.execute(create_character_table)

show_tables = """
select * from pg_catalog.pg_tables
where schemaname != 'pg_catalog'
and schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)

print(pg_curs.fetchall())


print(str(characters[0][1:]))


insert_start = """
insert into charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
values """

for character in characters:
    insert_character = insert_start + str(character[1:]) + ';'
    pg_curs.execute(insert_character)

pg_curs.execute('select * from charactercreator_character;')
print(pg_curs.fetchall())


pg_curs.close()
pg_conn.commit()

