#!/usr/bin/env python3

import psycopg2
import sqlite3
import pandas as pd

dbname = 'nhworfxj'
user = 'nhworfxj'
password = 'kP5yE4IqyZ80aWYuhHUkPzrTCrvetxgP'
host = 'balarama.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
        password = password, host = host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect("titanic.sqlite3")

df = pd.read_csv("titanic.csv")
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')
df.to_sql("titanic", sl_conn)

sl_conn.commit()

sl_curs = sl_conn.cursor()

print(sl_curs.execute("PRAGMA table_info(titanic);").fetchall())

pg_curs.execute("CREATE TYPE gender AS ENUM ('male', 'female');")

create_titanic_table = """
CREATE TABLE titanic (
    titanic_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    sex gender,
    age INT,
    siblings_or_spouses_aboard INT,
    parents_or_children_aboard INT,
    fare REAL
);
"""

pg_curs.execute(create_titanic_table)

pg_curs.close()
pg_conn.commit();


get_passengers = 'SELECT * FROM titanic'
passengers = sl_curs.execute(get_passengers).fetchall()

sl_curs.close()

pg_curs = pg_conn.cursor()

for passenger in passengers:
  insert_character = """
    INSERT INTO titanic
    (survived, pclass, name, sex, age, siblings_or_spouses_aboard, parents_or_children_aboard, fare)
    VALUES """ + str(passenger[1:]) + ";"
  pg_curs.execute(insert_character)

pg_conn.commit()

pg_curs.execute('SELECT * FROM titanic')
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()