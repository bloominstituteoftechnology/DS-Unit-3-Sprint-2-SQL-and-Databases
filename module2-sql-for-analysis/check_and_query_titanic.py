import psycopg2
import sqlite3

dbname = 'INSERT'
user = 'INSERT'
password = 'INSERT'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_conn

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic_upload;')
pg_titanic = pg_curs.fetchall()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()
titanic = sl_curs.execute('SELECT * FROM titanic;').fetchall()

# Checking to make sure upload looks right...
for passenger, pg_passenger in zip(titanic, pg_titanic):
    assert passenger[1:] == pg_passenger[1:]

# Querying uploaded database...
query = """
    SELECT Name, Survived FROM titanic_upload
    WHERE Sex = 'female' AND Age < 18;
"""
pg_curs.execute(query)

# Printing results...
print('Name and survival status for females under age 18:')
print(pg_curs.fetchall())