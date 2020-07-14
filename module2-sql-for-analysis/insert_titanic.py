# Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
# thinking about the schema to make sure it is appropriate for the columns.
# [Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
# be useful. Once it is set up, write a `insert_titanic.py` script that uses
# `psycopg2` to connect to and upload the data from the csv, and add the file to
# your repo. Then start writing PostgreSQL queries to explore the data!

import sqlite3
import psycopg2
import pandas as pd 

#read in csv 
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'"," ")

df.info()

#create sqlite3 
conn = sqlite3.connect('titanic.sqlite3')
#create cursor 
curs = conn.cursor()
#convert to sql 
df.to_sql('titanic', conn)

#pulling out data from the sql base we just made
get_titanic = 'SELECT * FROM titanic;'
passangers = curs.execute(get_titanic).fetchall()

#put info and connect elephant 
dbname = 'njskuvoi'
user = 'njskuvoi'
password = 'V4hoTmOL2IlAb_98ylcdRtErA_ERzFMo'
host = 'ruby.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

create_table_statement = """

CREATE TABLE titanic1 ( 
    id SERIAL PRIMARY KEY, 
    Survived INTEGER,
    pclass INTEGER,
    name VARCHAR (140),
    sex VARCHAR (10),
    age FLOAT(1),
    siblings_spouses_aboard INTEGER, 
    parents_children_aboard INTEGER,
    fare FLOAT(4) 
);
"""
#CREATE NEW CURSOR 
pg_curs = pg_conn.cursor()

#EXECUTE 
pg_curs.execute(create_table_statement)

for x in passangers:
    insert_passanger = """
    INSERT INTO titanic1 
    (Survived, Pclass, Name, Sex, Age, 
    Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES """ + str(x[1:]) + ";"
    pg_curs.execute(insert_passanger)


pg_conn.commit()

