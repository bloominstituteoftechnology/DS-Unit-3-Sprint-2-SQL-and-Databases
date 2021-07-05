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

create_table_titanic = """
        CREATE TABLE titanic(
            Survived INT,
            Pclass INT,
            Name VARCHAR(100) NOT NULL, 
            Sex VARCHAR(50) NOT NULL,
            Age FLOAT, 
            Sibling_spouse INT, 
            Parents_children INT,
            Fare FLOAT
        )
        """

df = pd.read_csv('titanic.csv')
# pg_curs.execute(create_table_titanic)

csv = open('titanic.csv')
next(csv)
pg_curs.copy_from(csv, 'titanic', sep=',')
pg_conn.commit()

query = """
        SELECT * FROM titanic;
        """
pg_curs.execute(query)
print(pg_curs.fetchall())