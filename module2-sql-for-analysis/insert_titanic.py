import pandas as pd
import sqlite3
import psycopg2

"""Remove (') from names"""
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")

"""Make sqlite3 file and connect to cursor"""
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

"""data from df to sql file"""
df.to_sql('titanic', conn, index=False, if_exists = 'replace')

"""Look at datatable and dattypes"""
x_curs = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'
x_curs.execute(query).fetchall()

titanic = x_curs.execute('SELECT * FROM titanic;').fetchall()
x_curs.execute('PRAGMA table_info(titanic);').fetchall()

"""Connect psycopg2"""
dbname = 'askuvppm'
user = 'askuvppm'
password = 'wuWrTwrCn1UoR92DecFFLZaT4CRxZSOg'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_conn
pg_curs = pg_conn.cursor()

"""Create table and execute"""
titanic_table = """
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name TEXT,
        Sex TEXt,
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Abroad INT,
        Fare REAL
);
"""
pg_curs.execute(titanic_table)

"""Insert"""
for t in titanic:
    insert_titanic = """
      INSERT INTO titanic
      (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Abroad, Fare)
        VALUES """ + str(titanic[1:]) + ';'
    pg_curs.execute(insert_titanic)

pg_curs.execute('SELECT * FROM titanic;')
pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()
