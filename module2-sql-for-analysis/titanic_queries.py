"""
----------------------------------------------------------------
             RPG DataBase Queries
----------------------------------------------------------------
"""
import psycopg2


# ___ Connect to ElephantSQL db _________
def conx_elephant(conx_str):
    # instantiate and return connection obj
    cnx = psycopg2.connect(conx_str)
    return cnx


# ___ QUERIES _________________________________
def run_queries(c):
    print('----- T I T A N I C   I N F O ------')
    # _____ How Many Total pASSENGERSs_____________________
    query = """
    SELECT COUNT(public.titanic.index)
    FROM public.titanic
    """
    c.execute(query)
    rows = c.fetchone()
    print('There were a total of', rows[0], 'passengers')

    query = """
    SELECT COUNT(public.titanic.index)
    FROM public.titanic
    WHERE public.titanic."Survived" > 0
    """
    c.execute(query)
    rows = c.fetchone()
    print(rows[0], 'passengers survived')

    query = """
    SELECT COUNT(public.titanic.index)
    FROM public.titanic
    WHERE public.titanic."Survived" < 1
    """
    c.execute(query)
    rows = c.fetchone()
    print(rows[0], 'passengers DID NOT')


def main():
    conx_str = """
    dbname='zoafqkfp' user='zoafqkfp'
    host='stampy.db.elephantsql.com'
    password='MCJu21HwCynkStIs3FOmV-xHXSAXOSDD'
    """
    conn = conx_elephant(conx_str)
    cur = conn.cursor()  # create cursor
    run_queries(cur)
    cur.close()
    conn.close()   # Close the connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
