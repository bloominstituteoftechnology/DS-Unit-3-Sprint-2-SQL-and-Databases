#  ________
import pandas as pd
import sqlite3
import psycopg2
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite
import dotenv
import os


def verify_output(pgres_engine, table_name):
    # ______  verify output-table contents ____
    query = 'SELECT * FROM ' + table_name + ' LIMIT 10;'
    for row in pgres_engine.execute(query).fetchall():
        print(row)
    return


def run_conversion(pgres_engine):
    # ___ process tables ____
    # - WARNING!  schema must already exist
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

        #  BUG ALERT! drop the dataframe index column
        #             before executing .to_sql()

        # ___ Convert to postgres DB____
        df.to_sql(table_name,
                  if_exists='replace',
                  con=pgres_engine,
                  schema=schema_name,
                  method='multi')
        verify_output(pgres_engine, table_name)

    return


def main():
    # __ Connect to postgres (SQLalchemy.engine) ____
    dbname = ''
    user = ''
    host = ''
    password = ''
    file = open('aws.pwd', 'r')
    ctr = 1
    for line in file:
        line = line.replace('\n', '')
        if ctr == 1: dbname = line
        if ctr == 2: user = line
        if ctr == 3: host = line
        if ctr == 4: passw = line
        ctr = ctr + 1

    pgres_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    pgres_engine = create_engine(pgres_str)

    # ____ Port sqlite to postgres ___
    run_conversion(pgres_engine)

    # ___ end main ___________

    print('Conversion successful.....')
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
