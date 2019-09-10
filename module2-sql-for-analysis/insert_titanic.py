import sqlite3
import psycopg2
import pandas as pd

# Read in and clean up data for transport to db
df = pd.read_csv('titanic.csv')
df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age',
              'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']
df['Name'] = df['Name'].str.replace("'", "")

# Open connection, and create db in sqlite
sl_conn = sqlite3.connect('titanic_table')
df.to_sql('titanic_table', con=sl_conn, if_exists='replace')
sl_curs = sl_conn.cursor()

# Open connection and cursor to postgreSQL
dbname = 'cwmypbdz'
user = 'cwmypbdz'
password = 'rASy8noJg5Hhuhyn0Mxr_XyY2VVYR9zI'
host = 'salt.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname,
                           user=user,
                           password=password,
                           host=host)
pg_curs = pg_conn.cursor()

# Drop titanic table if it already exists
pg_curs.execute('DROP TABLE IF EXISTS titanic_table')

# Create schema for postgreSQL table
create_titanic_table = """
    CREATE TABLE titanic_table (
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

# Get data from sqlite table
chars = sl_curs.execute('SELECT * FROM titanic_table').fetchall()

# Fill postgreSQL table with data
insert = """
INSERT INTO titanic_table
(Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
 Parents_Children_Aboard, Fare)
VALUES """
for char in chars:
    insert_query = insert + str(char[1:])
    pg_curs.execute(insert_query)

# Get data from postgreSQL table for testing
pg_curs.execute('SELECT * FROM titanic_table')
pg_chars = pg_curs.fetchall()
# Close connections and commit
pg_curs.close()
pg_conn.commit()

sl_curs.close()
sl_conn.commit()

print('''This throws an assertion error at the end but I'm not sure why.
      Here's the two lists of data printed out.''')
print(chars)
print(pg_chars)

# Test that it works - for some reason it doesn't
for char, pg_char in zip(chars, pg_chars):
    print(char, pg_char)
    assert char == pg_chars
