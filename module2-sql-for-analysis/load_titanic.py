import psycopg2
import sqlite3
import pandas as pd
from credentials import db_login_info
from df_utils import load_titanic


CREDS = db_login_info()

pg_conn = psycopg2.connect(dbname = CREDS[0],
                           user = CREDS[1],
                          password = CREDS[2],
                          host = CREDS[3])
pg_cur = pg_conn.cursor()

command = 'DROP TABLE IF EXISTS titanic'
pg_cur.execute(command)

sl_conn = sqlite3.connect('titanic.db')
sl_cur = sl_conn.cursor()

df = load_titanic()

df.to_sql('titanic', sl_conn)

DB_INFO = sl_cur.execute('SELECT * FROM titanic').fetchall()

command = """CREATE TABLE titanic(
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare Real
    );"""

pg_cur.execute(command)
pg_cur.close()
pg_conn.commit()

pg_conn = psycopg2.connect(dbname = CREDS[0],
                           user = CREDS[1],
                          password = CREDS[2],
                          host = CREDS[3])
pg_cur = pg_conn.cursor()

for item in DB_INFO:
    item = """
        INSERT INTO titanic
        (Survived, Pclass, 
        Name, Sex, Age, 
        Siblings_Spouses_Aboard, 
        Parents_Children_Aboard,Fare)
        VALUES""" + str(item[1:]) + ";"
    pg_cur.execute(item)

pg_cur.close()
pg_conn.commit()
