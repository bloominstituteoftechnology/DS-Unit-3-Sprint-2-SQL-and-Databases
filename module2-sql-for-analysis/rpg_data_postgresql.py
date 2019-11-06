"""
Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a PostgreSQL database, and add the code you write
to do so.
"""

import psycopg2
import sqlite3

pg_conn = psycopg2.connect("dbname=postgres user=postgres password={secret}")
pg_curs = conn.cursor()

# I cut out local username for security reasons
sl_conn = sqlite3.connect(('rpg_db.sqlite3')
sl_curs=sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()
sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character'
                ).fetchall()

characters=sl_curs.execute('SELECT * FROM charactercreator_character;'
                           ).fetchall()
# This line will let me see all the elements I need to create table
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

query_create_table="""
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
pg_curs.execute(query_create_table)

show_tables="""
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
    """
pg_curs.execute(show_tables)
pg_curs.fetchall()

for character in characters:
    insert_character="""
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_curs.close()
pg_conn.commit()
