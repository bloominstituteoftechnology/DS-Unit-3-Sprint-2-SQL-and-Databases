import os
import sqlite3
import json
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
load_dotenv()



DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_NAME=os.getenv("DB_NAME")
DB_PW= os.getenv("DB_PW")

# DB_NAME = os.getenv("DB_NAME", default="OOPS")
# DB_USER = os.getenv("DB_USER", default="OOPS")
# DB_PW = os.getenv("DB_PW", default="OOPS")
# DB_HOST = os.getenv("DB_HOST", default="OOPS")
lite_con = sqlite3.connect(DATABASE_FILEPATH)
lite_cursor = lite_con.cursor()
get_table = """
select * from charactercreator_character"""
query1 = lite_cursor.execute(get_table).fetchall()
#print(query1)

create_table = """
create table if not exists character(
    character_id INTEGER,
    name varchar(40),
    level INTEGER,
    exp INTEGER,
    hp INTEGER,
    strength INTEGER,
    intelligence INTEGER,
    dexterity INTEGER,
    wisdom INTEGER
)"""
#print(type(conn))
#cursor = conn.cursor()
### Connect to ElephantSQL-hosted PostgreSQL
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PW, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
pg_cur = pg_conn.cursor()
# ### An example query
insertion_query = f"insert into character (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s"

pg_cur.execute(create_table)
execute_values(pg_cur, insertion_query, query1)

pg_conn.commit()
pg_conn.close()
# ### Note - nothing happened yet! We need to actually *fetch* from the cursor
# cur.fetchone()