import psycopg2 as pg
import sqlite3
dbname = 'a'
user = 'a'
password = 'v'
host = 'b'
conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
rpg_db = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
pg_cur = conn.cursor()
sl_cur = rpg_db.cursor()
sl_cur.execute('SELECT * FROM charactercreator_character LIMIT 5')
results = sl_cur.fetchall()
print(results)
create_character_table = '''
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
)'''
print(create_character_table)
pg_cur.execute(create_character_table)
for result in results:
    insert_result = """INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES""" + str(result[1:])
    pg_cur.execute(insert_result)
print(pg_cur.fetchall())
conn.commit()
