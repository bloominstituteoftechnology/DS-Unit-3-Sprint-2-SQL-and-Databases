import psycopg2
# print(dir(psycopg2))
dbname = 'hvvolzee'
user = 'hvvolzee'
password = 'dAKXw5LOi5bSb_IZtRP6yXMG0jddM_qD'  # Don't commit or share this for security purposes!
host = 'rajje.db.elephantsql.com'  # Port should be included or default
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
#print(pg_conn)
pg_curs = pg_conn.cursor()

import sqlite3
import pandas as pd

df = pd.read_csv('/Users/julie/Desktop/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv')
print(df.head())
print(df.shape)

df['Name']= df['Name'].str.replace("'","")
print(df.head())

df_conn=sqlite3.connect('titanic.sqlite3')
df_curs = df_conn.cursor()
df.to_sql('titanic',df_conn,if_exists='replace')
titanic=df_curs.execute('SELECT * FROM titanic').fetchall()
print(df_curs.execute('PRAGMA table_info(titanic);').fetchall())
create_titanic_table ="""
CREATE TABLE IF NOT EXISTS Titanic(
    index INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex Text,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare REAL

);"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()

for x in titanic:
  insert_x = """
    INSERT INTO Titanic
    (Survived, Pclass, Name, Sex,Age, Siblings_Spouses_Aboard,  Parents_Children_Aboard, Fare)
    VALUES """ + str(x[1:]) + ";"
  pg_curs.execute(insert_x)

  pg_curs.execute('SELECT * FROM Titanic')
  pg_x=pg_curs.fetchall()
  pg_conn.commit()
  