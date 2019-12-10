import psycopg2

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()