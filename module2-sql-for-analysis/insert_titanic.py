import psycopg2
import sqlite3
import pandas as pd

dbname = 'INSERT'
user = 'INSERT'
password = 'INSERT'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_conn
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')

df = pd.read_csv('titanic.csv')
# apostrophes in names make data loading difficult, so...
df['Name'] = df['Name'].str.replace("'", "")
df.to_sql('titanic', con=sl_conn, if_exists='replace')

sl_curs = sl_conn.cursor()
titanic = sl_curs.execute('SELECT * FROM titanic;').fetchall()

create_titanic_table = """
    CREATE TABLE titanic_upload (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name TEXT,
        Sex TEXT,
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare FLOAT
    );
"""
pg_curs.execute(create_titanic_table)

for passenger in titanic:
    insert_passenger = """
        INSERT INTO titanic_upload
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, 
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ';'
    pg_curs.execute(insert_passenger)

pg_curs.close()
pg_conn.commit()