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


def run_conversion(pgres_cur):
    # __________
    csv_url = "titanic.csv"
    df = pd.read_csv(csv_url)
    vals = df.to_csv(index=False, header=None)
    print(df.head(5))
    print(vals)
    return


def main():
    # ____ Connect to an ElephantSQL __________
    pgres_str = """
    dbname='zoafqkfp' user='zoafqkfp'
    host='TODO'
    password='TODO'
    """
    pgres_conn = conx_elephant(pgres_str)

    # ____ create cursor ___
    pgres_cur = pgres_conn.cursor()

    # ____ Port titanic.csv to Postgres ___
    run_conversion(pgres_cur)

    # ___ end main ___________
    pgres_cur.close()   # close cursor
    pgres_conn.close()  # close connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
