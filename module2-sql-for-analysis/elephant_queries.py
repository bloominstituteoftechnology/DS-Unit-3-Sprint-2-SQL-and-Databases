import os
from dotenv import load_dotenv
import psycopg2
import sqlite3

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()

# Fetch RPG data
rpgconn = sqlite3.connect('rpg_db.sqlite3')
rpgcur = rpgconn.cursor()
rpgdata = rpgcur.execute('SELECT * FROM charactercreator_character').fetchall()

# Convert to list of tuples
#--it already is

# Insert into DB
#create table
create = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name varchar(30) NOT NULL,
    level INTEGER NOT NULL,
    exp INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    wisdom INTEGER NOT NULL
);'''
cur.execute(create)

#Insert values
insert = 'INSERT INTO rpg_characters  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cur.executemany(insert,rpgdata)