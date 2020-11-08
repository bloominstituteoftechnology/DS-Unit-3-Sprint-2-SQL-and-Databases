import sqlite3
from demo_queries import run_queries


def conx_sqlite(db_filename):
    conn = sqlite3.connect(db_filename)
    return conn


def create_tables(c, conn):
    # ___ Create table ____________________________________________
    create_script = '''
    CREATE TABLE demo (
    s TEXT NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL
    );
    '''
    c.execute(create_script)
    conn.commit()
    return


def insert_data(c, conn):
    # ___ Insert data ______________________________________
    c.execute('INSERT INTO demo VALUES("g",3,9);')
    c.execute('INSERT INTO demo VALUES("v",5,7);')
    c.execute('INSERT INTO demo VALUES("f",8,7);')
    conn.commit()
    return


def verify_output(cur):
    # ___ Print out a List __________________________________________
    for row in cur.execute('SELECT * FROM demo'):
        print(row[1])
    return


def main():
    # ____ connect to db ____
    conn = conx_sqlite('demo_data.sqlite3')
    cur = conn.cursor()

    # _____  Process ______
    # create_tables(cur, conn)
    # insert_data(cur, conn)

    run_queries(cur)

    # ___end main ________
    cur.close()
    conn.close()
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
