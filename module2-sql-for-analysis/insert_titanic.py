# importing libraries
import psycopg2
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

#assigning engine constant for df.to_sql
engine = create_engine('sqlite://', echo=False)


#reading titanic .csv
df = pd.read_csv('titanic.csv')
#titanic dataframe must be read to a sql table callled titanic
df.to_sql('titanic', con=engine)


# Creating a dataabase connection to elephantsql
dbname = 'clfidagv'
user = 'clfidagv'
password = 'wasMdZHPBbnq_hfIsWYPvtyQDmO28ML9' #password goes here
# wasMdZHPBbnq_hfIsWYPvtyQDmO28ML9
host = 'salt.db.elephantsql.com'

#creating connection to interact
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

#creating the cursor to interact with database connection
pg_curs = pg_conn.cursor()


#pulling a schema from titanic
engine.execute('PRAGMA table_info(titanic);').fetchall()


#Schema for titanic table
# [(0, 'index', 'BIGINT', 0, None, 0),
# (1, 'Survived', 'BIGINT', 0, None, 0),
# (2, 'Pclass', 'BIGINT', 0, None, 0),
# (3, 'Name', 'TEXT', 0, None, 0),
# (4, 'Sex', 'TEXT', 0, None, 0),
# (5, 'Age', 'FLOAT', 0, None, 0),
# (6, 'Siblings/Spouses Aboard', 'BIGINT', 0, None, 0),
# (7, 'Parents/Children Aboard', 'BIGINT', 0, None, 0),
# (8, 'Fare', 'FLOAT', 0, None, 0)]

#creating a table in elephentsql:
create_titanic_table = """
  CREATE TABLE titanic(
  index SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name varchar(100),
  Sex varchar(10),
  Age FLOAT,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare FLOAT
  );
"""

#creating the titanic table
pg_curs.execute(create_titanic_table)

#updating the titanic.csv sql table to replace the ' value in the name column
engine.execute('''
UPDATE titanic SET Name = REPLACE(Name, "'", " ")
''')

#pulling all of the names in the titanicsql table
passengers = engine.execute('SELECT * FROM titanic').fetchall()

#for each passanger in this list (after removing the first entry)
for passenger in passengers[1:]:
    insert_passenger = """
        INSERT INTO titanic
        VALUES""" + str(passenger) + ";"
    pg_curs.execute(insert_passenger)
pg_conn.commit()
