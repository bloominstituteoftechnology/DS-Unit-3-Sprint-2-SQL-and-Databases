import psycopg2 
import sqlite3
import pandas as pd

dbname = 'xindmaoa'
user = 'xindmaoa'
password = 'Xw7UVM2_zcJIP7td-LIHWNDMceV2JeKp'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
                           password = password, host = host)
pg_curs = pg_conn.cursor()

query = """
        SELECT * FROM titanic
        WHERE titanic.Survived = 1;
        """
pg_curs.execute(query)
print(pg_curs.fetchall())