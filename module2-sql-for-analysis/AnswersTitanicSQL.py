import psycopg2

dbname = 'lqsujdux' 
user = 'lqsujdux' 
password =  'w7ih63BvRfpV_Mf9suEjW-6NmOGaTcP-'
host =  'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
pg_curs = pg_conn.cursor()

import sqlite3
import pandas as pd

sl_conn = sqlite3.connect('titanic.sqlite3')

# transform the titanic csv into a database that i can connect to using sqlite
df = pd.read_csv('https://raw.githubusercontent.com/EvidenceN/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
df.head()

def clean(x):
    
    x['Name'] = x['Name'].str.replace("'","`")
    
    return x

new_df = clean(df)

data = new_df.to_sql(name = 'titanic', con=sl_conn)

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT * FROM titanic').fetchone()

sl_curs.execute('PRAGMA table_info(titanic);').fetchall()

create_titanic_table = """
    CREATE TABLE titanic(
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare REAL);
"""
pg_curs.execute(create_titanic_table)

show_tables = """
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

original_titanic = sl_curs.execute('SELECT * FROM titanic').fetchall()

original_titanic[0]
 
str(original_titanic[4][1:])
 
for people in original_titanic:
    insert_data = """
        INSERT INTO titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, 
        Parents_Children_Aboard, Fare)
        VALUES """ + str(people[1:]) + ";"
    pg_curs.execute(insert_data)
 
pg_curs.close()
pg_conn.commit()
 
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host) #reopened connection
pg_curs = pg_conn.cursor() #reopened the cursor
 
pg_curs.execute('SELECT * FROM titanic;')
new_titanic = pg_curs.fetchall()
 
original_titanic[0:3]

new_titanic[0:3]
 
# somethings match exactly, and some things don't
for data, pg_data in zip(original_titanic, new_titanic):
    if data[1:] == pg_data:
        print('hurray')
    else:
        print('cry')
