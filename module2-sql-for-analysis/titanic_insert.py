import pandas as pd
import sqlite3
import psycopg2

#Login Information
dbname = 'mtjkhpkq'
user = 'mtjkhpkq'
password = '' 
host = 'salt.db.elephantsql.com'

#connection & cursor
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

#Create db titanic.sqlite3 & cursor
t_conn = sqlite3.connect("titanic.sqlite3")
t_curs = t_conn.cursor() 

#Import titanic.csv
df = pd.read_csv('titanic.csv')
titanic_data.to_sql('Titanic',t_vonn, index_label='id')

create_titanic_table = """
 CREATE TABLE titanic_table (
 survived INT,
 pclass INT,
 name VARCHAR (110),
 sex  VARCHAR(10),
 age FLOAT,
 siblingsSpouses INT,
 parentsChildren INT,
 fare FLOAT
 );
 """

pg_curs.execute(create_titanic_table)
titanic_list= sl_curs.execute("SELECT * FROM Titanic").fetchall()

for n in titanic_list:
    insertinfo = """
        INSERT INTO titanic_table
        (survived, pclass, name, sex, age, siblingsSpouses,
        parentsChildren, fare)
        VALUES """ + str(n[1:]) + ';'
    pg_curs.execute(insertinfo)

# pg_curs.fetchall()
pg_curs.close()
pg_conn.commit()