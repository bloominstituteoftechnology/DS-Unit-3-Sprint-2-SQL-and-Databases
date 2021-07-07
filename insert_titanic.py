"""Code for moving a csv to postgreSQL"""

import psycopg2
import sqlite3
import pandas as pd
df = pd.read_csv('C:/Users/Phatdeluxe/lamdata/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv')

df['Name'] = df['Name'].replace(to_replace={"'": " "}, regex=True)

df['Name'].head()

sl_conn = sqlite3.connect('titanic_dataset.sqlite3')
sl_curs = sl_conn.cursor()


df.to_sql('var12', con=sl_conn)


dbname = 'qpjhbufi'
user = 'qpjhbufi'
password = 'W1NW1ePJWdJx1NsKlJqqxoi3PC4xAtB7'
host = 'salt.db.elephantsql.com'


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


titanic_pass = sl_curs.execute('SELECT * FROM var12;').fetchall()

titanic_pass[6]

new_table = '''
    CREATE TYPE sex AS ENUM ('male', 'female');
    CREATE TABLE titanic_data (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex sex,
        Age INT,
        Siblings_Spouses_Aboard INT,
        Parents_Children_Aboard INT,
        Fare FLOAT
    );'''


pg_curs.execute(new_table)


for passenger in titanic_pass:
    insert_passenger = '''
    INSERT INTO titanic_data
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES ''' + str(passenger[1:]) + ';'
    pg_curs.execute(insert_passenger)


pg_curs.close()
pg_conn.commit()
