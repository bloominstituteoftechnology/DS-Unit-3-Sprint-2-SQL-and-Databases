# imports
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# load titanic csv into df
titanic_df = pd.read_csv('titanic.csv')

titanic_df.columns = map(str.lower, titanic_df.columns)

print(titanic_df.head())

# elephantsql credentials
host = 'salt.db.elephantsql.com'
user = 'rtwvxkrw'
database = 'rtwvxkrw'
password = 'bfZkn2ysvf3eTCa19VmMwJkt-bZyO-tK'

# make connection to elephantsql, open cursor
pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

# enumerated type declarations
enum_survival = """
CREATE TYPE survival AS ENUM ('0', '1');
"""
enum_pass_class = """
CREATE TYPE pass_class AS ENUM ('1', '2', '3');
"""
enum_gender = """
CREATE TYPE gender AS ENUM ('male', 'female');
"""

# execute type declarations
pg_cur.execute(enum_survival)
pg_conn.commit()

pg_cur.execute(enum_pass_class)
pg_conn.commit()

pg_cur.execute(enum_gender)
pg_conn.commit()

"""# create titanic table
create_titanic_table = """
"""CREATE TABLE titanic(
    survived survival,
    pclass pass_class,
    name TEXT,
    sex gender,
    age INT,
    siblings INT,
    parents INT,
    fare FLOAT
);
""""""
# execute table creation
pg_cur.execute(create_titanic_table)
pg_conn.commit()"""

# open connection using sqlalchemy
db_string = "postgres://rtwvxkrw:bfZkn2ysvf3eTCa19VmMwJkt-bZyO-tK@salt.db.elephantsql.com:5432/rtwvxkrw"
engine = create_engine(db_string)

pg_conn_alch = engine.connect()

# load records into table
titanic_df.to_sql('titanic', pg_conn_alch)

# close connecions
pg_conn.close()
pg_conn_alch.close()