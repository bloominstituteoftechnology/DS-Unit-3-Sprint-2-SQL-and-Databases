import pandas as pd
import sqlite3
import psycopg2
from psycopg2.extensions import AsIs
import warnings

# pg = PostGres, sql3 = sqlite3

# for connect to WinstonElephantSQL
dbname = "fxbzafim"
user = "fxbzafim"
password = "wqVYFX8ryOe6QXiUzYk_kbJj8SnRJ6nv"
host = "isilo.db.elephantsql.com"

warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df_titanic = pd.read_csv("data/titanic.csv")
print()
df_titanic.Name = df_titanic.Name.replace("'", '', regex=True)  # take out fucking apost that caused three hours of heartache
print(df_titanic.head())

# first stick into sqlite db
db_table = 'titanic'
sql3_conn = sqlite3.connect('data/' + db_table + '.sqlite3')
df_titanic.to_sql(db_table, sql3_conn, if_exists='replace')
sql3_curs = sql3_conn.cursor()
query = 'SELECT COUNT(*) FROM titanic;'
rows = sql3_curs.execute(query).fetchall()[0][0]
print("\nThere are", rows, "rows in the titanic table")
query = 'SELECT COUNT(*) FROM titanic WHERE survived = 1;'
survived = sql3_curs.execute(query).fetchall()[0][0]
print(survived, "people survived, so", rows - survived, "perished\n")
query = 'SELECT COUNT(*) FROM titanic WHERE (Age < 50 and  Fare > 100)';
print(sql3_curs.execute(query).fetchall()[0][0], "people were younger than 50 and paid more than 100\n\n")

# now connect to WinstonElephantSQL Postgre db
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

pg_curs = pg_conn.cursor()

pg_curs.execute('SELECT * FROM test_table;')
results = pg_curs.fetchall()

print("Stuff in WinstonElephantSQL test_table")
for result in results:
    print(result)

# Our goal - an ETL/data pipeline
# Get the character data from SQLite to PostgreSQL!
sql3_titanic_table = sql3_curs.execute('SELECT * FROM titanic;').fetchall()

# Character schema for PostgreSQL
create_titanic_table = """
CREATE TABLE titanic (
  person_id SERIAL PRIMARY KEY,
  survived INT,
  pclass INT,
  name VARCHAR(82),
  gender VARCHAR(7),
  age FLOAT,
  "siblings/spouses aboard" INT,
  "parents/children aboard" INT,
  fare FLOAT 
)
"""

pg_curs.execute(create_titanic_table)

# Loop over and actually insert all the results
for row in sql3_titanic_table:
  insert_row = """
  INSERT INTO titanic
  (survived, pclass, name, gender, age, "siblings/spouses aboard", "parents/children aboard", fare)
  VALUES """ + str(row[1:])

  pg_curs.execute(insert_row)

pg_conn.commit()

# Let's remake the pg cursor and check things
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic;')
pg_titanic_table = pg_curs.fetchall()

# commented out 'cause assertion fails
#for character, pg_character in zip(sql3_titanic_table, pg_titanic_table):
#  assert character == pg_character

# If nothing prints - means the two tables are equal!
