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
        # ____ Connect to an ElephantSQL __________
    dbname = ''
    user = ''
    host = ''
    passw = ''
    file = open('elephant.pwd', 'r')
    ctr = 1
    for line in file:
        line = line.replace('\n', '')
        if ctr == 1:
            dbname = line
        if ctr == 2:
            user = line
        if ctr == 3:
            host = line
        if ctr == 4:
            passw = line
        ctr = ctr + 1
    conx_str = 'dbname=' + dbname + ' user=' + user + ' host=' + host + ' password=' + passw
    conn = conx_elephant(conx_str)
    cur = conn.cursor()  # create cursor
    run_queries(cur)
    cur.close()
    conn.close()   # Close the connection
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
