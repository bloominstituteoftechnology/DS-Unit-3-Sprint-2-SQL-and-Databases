
import psycopg2
#for connection to elephantsql
import sqlite3 as sql
import pandas as pd

#elephantsql conventions
dbname = 'ijpwepjo'
user = 'ijpwepjo'
password = 'ucEObTZwD7mDk9sa2lmT428Vy3NhwtMn'
host = 'salt.db.elephantsql.com'

#elephantsql conventions
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

#creating cursor to connect to elephantsql
pg_cursor = pg_conn.cursor()

#write and execute command to delete any previous table
delete_table = "DROP TABLE IF EXISTS titanic_table"
pg_cursor.execute(delete_table)

#read in Titanic data; remove apostrophes from names
TitanicData = pd.read_csv('titanic.csv')
TitanicData.Name = TitanicData.Name.replace("'", '', regex=True)

# create command for postgres table, name columns and datatypes
create_titanic_table ="""
CREATE TABLE titanic_table (
    id SERIAL PRIMARY KEY,
    "survived" INT,
    "pclass" INT,
    "name" TEXT,
    "sex" TEXT,
    "age" INT,
    "siblingsspouses" INT,
    "parentschildren" INT,
    "fare" FLOAT
);
"""
# execute command to create table
pg_cursor.execute(create_titanic_table)

#for loop to populate table with tuples from dataframe
for i in TitanicData.to_records(index=False):
    insertinfo ="""
        INSERT INTO titanic_table
            (survived, pclass, name, sex, age, siblingsspouses,
            parentschildren, fare)
            VALUES
            """ + str(i) + ';' #change tuple to string
    pg_cursor.execute(insertinfo) #execute putting tuple df data in table

pg_cursor.close()
pg_conn.commit()
