import pandas as pd
import psycopg2
import sqlite3

# Connect to ElephantSQL
dbname = ''
user = ''
password = '-'  # Don't commit this!
host = 'raja.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

df = pd.read_csv('titanic.csv')

# Create empty sqlite3 file
sl_conn = sqlite3.connect('titanic.sqlite3')
# Transform df to sql
# df.to_sql('titanic_table', con=sl_conn)
sl_curs = sl_conn.cursor()

# Create empty titanic_table
create_titanic_table = """
CREATE TABLE titanic_table (
    Index SERIAL PRIMARY KEY,
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

titanic_data = sl_curs.execute('SELECT * FROM titanic_table;').fetchall()

for data in titanic_data:
    if '"' in str(data[1:]):
        lst_test = list(data[1:])
        lst_test[2] = lst_test[2].replace("'",' ')
        str_data = str(tuple(lst_test))
    else:
        str_data = str(data[1:])
    insert_data = '''
        INSERT INTO titanic_table (
            Survived, Pclass, Name, Sex, Age,
            Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare
        ) VALUES ''' + str_data + ";"
    # print(insert_data)
    pg_curs.execute(insert_data)

pg_curs.close()
pg_conn.commit()
