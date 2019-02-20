#!/usr/bin/env/ python



import sqlite3
import psycopg2 as pg
import csv

sl_conn = sqlite3.connect('../joshdsolis/titanic.db')
curs = sl_conn.cursor()
curs.execute("""CREATE TABLE t (
    Survived int, 
    Pclass int, 
    Name varchar(500), 
    Sex varchar(30), 
    Age int, 
    Siblings_Spouses_Aboard int, 
    Parents_Children_Aboard int, 
    Fare float
);""")


with open('titanic.csv', 'rt') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Survived'], i['Pclass'], i['Name'], i['Sex'],
    i['Age'], i['Siblings/Spouses Aboard'], i['Parents/Children Aboard'],
    i['Fare']) for i in dr]

curs.executemany("""INSERT INTO t (
    Survived, 
    Pclass, 
    Name, 
    Sex, 
    Age, 
    Siblings_Spouses_Aboard, 
    Parents_Children_Aboard, 
    Fare) VALUES (?,?,?,?,?,?,?,?);""", to_db)

sl_conn.commit()
sl_conn.close()


dbname = 'TODO'
user ='TODO'
password='TODO'
host = 'TODO'

 
pg_conn = pg.connect(dbname=dbname, user=user,
                     password=password, host=host)

sl_conn = sqlite3.connect('../joshdsolis/titanic.db')
results = sl_conn.execute('SELECT * FROM t;').fetchall()


def make_and_populate_character_table():
    pg_curs = pg_conn.cursor()

    pg_curs.execute("""CREATE TABLE titanic (
    Survived int, 
    Pclass int, 
    Name varchar(500), 
    Sex varchar(30), 
    Age int, 
    Siblings_Spouses_Aboard int, 
    Parents_Children_Aboard int, 
    Fare float
    );""")

    for result in results:
        insert_result = """INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES""" + str(result)
    
        pg_curs.execute(insert_result)
    pg_conn.commit()
