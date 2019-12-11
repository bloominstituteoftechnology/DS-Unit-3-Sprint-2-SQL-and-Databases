import psycopg2

dbname = 'lqsujdux' 
user = 'lqsujdux' 
password =  'w7ih63BvRfpV_Mf9suEjW-6NmOGaTcP-'
host =  'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
pg_curs = pg_conn.cursor()

import sqlite3
import pandas as pd

sl_conn = sqlite3.connect('titanic.sqlite3')

# transform the titanic csv into a database that i can connect to using sqlite
df = pd.read_csv('titanic.csv')

data = df.to_sql(name = 'titanic', con=sl_conn)

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT * FROM titanic').fetchall()

sl_curs.execute('PRAGMA table_info(titanic);').fetchall()

create_titanic_table = """
    CREATE TABLE titanic(
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    Siblings/Spouses Aboard INT,
    Parents/Children Aboard INT,
    Fare REAL);
"""

