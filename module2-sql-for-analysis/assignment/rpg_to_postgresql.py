!pip install psycopg2-binary

import sqlite3
import psycopg2


!wget https://github.com/jonathanmendoza-tx/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true -O rpg_db.sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cur = sl_conn.cursor()

sl_cur.execute("SELECT * FROM charactercreator_character")
sl_character_table = sl_cur.fetchall()

host = 'raja.db.elephantsql.com'
user = 'eanjyxnx'
database = 'eanjyxnx'
password = 'DG3VKCromh_iPadB06yhaPbZiiT6KJF2'

pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

create_character_table = """
CREATE TABLE Characters(
   character_id serial PRIMARY KEY,
   name VARCHAR (200) NOT NULL,
   level INTEGER NOT NULL,
   exp INTEGER NOT NULL,
   hp INTEGER NOT NULL,
   strength INTEGER NOT NULL,
   intelligence INTEGER NOT NULL,
   dexterity INTEGER NOT NULL,
   wisdom INTEGER NOT NULL
);
"""

pg_cur.execute(create_character_table)
pg_conn.commit()

for row in sl_character_table:
	query = f"INSERT INTO Characters VALUES {str(row)}"
	pg_cur.execute(query)

pg_conn.commit()
