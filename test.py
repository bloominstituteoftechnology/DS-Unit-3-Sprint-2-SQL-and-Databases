import psycopg2
import wget
import sqlite3

dbname = 'FoodSquad'
user = 'Admin-Jordan'
password = 'EvYctGaMX3Yt8qQ'
host = 'https://a2plcpnl0542.prod.iad2.secureserver.net'

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host )

pg_conn

pg_curs = pg_conn.cursor()

pg_curs

pg_curs.execute('SELECT * FROM users;')
print(pg_curs.fetchall())