import psycopg2
import sqlite3
import os
from dotenv import load_dotenv

dir(psycopg2)

load_dotenv()
password = os.getenv("ELEPHANT_PW")

dbname = 'htcgadjc'
user = 'htcgadjc'
host = ('salt.db.elephantsql.com')

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute("SELECT * FROM staff;")
print(pg_curs.fetchall())


# !wget -nc https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true
# !mv -n 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

sl_conn = sqlite3.connect('./rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

count = sl_curs.execute(
    'SELECT COUNT(*) FROM charactercreator_character;').fetchall()
print(count)

characters = sl_curs.execute(
    'SELECT * from charactercreator_character;').fetchall()
print(len(characters))


show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
print(pg_curs.fetchall())

create_table = """
CREATE TABLE charactercreator_character (
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
pg_curs.execute(create_table)

for character in characters:
    insert_character = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)

sl_curs.close()
sl_conn.close()

pg_curs.close()
pg_conn.commit()
pg_conn.close()
