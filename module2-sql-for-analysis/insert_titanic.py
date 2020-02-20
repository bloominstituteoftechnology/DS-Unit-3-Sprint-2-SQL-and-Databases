import pandas as pd
import psycopg2
import sqlite3


dbname = 'gzczudsv'
user = 'gzczudsv'
password = 'rbQXW-AT5HA0vudl9kvjtIw07ZzTOlNR'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)

pg_curs = pg_conn.cursor()

titanic_db = pd.read_csv('/Users/josephbell/Desktop/sql-practice/titanic.csv')

titanic_db['Name'] = titanic_db['Name'].str.replace("'", "")

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

titanic_db.to_sql('titanic', sl_conn)

get_passengers = "SELECT * FROM titanic"
passengers = sl_curs.execute(get_passengers).fetchall()

create_passengers_table = """
CREATE TABLE IF NOT EXISTS passengers (
survived BOOL,
pclass INT,
name VARCHAR,
sex VARCHAR,
age INT,
sib_sp INT,
parent_child INT,
fare FLOAT8
);
"""

pg_curs.execute(create_passengers_table)

for passenger in passengers:
    insert_passenger = """
    INSERT INTO passengers
    (survived, pclass, name, sex, age, sib_sp, parent_child, fare)
    VALUES """ + str(passenger[1:]) + ';'
    pg_curs.execute(insert_passenger)

pg_conn.commit()


