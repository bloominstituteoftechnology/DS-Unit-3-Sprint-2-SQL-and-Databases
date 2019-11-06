#!/usr/bin/env python3

import psycopg2
import sqlite3
import os
import pandas as pd

dbname = 'nsvybuvb'
user = 'nsvybuvb' # same as dbname
password= 'ZSQQPpNjrb78uZJLGrGliTLdiTaWCAK5' # not my real password
password = 'MFDDCcAweo78hMWYTeTyvGYqvGnJPNX5'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

# create types for two of the titanic data columns to limit input
create_pclass = "create type pclass as enum ('1','2','3');"
create_sex = "create type sex as enum ('male','female');"

pg_curs.execute(create_pclass)
pg_curs.execute(create_sex)

# create empty passenger table to be exported into postgres later
create_passenger_table = """
create table passengers (
passenger_id serial primary key,
survived boolean,
pclass pclass,
name varchar(100),
sex sex,
age int,
sibling_spouse_aboard int,
parents_children_aboard int,
fare real);
"""

pg_curs.execute(create_passenger_table)


# Open local titanic dataset with pandas, modify and save data to sqlite3 

## remove file if it exists so an "already exists error" is not thrown
os.system('rm titanic.sqlite3')

infile = 'titanic.csv'
df = pd.read_csv(infile)
## pclass is a type created above defined to be strings, so it must be changed in the dataframe for consistancy. Similarly, the booleans: "Survived", "Siblings..." and "Parents..." are changed to strings because that's how postgres takes booleans. Age is an int 
df.Pclass = df.Pclass.astype(str) 
df.Survived = df.Survived.astype(str)
df.Age = df.Age.astype(int)

sl_conn = sqlite3.connect('titanic.sqlite3')
df.to_sql('titanic.sqlite3',con=sl_conn,index=False) # index= True serves as primary key



# Store passengers from sqlite, send to postgres
sl_curs = sl_conn.cursor()
passengers = sl_curs.execute('select * from "titanic.sqlite3";').fetchall()

add_passenger_query = """
insert into passengers
(survived, pclass, name, sex, age, sibling_spouse_aboard, parents_children_aboard, fare)
values (%s, %s, %s, %s, %s, %s, %s, %s);
"""

## using curs.execute sanitizes the input, avoiding SQL injection attacks
for p in passengers:
    print(f"adding information for passenger: {p[2]}")
    pg_curs.execute(add_passenger_query, p)
    #print(pg_curs.mogrify(add_passenger_query,p)) # displays formated text for preview


# close cursor and commit changes to postgres

pg_curs.close()
pg_conn.commit()



