#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:44:55 2019

@author: ggash
"""

""" 
making a post-gress connection
today's activity
connectint to a postgress SQL server
"""

# this is only only needed if not installed
#!pip install psycopg2-binary

#this is needed to use the library
import psycopg2

#optional
dir(psycopg2)

#optional
help(psycopg2.connect)

# mask
dbname = 'nhxdkzlk' #same as user here
user = 'nhxdkzlk' # same as dbbase here
password = 'KT9iAxwS5ix36ZnNS_w1cGXW7a0nkgVV' # don't commit this to github!
host = 'otto.db.elephantsql.com' #

# 
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_conn

#this creates a cursor
pg_curs = pg_conn.cursor()

# testing connection to see what works
pg_curs.execute('SELECT * FROM test_table;')

pg_curs.fetchall()

# downloads the file
!wget = https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

#!ls -alh
#ls

# decompresses file?
!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3


import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()
print(sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall())

sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall()
print(sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall())

characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()

#characters

characters[0]

characters[-1]

len(characters)

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

create_character_table = """
    CREATE TABLE charactercreator_character2 (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
        );
"""

pg_curs.execute(create_character_table)

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)

pg_curs.fetchall()

str(characters[0][1:])

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ';'

print(example_insert)

# next section

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ';'
    #print(insert_character)

insert_character

pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

characters[0]

pg_characters[0]

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

pg_curs.close()
pg_conn.commit()
