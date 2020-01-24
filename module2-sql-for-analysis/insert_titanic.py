import psycopg2
import sqlite3
import pandas as pd

dbname = 'lsustohi'
user = 'lsustohi'
password = 'nCW8Zgf4Lp0oVej5-fs0dxQY9OEhyMhY'
host = 'rajje.db.elephantsql.com'

#Create connections and cursors
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

df = pd.read_csv('titanic.csv')
#df.to_sql('titanic', sl_conn) only once


# Extract titanic data
query = 'SELECT * FROM titanic'
titanic_sql = sl_curs.execute(query).fetchall()


# Create postgreSQL table
create_titanic_table = """
CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(70),
    sex VARCHAR(10),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare REAL
);
"""


