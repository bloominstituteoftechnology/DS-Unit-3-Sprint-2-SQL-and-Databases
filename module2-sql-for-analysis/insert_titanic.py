import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# load data
df = pd.read_csv('titanic.csv')

# elephantsql
database = 'qeipvcuk'
user = 'qeipvcuk'
password = 'giRROP4E18vrmHVYBaQZ1fPDTenGyYXX'
host = '	rajje.db.elephantsql.com 

# connect to python postgresql db adapter
pg_conn = psycopg2.connect(database=database, user=user, password=password,
                           host=host)

# create cursor obj
curs = pg_conn.cursor()

# TABLE TO INSERT INTO

create_passenger_table = """
    CREATE TABLE passengers (
        id INT,
        survived INT,
        pclass INT,
        name VARCHAR(30),
        sex VARCHAR(10),
        age REAL,
        siblings_spouses_aboard INT,
        parents_children_aboard INT,
        fare REAL
    ); """


curs.execute(create_passenger_table)

pg_conn.commit()

#
db_string = 'postgres://qeipvcuk:giRROP4E18vrmHVYBaQZ1fPDTenGyYXX@rajje.db.elephantsql.com:5432/qeipvcuk'

engine = create_engine(db_string)
#
pg_conn_2 = engine.connect()
#
#
#
df.to_sql('passengers', pg_conn_2, if_exists='replace')
#
#
pg_conn.close()

pg_conn_2.close()