""" set up a new table for the Titanic data (titanic.csv) """
import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import sqlite3

def load_data(filepath):
    df = pd.read_csv(filepath)
    print('Shape is ', df.shape)
    print('-'*80)
    print('Pandas Dataframe')
    print(df.head(5))
    print('-'*80)
    return df

#Loading titanic dataset into dataframe
filepath = 'titanic.csv'
titanic= load_data(filepath)

#Convert CSV to sqlite database
dbfile ='titanic.sqlite3'
#conn = sqlite3.connect(titanic.sqlite3)
def create_connection(dbfile):
    '''creating connection to the new database file'''
    conn = sqlite3.connect(dbfile)
    return conn

sql_conn = create_connection(dbfile)   
titanic.to_sql('titanic', sql_conn, if_exists= 'replace', index_label= 'id')

# # Print rows from sqlite database titanic table

query = 'SELECT * FROM titanic;'
def run_queries(query):
    '''Excute query from database table'''
    conn = create_connection(dbfile)
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    return results
    

print('--------Titanic Dataframe 5 Rows--------')
passengers = run_queries(query)
df1 = pd.read_sql(query, sql_conn)
print(df1.head())


#Connect to the Postgre Database in Elephant SQL sever

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")


pg_conn= psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)
# Create cursor
pg_curs = pg_conn.cursor()
# Drop table if exists
pg_curs.execute("DROP TABLE IF EXISTS titanic")
pg_conn.commit()

#creating titanic table in PostgreSQL
create_titanic_table ="""
CREATE TABLE titanic(
    passanger_id  SERIAL PRIMARY KEY,
    servived  INT,
    pclass  INT,
    name  VARCHAR(80),
    sex  VARCHAR(20),
    age REAL,
    siblings_spouses INT,
    parents_children INT,
    fare REAL 
)
"""
pg_curs.execute(create_titanic_table)
pg_conn.commit()

# for passenger in passengers:
#     insert_passenger = """INSERT INTO titanic
# (passenger_id, survived, pclass, name, sex, age, siblings_spouses, parents_children, fare)
# VALUES """ + str(passenger) + ';'
#     pg_curs.execute(insert_passenger)

    # print(insert_passenger)



insert_query ='''INSERT INTO titanic(servived, pclass, name, sex, age,
        siblings_spouses, parents_children, fare)
         VALUES(0,3, 'Mr. Owen Harris Braund', 'male',22,1,0,7.25),
        (1,1, 'Mrs. John Bradley (Florence Briggs Thayer) Cumings', 'female',38,1,0,71.2833)'''

pg_curs.execute(insert_query)
pg_conn.commit()
query = "SELECT * FROM titanic LIMIT 2;"
pg_curs.execute(query)
results= pg_curs.fetchall()
df2 = pd.read_sql(query, pg_conn)
print(df2.head())
print('-'*80, '\n')
