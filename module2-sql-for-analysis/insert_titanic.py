import pandas as pd
import sqlite3
import psycopg2

# Import CSV as a DataFrame
df = pd.read_csv('titanic.csv')

# Prepare Data For Conversion to Postgres
df['Survived'] = df['Survived'].replace({0:'no', 1:'yes'})
df['Pclass'] = df['Pclass'].replace({1:'first',2:'second',3:'third'})
# Note, need to remove apostrophes from Names to avoid conflict with Postgres
df['Name'] = df['Name'].str.replace(r"[\"\',]", '')

# Convert DataFrame to SQlite3
sl_conn = sqlite3.connect('titanic.sqlite3')
df.to_sql(name='passengers', con=sl_conn, if_exists='replace')
sl_curs = sl_conn.cursor()

# Extract observation in list format from SQLITE3
people = sl_curs.execute('SELECT * FROM passengers;').fetchall()

# Input Credentials for Postgres DB
dbname = 'NAME'
user = 'NAME'
password = 'PASSWORD'
host = 'raja.db.elephantsql.com'

# Connect to remote Postgres DB
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Create Enumerated Types for table schema
pg_curs.execute("CREATE TYPE gender AS ENUM ('male', 'female');")
pg_curs.execute("CREATE TYPE class AS ENUM ('first', 'second', 'third');")
pg_curs.execute("CREATE TYPE survive AS ENUM ('no', 'yes');")

# Create schema for passenger table
create_passenger_table = """
CREATE TABLE passengers_titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived survive,
    pclass class,
    name text,
    sex gender,
    age DOUBLE PRECISION,
    sibl_spouse_aboard INT,
    parent_child_aboard INT,
    fare DOUBLE PRECISION
)
"""

# Execute create of table in remote Postgres DB
pg_curs.execute(create_passenger_table)

# Insert each person in list created from SQLITE3 table
for person in people:
    insert_person = """
    INSERT INTO passengers_titanic
    (survived, pclass, name, sex, age, sibl_spouse_aboard, parent_child_aboard, fare)
    VALUES """ + str(person[1:])
    pg_curs.execute(insert_person)

# Commit change to remote Postgres server (only runs if rest of file executed without error)
pg_conn.commit()