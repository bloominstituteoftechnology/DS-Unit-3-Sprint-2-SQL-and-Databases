# Imports
import psycopg2
import sqlite3
import pandas as pd

# Set connection variables
dbname = 'itlfjtuh'
user = 'itlfjtuh'
# password = 
host = 'rajje.db.elephantsql.com'

# Create postgreSQL connection and cursor
pg_conn = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host
    )
pg_curs = pg_conn.cursor()

# Read in CSV file
df = pd.read_csv('titanic.csv')

# Remove apostrophes from Name to prevent parsing erros
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')

# Create sqlite connection
sl_conn = sqlite3.connect('titanic.sqlite3')

# Convert to SQL df
df.to_sql('titanic', con=sl_conn, if_exists='replace')

# Create SL cursor
sl_curs = sl_conn.cursor()

# Query to pull all titanic data
query = """SELECT *
FROM titanic
"""
titanic_sql = sl_curs.execute(query).fetchall()

# Create postgreSQL table
create_titanic_table = """
CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(81),
    sex VARCHAR(10),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare REAL
)
"""
pg_curs.execute(create_titanic_table)
pg_conn.commit()

# Insert data into table
for person in titanic_sql:
    insert_person = """
    INSERT INTO titanic
    (survived, pclass, name, sex, age,
    siblings_spouses_aboard, parents_children_aboard, fare)
    VALUES """ + str(person[1:]) + ";"
    pg_curs.execute(insert_person)
pg_conn.commit()

# Look at data to confirm correct
pg_curs.execute('SELECT * FROM titanic LIMIT 5')
pg_table = pg_curs.fetchall()
print(pg_table)
