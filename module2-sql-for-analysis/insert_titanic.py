import psycopg2
import sqlite3

### Connect to ElephantSQL-hosted PostgreSQL
pg_conn = psycopg2.connect(dbname='assmldlq', user='assmldlq',
                        password=input('Enter Password: '), 
                        host='raja.db.elephantsql.com')

### A "cursor", a structure to iterate over db records to perform queries
pg_curs = pg_conn.cursor()

### connect to sqlite3 titanic db
sl_conn = sqlite3.connect('titanic.sqlite3')

### cursor to iterate over db records
sl_curs = sl_conn.cursor()


pg_curs.execute("DROP TABLE IF EXISTS titanic_table")

create_titanic_table = """
CREATE TABLE titanic_table (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass SMALLSERIAL,
    name VARCHAR(100),
    sex VARCHAR(10),
    age SMALLSERIAL,
    siblings_and_spouses SMALLSERIAL,
    parents_and_children SMALLSERIAL,
    fare REAL
)
"""

sl_curs.execute("""
UPDATE titanic
SET Name = REPLACE(Name, "'", " ")
""")

pg_curs.execute(create_titanic_table)

passengers = sl_curs.execute('SELECT * FROM titanic').fetchall()

for passenger in passengers[1:]:
    insert_passenger = """
        INSERT INTO titanic_table
        VALUES""" + str(passenger)
    pg_curs.execute(insert_passenger)
pg_conn.commit()



