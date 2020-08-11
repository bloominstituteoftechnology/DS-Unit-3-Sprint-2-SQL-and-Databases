# pipenv shell
# pipenv install psycopg2-binary
# pipenv install pandas if not installed

import psycopg2
import sqlite3
import pandas as pd


conn = sqlite3.connect('testdb.db')
c = conn.cursor()

data = 'titanic.csv'
df = pd.read_csv(data)

print(df.shape)

df.to_sql('titanic', con=conn)

sl_conn = sqlite3.connect('titanic')
sl_curs = sl_conn.cursor()

get_passenger = "SELECT * FROM titanic;"
sl_curs.execute(get_passenger)
passengers = sl_curs.fetchall()

# Auth/Host info to connect
dbname = 'yfnzcrhk'
user = 'yfnzcrhk'
password = 'C9HzIuc_T0xZEBHH9S89mMfJMLGR_caH'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE titanic_table (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name varchar(40) NOT NULL,
    sex STR,
    age INT,
    siblings/spouses aboard INT,
    parents/children aboard INT,
    fare INT,
    data JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_conn.commit()


insert = """
INSERT INTO titanic
(survived, pclass, name, sex, age, siblings/spouses aboard,
 parents/children aboard, fare)
 VALUES"""


for passenger in passengers:
    insert = """
        INSERT INTO titanic
        (survived, pclass, name, sex, age, siblings/spouses aboard,
        parents/children aboard, fare)
        VALUES"""+ str(passengers[1:]) + ";"
    pg_curs.execute(insert)