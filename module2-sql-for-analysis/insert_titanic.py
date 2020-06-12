# import libraries:
import pandas as pd
import psycopg2
import csv

# details of postgresql account:
dbname = 'bpecpenu' # same than user
user = 'bpecpenu' # same than dbname
password = 'pm5X5ZXRZjSD9oOEM2t_aLJALLdXNyuN' # Don't commit original pass
host = 'otto.db.elephantsql.com' # from SERVER type

# stablish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_conn
# instantiate cursor 
pg_curs = pg_conn.cursor()

# create new empty table and define schema)
create_passengers_table = """
  CREATE TABLE passengers (  
    id SERIAL NOT NULL PRIMARY KEY, 
    survived INT,
    pclass INT,
    name VARCHAR(200),
    sex VARCHAR(20),
    age INT,
    siblings_spouses INT,
    parents_children INT,
    fare NUMERIC(30)
);
"""

pg_curs.execute(create_passengers_table)

# show table on list of tables
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

# read csv file
csv_data = pd.read_csv('titanic.csv')

# Input each row from the DataFrame into the new table on DataBase
statement = """
        INSERT INTO passengers (
            survived, 
            pclass, 
            name, 
            sex, 
            age, 
            siblings_spouses, 
            parents_children, 
            fare 
        ) VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
        """

# define data row by row in a for loop where each value is iterated over pandas dataframe using itertuples
data = [row for row in csv_data.itertuples(index=False)]

# using a for loop to populate the new table passengers
for item in data:
  pg_curs.execute(
  statement, 
  item
  )

# close cursor and commit changes on the DB
pg_curs.close()
pg_conn.commit()