import psycopg2

dir(psycopg2)

# very much like sqlite3 api 
# help(psycopg2.connect)

# don't commit this 
dbname = 'hwtvsmxc'
user = 'hwtvsmxc'
password = '7ybnvCKf2B8jjrnIhaMpsGvvnmM9o8fi' 
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)


# connection object
pg_conn

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

