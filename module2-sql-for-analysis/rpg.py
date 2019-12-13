import psycopg2

dbname = 'solhbfxg'
user = 'solhbfxg'
password = '13OzHHPubTuYr8pbMgiukG2QEe_rugEl'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

import sqlite3
ite_conn = sqlite3.connect('rpg_db.sqlite3')
ite_curs = ite_conn.cursor()

data = ite_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

pg_curs.execute('CREATE TABLE charactercreator_character (character_id INTEGER PRIMARY KEY, name TEXT, level INTEGER, exp INTEGER, hp INTEGER, strength INTEGER, intelligence INTEGER, dexterity INTEGER, wisdom INTEGER);')
for row in data:
  row = list(map(lambda x: f"'{x}'" if isinstance(x, str) else str(x), row))
  row = ', '.join(row)
  q = f'INSERT INTO charactercreator_character (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES ({row});'
  pg_curs.execute(q)

ite_curs.close()
ite_conn.commit()
pg_curs.close()
pg_conn.commit()