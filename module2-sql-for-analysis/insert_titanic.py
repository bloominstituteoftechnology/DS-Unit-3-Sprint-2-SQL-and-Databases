# Pythonic Python Pythonifies the Pythas.
import psycopg2
import sqlite3
import os
import pandas as pd

# Already done
df = pd.read_csv("./titanic.csv")
df['Name'] = df['Name'].str.replace("'", " ")
# Connect to this special csv; Get cursor for this table
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()
# df.to_sql('titanic', con=conn)

temp_pass = os.environ.get('password')
# Don't even try
temp_user = os.environ.get('username')
host = 'salt.db.elephantsql.com'
dbnm = temp_user

# Connect to postgres; Get cursor
pg_conn = psycopg2.connect(dbname=dbnm, user=temp_user,
                           password=temp_pass, host=host)
pg_curs = pg_conn.cursor()

# Get passengers
passengers = curs.execute('SELECT * FROM titanic;').fetchall()
if len(passengers) != 887:
    raise ValueError("Not the right table")

# Postgres is different, yeah
create_table = f'''
CREATE TABLE titanic_passengers (
    index INT,
    Survived INT,
    Pclass INT,
    Name varchar(100),
    Sex varchar(15),
    Age NUMERIC,
    Ss INT,
    Pc INT,
    Fare NUMERIC
);
'''

pg_curs.execute(create_table)

# Query table using this postgresql internal thingie
show_tables = f'''
SELECT * FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema'
'''
pg_curs.execute(show_tables)
print(pg_curs.fetchall())
thingie = curs.execute('PRAGMA table_info(titanic);').fetchall()
for i in thingie:
    print(i)

# Transforming is finito, now we load those values
for p in passengers:
    insert = f'''
    INSERT INTO titanic_passengers
    (index, Survived, Pclass, Name, Sex, Age, Ss, Pc, Fare)
    VALUES ''' + str(p[0:]) + ';'
    # Needed to make sure to remove double quotes
    pg_curs.execute(insert)

pg_curs.execute('SELECT * FROM titanic_passengers;')

print('Length:', len(pg_curs))

for i in pg_curs.fetchall():
    print(i)

pg_curs.close()
pg_conn.commit()

# Let's see if it worked
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic_passengers')
pg_p = pg_curs.fetchall()
print(passengers[0][0], '\n', pg_p[0])
