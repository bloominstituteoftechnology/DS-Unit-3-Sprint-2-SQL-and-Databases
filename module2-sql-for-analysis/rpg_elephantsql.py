import psycopg2

dbname = 'lsustohi'
user = 'lsustohi'
password = '?'
host = 'rajje.db.elephantsql.com'

#Create connection and cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()



