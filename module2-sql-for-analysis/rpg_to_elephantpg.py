import psycopg2
import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

SQL_DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..",
                               "module1-introduction-to-sql",
                               "rpg_db.sqlite3")

PG_DB_NAME = os.genenv("PG_DB_NAME")
PG_DB_USER = os.genenv("PG_DB_USER")
PG_DB_PASSWORD = os.genenv("PG_DB_PASSWORD")
PG_DB_HOST = os.genenv("PG_DB_HOST")
PG_ALCHEMY_ENGINE = os.genenv("PG_ALCHEMY_ENGINE")
SQL_ALCHEMY_ENGINE = os.genenv("SQL_ALCHEMY_ENGINE")

sqlconn = sqlite3.connect(SQL_DB_FILEPATH)
pgconn = psycopg2.connect(dbname=PG_DB_NAME,
                          user=PG_DB_USER,
                          password=PG_DB_PASSWORD,
                          host=PG_DB_HOST)

pg_engine = create_engine(PG_ALCHEMY_ENGINE)
sql_engine = create_engine(SQL_ALCHEMY_ENGINE)

sqlcurs = sqlconn.cursor()
pgcurs = pgconn.cursor()

# create a list of table names in preparation for our pandas import
sql_table_names = []

sql_table_query = """
    SELECT name
    from sqlite_master
    where type = 'table'
"""

for table_name in sqlcurs.execute(sql_table_query):
    pragma_query = f"""
    PRAGMA foreign_key_list({table_name})
    """
    foreign_keys = sqlcurs.execute(pragma_query).fetchall()
    sql_table_names.append(table_name)

# create a dictionary of pandas dataframes
tables_dict = {}
for name in sql_table_names:
    table = pd.read_sql_table()

# another alternative to the below query
# ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address)
# REFERENCES addresses (address) MATCH FULL;

# create tables from pandas to postgresql
for i in tables_dict:
    insert_keys_query = """
    ALTER TABLE table_name ADD INDEX(column_name);
    """
