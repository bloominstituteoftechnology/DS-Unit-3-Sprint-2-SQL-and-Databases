import psycopg2
import pandas as pd
import sqlite3
import helper
from settings import secrets


def load_dataset(fpath, verbose=False):
    df = pd.read_csv(fpath)
    df['Name'] = df['Name'].str.replace("'", "")
    if verbose:
        print('Shape  is: ', df.shape)
        print('-'*80)
        print('Pandas Data Frame')
        print(df.head())
        print('-'*80, '\n')
    return df


# Load titanic data set to dataframe
print('Loading dataset...')
titanic = load_dataset('titanic.csv', verbose=True)
print('-'*80, '\n')


# Convert CSV to SQLite database
print('------------------( ETL ) CSV to SQLite ------------------')
print('Converting...')
db_file = 'titanic.sqlite3'
sql_conn = helper.create_connection(db_file)
titanic.to_sql('titanic', sql_conn, if_exists='replace',
               index_label='id')
print('Done')


# Print rows from the SQlite database titanic table
print('------------------ TITANIC DATAFRAME 10 ROWS ------------------')
query = "SELECT * FROM titanic"
passengers = helper.select_all_query(db_file, query)
df = pd.read_sql(query, sql_conn)
print(df.head())
print('-'*80, '\n')


# Print data type of SQLite titanic table
print('------------------ DATA TYPE OF TITANIC TABLE ------------------')
pragma_result = sql_conn.execute(
    'PRAGMA table_info(titanic);').fetchall()
for row in pragma_result:
    print(row)
print('-'*80, '\n')


# Connect to Postgre SQL database in Elephant SQl Server
dbname = secrets.get('dbname')
user = secrets.get('user')
password = secrets.get('password')
host = secrets.get('host')


print('------------------( ETL ) SQLite to PostgreSQL ------------------')
print(f'Connecting to {dbname}')
print(f'Host is: {host}')

try:
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
except:
    print("I am unable to connect to the database")

# Create Cursor
pg_curs = pg_conn.cursor()

# Drop table if exists
pg_curs.execute("DROP TABLE IF EXISTS titanic")
pg_conn.commit()

# Create titanic table in PostgreSQL
create_titanic_table = """
CREATE TABLE titanic (
    passenger_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(200),
    sex VARCHAR(20),
    age REAL,
    siblings_spouses INT,
    parents_children INT,
    fare REAL
)
"""
pg_curs.execute(create_titanic_table)
pg_conn.commit()


for passenger in passengers:
    insert_passenger = """INSERT INTO titanic
(passenger_id, survived, pclass, name, sex, age, siblings_spouses, parents_children, fare)
VALUES """ + str(passenger) + ';'
    pg_curs.execute(insert_passenger)

    # print(insert_passenger)

pg_conn.commit()

# Print rows from the Postgres titanic table
print('------------------ TITANIC DATAFRAME 10 ROWS ------------------')
query = "SELECT * FROM titanic LIMIT 10;"
passengers = helper.select_all_query(db_file, query)
df = pd.read_sql(query, pg_conn)
print(df.head())
print('-'*80, '\n')
