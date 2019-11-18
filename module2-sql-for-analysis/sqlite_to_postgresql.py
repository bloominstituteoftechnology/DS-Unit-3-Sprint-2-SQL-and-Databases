# imports
import sqlite3
import psycopg2

# sqlite connection and cursor
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cur = sl_conn.cursor()

# test connection
sl_cur.execute("""SELECT * FROM charactercreator_character
                  LIMIT 20""")
sl_character_table =  sl_cur.fetchall()
print(sl_character_table[0])
print(len(sl_character_table))

# elephantsql credentials
host = 'salt.db.elephantsql.com'
user = 'rtwvxkrw'
database = 'rtwvxkrw'
password = 'bfZkn2ysvf3eTCa19VmMwJkt-bZyO-tK'

# make connection to elephantsql, open cursor
pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

# create table for elephantsql
create_character_table = """
CREATE TABLE Characters(
    characterid int PRIMARY KEY,
    name VARCHAR(255),
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,
    wisdom int);
"""

pg_cur.execute(create_character_table)
pg_conn.commit()

# using executemany
query = """INSERT INTO Characters VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
pg_cur.executemany(query, sl_character_table)
pg_conn.commit()

sl_cur.close()
pg_cur.close()