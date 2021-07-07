import psycopg2
import sqlite3

dbname = 'zqxmasuz'
user = 'zqxmasuz'
password = 'BLANK'
host = 'raja.db.elephantsql.com'

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)


def transfer_postgre(pg_conn):
    pg_curs = pg_conn.cursor()
    create_character_table = """
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
    pg_curs.execute(create_character_table)

    for character in characters:
        insert_character = """
            INSERT INTO charactercreator_character
            (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES """ + str(character[1:]) + ';'
        pg_curs.execute(insert_character)

    pg_curs.close()
    pg_conn.commit()


def test(pg_conn):
    pg_curs = pg_conn.cursor()
    pg_curs.execute('SELECT * FROM charactercreator_character;')
    pg_characters = pg_curs.fetchall()

    for character, pg_character in zip(characters, pg_characters):
        assert character == pg_character

    assert len(characters) == len(pg_characters)
    pg_curs.close()
    pg_conn.commit()
    sl_curs.close()
    sl_conn.commit()


transfer_postgre(pg_conn)
test(pg_conn)