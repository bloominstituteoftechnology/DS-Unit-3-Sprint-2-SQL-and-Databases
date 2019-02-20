import sqlite3
import psycopg2 as pg

# Get the data from sqlite3
sqlite_connection = sqlite3.connect('rpg_db.sqlite3')
query_returned = sqlite_connection.execute('SELECT * FROM charactercreator_character;').fetchall()

# assign explicit types or postgres will be doomed. >.> My first upload file failed to do this
# 1. Because it does not know how to handle the django tables
# 2. Because the sqlite tables lack formatting. Must be a way to optimize that process over this explicit casting

create_character_table = """
    CREATE TABLE charactercreator_character (
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


postgres_db_name = 'munmevbr'
user = 'munmevbr'
password = 'ZTpRBiHy6sTarv3OPATL8vOVsQmOCeAH'
host = 'stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=postgres_db_name, user=user, password=password, host=host, port=5432)

postgres_cursor = pg_conn.cursor()
postgres_cursor.execute(create_character_table)

for table_name in query_returned:
        insert_result = """INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES""" + str(table_name[1:])

        postgres_cursor.execute(insert_result)

        pg_conn.commit()
