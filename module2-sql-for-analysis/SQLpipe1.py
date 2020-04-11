'''
 __SQL Pipeline Conversion 1 __
  Sqlite to  ElephantSQL(postgres) 
   using SQLalchemy engine
         pandas.read_sql_table() converts SQL->df
         pandas.to_sql() converts df->SQL
'''

import pandas as pd
import sqlite3
import psycopg2
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite
import os
from dotenv import load_dotenv
load_dotenv()

def verify_output(pgres_engine, table_name, schema_name):
    # ______  verify output-table contents ____
    #   ElephantSQL requires FROM "schema".table_name   format
    query = 'SELECT * FROM ' + '"' + schema_name + '"' +  '.' + table_name + ' LIMIT 10;'
    for row in pgres_engine.execute(query).fetchall():
        print(row)
    return


def run_conversion(pgres_engine):
    # ___ process tables ____
    # - WARNING!  FOR AWS : schema must already exist
    schema_name = 'lambdaRPG'
    tables = ['charactercreator_character',
              'charactercreator_character_inventory',
              'charactercreator_cleric',
              'charactercreator_fighter',
              'charactercreator_thief',
              'charactercreator_mage',
              'charactercreator_necromancer',
              'armory_item',
              'armory_weapon']

    # ___ connect to  sqlite3  ____
    lite_engine = create_engine('sqlite+pysqlite:///rpg_db.sqlite3',
                                module=sqlite)

    for table_name in tables:
        print('converting........ ', table_name)
        # ___ load SQlite into df   ____
        df = pd.read_sql_table(table_name,
                               con=lite_engine)

        #  To avoid an extra SQL table column,
        #  set dataframe index to 1st column
        #  before executing .to_sql()
        df.set_index(df.columns[0], inplace=True)

        # ___ Convert df to postgresDB____
        df.to_sql(table_name,
                  if_exists='replace',
                  con=pgres_engine,
                  schema=schema_name,
                  method='multi')

        verify_output(pgres_engine, table_name, schema_name)
    return


def main():
    # __ Connect to ElephantSQL(postgres) (SQLalchemy.create_engine) ____
    # __ credentials stored in .env __
    dbname = os.getenv("DS_DB_NAME")
    user = os.getenv("DS_DB_USER")
    host = os.getenv("DS_DB_HOST")
    passw = os.getenv("DS_DB_PASSWORD")
    pgres_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    pgres_engine = create_engine(pgres_str)

    # ____ Port sqlite tables to postgres ___
    run_conversion(pgres_engine)

    # ___ end main ___________
    print('Conversion successful.....')
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
