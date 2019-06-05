import psycopg2
import sqlite3
import pandas as pd

# Import titanic data into DataFrame
df = pd.read_csv('titanic.csv')

# Cleaning up column names
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
df = df.rename(columns={'siblings_spouses_aboard': 'siblings_spouses', 'parents_children_aboard': 'parents_children'})

# Convert DataFrame to sqlite3 database
sl_conn = sqlite3.connect('Titanic.sqlite3')
sl_curs = sl_conn.cursor()
df.to_sql('Titanic', con=sl_conn)

# Postgresql login credentials
dbname = 'xgbbacwp'
user = 'xgbbacwp'
password = 'mJroxQrHR5UAZ0hTGw0DlCg0X8FQTKe_'
host = 'raja.db.elephantsql.com'

# Create a connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)
pg_curs = pg_conn.cursor()

# Add Titanic table to postgresql database
create_titanic_table = """
CREATE TABLE Titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(100),
    sex VARCHAR(6),
    age INT,
    siblings_spouses INT,
    parents_children INT,
    fare FLOAT(2)
)
"""
pg_curs.execute(create_titanic_table)

# Select passenger data
passengers = sl_curs.execute('SELECT * FROM Titanic;').fetchall()

# Add passenger data to Titanic table
for passenger in passengers:
    insert = '''INSERT INTO Titanic(
        passenger_id, survived, pclass, name, sex, age, siblings_spouses, 
        parents_children, fare) VALUES''' + str(tuple(passenger))
    pg_curs.execute(insert)

pg_conn.commit()

# Create new cursor and inspect data
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM Titanic;')
pg_passengers = pg_curs.fetchall()
len(pg_passengers)
