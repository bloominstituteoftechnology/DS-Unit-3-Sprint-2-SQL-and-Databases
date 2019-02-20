#!/usr/bin/env python
""" Example of moving data from rpg_db.sqlite3 to PostgreSQL."""
import sqlite3
import psycopg2 as pg

# Get the data from sqlite3
sl_conn = sqlite3.connect('C:\\Users\\Gutierrez\\Documents\\DataScience\\lambda_school\\DS-Unit-3-Sprint-2-SQL-and-Databases\\module1-introduction-to-sql\\rpg_db.sqlite3')
results = sl_conn.execute('SELECT * FROM charactercreator_character;').fetchall()

create_character_table = """CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,
    wisdom int);"""

# Assume user defines database parameters
dbname ='hartabvb'
user = 'hartabvb'
password = '9jk1ptYGv0qclPjUQybvhF8bnmAXPmNv'
host = 'stampy.db.elephantsql.com'

    
pg_conn = pg.connect(dbname=dbname, user=user,
                        password=password, host=host)

def make_and_populate_character_table():
    pg_curs = pg_conn.cursor()

    pg_curs.execute(create_character_table)


    for result in results:
        insert_result = """INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES""" + str(result[1:])
        pg_curs.execute(insert_result)

    pg_conn.commit()