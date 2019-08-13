import psycopg2

dbname = 'anhydaff'
user = 'anhydaff'
password = '08yEUwXsZ6Fv2c9Z2DKOxb0-u6qZVSsC'
host = 'raja.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

curs = conn.cursor()

curs.execute('SELECT * FROM test_table;')
asdf = curs.fetchall()

print(asdf)