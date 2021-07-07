import psycopg2

dbname = 'qtfmqnbz'
user = 'qtfmqnbz'
password = '9tayz5CDYqkpD94mIHclu6lqs7yu3AWD'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

pas_to_keep = 10.58125

q1 = """
SELECT COUNT(name) - COUNT(DISTINCT(name))
FROM titanic
"""

pg_curs.execute(q1)
print(pg_curs.fetchone()[0])

q2 = """
SELECT COUNT(name)
FROM titanic
"""
pg_curs.execute(q2)
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()

a = 10.452069

a = ((a*100)//1)/100

print('AVG:\t'+str(a))
