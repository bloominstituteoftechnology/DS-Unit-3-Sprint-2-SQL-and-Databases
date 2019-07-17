import psycopg2
import sqlite3
import pandas as pd

DB = 'testOne'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'


def create_table(con):
    pgcur = con.cursor()
    try:
        pgcur.execute(f'DROP TABLE titanic')
    except (psycopg2.ProgrammingError,
            psycopg2.InternalError) as err:
        # Table Does not exist yet.
        pass
    con.commit()
    enums = {
        'sex': ('male', 'female'),
        'pclass': ('1', '2', '3')
    }
    for e in enums.keys():
        vals = enums[e]
        tmplt = ', '.join(['%s' for _ in vals])
        try:
            pgcur.execute(f'DROP TYPE {e}')
        except (psycopg2.ProgrammingError,
                psycopg2.InternalError) as err:
            # Type Does not exist yet.
            pass
        con.commit()
        pgcur.execute(f'CREATE TYPE {e} AS ENUM ({tmplt})', vals)
        con.commit()
    pgcur.execute('''
        CREATE TABLE titanic (
            id SERIAL PRIMARY KEY,
            survived BOOL,
            pclass pclass,
            name VARCHAR (255),
            sex sex,
            age INT,
            siblings_spouses_aboard INT,
            parents_children_aboard INT,
            fare FLOAT);
    ''')
    con.commit()


def populate_table(con):
    pgcur = con.cursor()
    df = pd.read_csv('titanic.csv')
    cols = [col.lower().replace(' ', '_') .replace('/', '_')
            for col in df.columns]
    df.columns = cols

    for row in df.itertuples(index=False, name=None):
        tmplt = ', '.join(['%s' for _ in row])
        colnames = ', '.join([col for col in cols])
        row = list(row)
        # change sirvived to boolean and pclass to string
        row[0] = bool(row[0])
        row[1] = str(row[1])
        pgcur.execute(
            f'INSERT INTO titanic ({colnames}) VALUES ({tmplt})', row)
    con.commit()
    pgcur.execute('SELECT * FROM titanic LIMIT 20')
    res = pgcur.fetchall()
    for item in res:
        print(item)


def main():
    pgcon = psycopg2.connect(
        dbname=DB, user=USER, password=PASSWORD, host=HOST)
    create_table(pgcon)
    populate_table(pgcon)


if __name__ == "__main__":
    main()
