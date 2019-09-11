import psycopg2 as pgres
import pandas as pd


# ___ Connect to ElephantSQL db _________
def conx_elephant(conx_str):
    # instantiate and return connection obj
    cnx = pgres.connect(conx_str)
    return cnx


# _____ DROP table ____________
def drop_table(tbl_name, cur, conn):
    qry = "DROP TABLE " + tbl_name
    cur.execute(qry)
    conn.commit()
    return


# ---- CREATE a new table------------------
def create_table(tbl_name, fields_str, cur, conn):
    qry = "CREATE TABLE " + tbl_name + " " + fields_str + ';'
    cur.execute(qry)
    conn.commit()
    return


def insert_titanic(pgres_cur):
    # __________
    csv_url = "titanic.csv"
    df = pd.read_csv(csv_url)
    df.to_sql('titanic', if_exists='replace', con=pgres_cur, method='multi')
    return


def main():
    # ____ Connect to an ElephantSQL __________
    dbname = ''
    user = ''
    host = ''
    passw = ''
    file = open('elephant.pwd', 'r')
    ctr = 1
    for line in file:
        line=line.replace('\n', '')
        if ctr == 1:
            dbname = line
        if ctr == 2:
            user = line
        if ctr == 3:
            host = line
        if ctr == 4:
            passw = line
        ctr = ctr + 1
    pgres_str = 'dbname=' + dbname + ' user=' + user +' host=' + host + ' password=' + passw

    pgres_conn = conx_elephant(pgres_str)

    # ____ create cursor ___
    pgres_cur = pgres_conn.cursor()

    # ____ Port titanic.csv to Postgres ___
    insert_titanic(pgres_conn)

    # #  _______ verify output  _________
    # query = """
    # SELECT *
    # FROM public.titanic
    # LIMIT 10 ;
    # """
    # print('--- public.titanic table ---')
    # for row in pgres_cur.execute(query).fetchall():
    #     print(row)

    # ___ end main ___________
    pgres_cur.close()   # close cursor
    pgres_conn.close()  # close connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
