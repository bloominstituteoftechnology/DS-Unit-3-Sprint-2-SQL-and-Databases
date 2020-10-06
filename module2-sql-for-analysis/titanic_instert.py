import psycopg2
import sqlite3

pg_dbname = "vkrdlbel"
pg_user= "vkrdlbel"
pg_password = "luzKEtW5bsdypA4gwGerKxZ76WI00PyU"
pg_host = "topsy.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname = pg_dbname,
                           user = pg_user,
                           password = pg_password,
                           host = pg_host)

pg_curs = pg_conn.cursor()

pg_curs.close()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

get_passengers = "SELECT * FROM titanic;"
sl_curs.execute(get_passengers)
passengers = sl_curs.fetchall()
sl_curs.execute('PRAGMA table_info(titanic);')
sl_curs.fetchall()

create_titanic_passengers_table = """
CREATE TABLE titanic_passengers_3(
    id SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name TEXT, 
    Sex TEXT,
    Age INT, 
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare INT
);
"""

def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname = pg_dbname, user = pg_user, password = pg_password, host = pg_host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs
pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)


# Commiting table to instance
pg_curs.execute(create_titanic_passengers_table)
pg_conn.commit()


# Inserting characters into empty table
for passenger in passengers:
  insert_passenger = """
    INSERT INTO titanic_passengers_3
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES """ + str(passenger).replace('"', "'") + ";"
  pg_curs.execute(insert_passenger)


# Commiting to database
pg_conn.commit()
