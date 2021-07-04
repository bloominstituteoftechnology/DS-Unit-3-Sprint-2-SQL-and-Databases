
import psycopg2
from decouple import config

User = config('User')
Password = config('Password')
Server = config('Server')

pg_conn = psycopg2.connect(dbname = User,
                           user = User,
                           password = Password,
                           host = Server)

pg_curs = pg_conn.cursor()

#pg_curs.execute('SELECT * FROM test_table;')
#pg_curs.fetchall()

#pg_curs.execute('''
#CREATE TYPE pcla AS ENUM ('First', 'Second', 'Third');
#CREATE TYPE gndr AS ENUM ('Female','Male');
#CREATE TYPE status AS ENUM ('survived', 'perished');
#'''
#)

pg_curs.execute('''
CREATE TABLE titanic_manifest (
  pid int PRIMARY KEY,
  name varchar(100),
  pclass pcla,
  gender gndr,
  surv status,
  age int,
  ss_abd int,
  pc_abd int,
  fare real
);
'''
)

pg_conn.commit()
pg_conn.close()
