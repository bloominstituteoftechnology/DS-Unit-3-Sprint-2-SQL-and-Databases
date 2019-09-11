import pandas as pd
import psycopg2
import sqlite3

#Reproduce demopostgres lecture
#Extract data from csv

df = pd.read_csv("https://raw.githubusercontent.com/Jaydenzk/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv")
df['Name'] = df['Name'].str.replace("'", " ")

# Make sqlite3 file and Connect to get cursor
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()

# data from df into sql file

df.to_sql('titanic', conn, index=False, if_exists='replace')

# check out the data table and see data types
n_curs = conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'

n_curs.execute(query).fetchall()

titanic = n_curs.execute('SELECT * FROM titanic;').fetchall()

n_curs.execute('PRAGMA table_info(titanic);').fetchall()

# connect psycopg2
dbname = 'vlfwvshe'
user = 'vlfwvshe'
password = 'N2IX2e0smqxGQXPP-qRNmYNXvxZk67Yu'  # Don't commit this!
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)


pg_conn
pg_curs = pg_conn.cursor()

#Create table and execute

create_titanic_table = """
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name TEXT,
        Sex TEXT,
        Age REAL,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare REAL
);
"""
pg_curs.execute(create_titanic_table)

#Actual insert

for t in titanic:
    insert_titanic = """
      INSERT INTO titanic
      (Survived, PClass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
        VALUES """ + str(titanic[0]) + ';'

pg_curs.execute(insert_titanic)

pg_curs.close()
pg_conn.commit()
