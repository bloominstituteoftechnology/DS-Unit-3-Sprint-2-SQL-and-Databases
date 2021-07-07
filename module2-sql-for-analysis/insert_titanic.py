import psycopg2
import sqlite3
import csv

dbname = 'ejnhvpax'
user = 'ejnhvpax'
password = 'BLANK'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)


def transfer_postgre(pg_conn):
    pg_curs = pg_conn.cursor()
    create_enumerated_type = """
    CREATE TYPE gender AS ENUM ('male', 'female');
    """
    create_titanic_table = """
        CREATE TABLE titanic (
            person_id SERIAL PRIMARY KEY,
            survived INT,
            pclass INT,
            name TEXT,
            sex gender,
            age NUMERIC (4,1),
            siblings_spouses_aboard INT,
            parents_children_aboard INT,
            fare NUMERIC (5,2)
        );
    """
    pg_curs.execute(create_enumerated_type)
    pg_curs.execute(create_titanic_table)

    with open('titanic.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            pg_curs.execute(
            "INSERT INTO titanic (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",row)

    pg_curs.close()
    pg_conn.commit()


# def test(pg_conn):
#     pg_curs = pg_conn.cursor()
#     pg_curs.execute('SELECT * FROM titanic;')
#     pg_titanic = pg_curs.fetchall()

#     for data, item in zip(df, pg_titanic):
#         assert data == item

#     assert len(df) == len(pg_titanic)
#     pg_curs.close()
#     pg_conn.commit()


transfer_postgre(pg_conn)
# test(pg_conn)