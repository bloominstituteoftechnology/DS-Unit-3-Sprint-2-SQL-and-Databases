#!/usr/bin/env/python
# the above command is called shebang to tell the computer to execute
# the following code using avaialble python
""" Exmaple of moving data from rpg_db.sqlite3 to PostgreSQL"""

import sqlite3
import psycopg2 as pg

# get the data from sqlite3
sql_conn = sqlite3.connect(
    "/home/mishraka/repos/manjulamishra/titanic.sqlite3")
results = sql_conn.execute(
    'SELECT * FROM titanic;').fetchall()


#  Create table and insert data in PostgreSQL
create_titanic_table = """ CREATE TABLE passangers(
    Survived int,
    Pclass int,
    Name varchar(30),
    Sex text,
    Age int,
    Siblings_SpousesAboard int,
    Parents_ChildrenAboard int,
    Fare NUMERIC
);"""


# Assume user defines database parameters
dbname = 'wywlalgk'
user = 'wywlalgk'
password = 'vb6ja9HHMnqH2QMzocJuuGSRxJEVKHaJ'
host = 'stampy.db.elephantsql.com'

pg_conn = pg.connect(dbname=dbname, user=user, password=password, host=host)


def make_and_populate_titanic_table():
    pg_curs = pg_conn.cursor()

    pg_curs.execute(create_titanic_table)

    for result in results:
        insert_result = """INSERT INTO passangers
    (Survived, Pclass, Name, Sex, Age,
     Siblings_SpousesAboard, Parents_ChildrenAboard, Fare)
    VALUES""" + str(result[1:])
        pg_curs.execute(insert_result)

    pg_conn.commit()


def euler_phi(n):
    y = n
    for i in range(2, n+1):
        if isPrime(i) and n % i == 0:
            y *= 1 - 1.0/i
    return int(y)
