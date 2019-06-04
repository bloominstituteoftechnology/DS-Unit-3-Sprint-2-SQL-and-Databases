import psycopg2

# Re Enter
dbname = 'eczastgf'
user = ''
password = ''
host = ''

# Connect to ElephantSQL
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Read the ElephantSQL database
pg_curs = pg_conn.cursor()

# sqlite3 load titanic database
import sqlite3
import pandas as pd

# Save df
df = pd.read_csv('titanic.csv')

# Reset index to get an index,id
df = df.reset_index().rename(columns={'index':'id'})

# Save a create a titanic database
sl_conn = sqlite3.connect('titanic.sqlite3')

# CREATE TYPE for titanic sex
# CREATE TABLE for titanic database
create_titanic_table = '''
    CREATE TABLE titanic (
        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        survived INT,
        pclass INT,
        name VARCHAR(100),
        sex VARCHAR(10),
        age INT,
        siblings_spouses_aboard INT,
        parents_child_aboard INT,
        fare INT
    );
'''

# Read the database
sl_curs = sl_conn.cursor()

# Create the table for the titanic database
#sl_curs.execute(create_titanic_table)
## Comment out since already created

# Define INSERT INTO
insert_titanic_db = '''
    INSERT INTO titanic
    VALUES ''' + str(tuple(df.loc[0, :].tolist()))

sl_curs.execute(insert_titanic_db)

# Fetch all data in titanic database
print(sl_curs.execute('SELECT * FROM titanic;').fetchall())