#  ________ rpg_postgres.py ______
import pandas as pd
import sqlite3
import psycopg2
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite


def verify_output(pgres_engine, table_name):
    # ______  verify output-table contents ____
    query = 'SELECT * FROM ' + table_name + ' LIMIT 10;'
    for row in pgres_engine.execute(query).fetchall():
        print(row)
    return


def run_conversion(pgres_engine):
    # ___ connect to  sqlite3  ____
    lite_engine = create_engine('sqlite+pysqlite:///rpg_db.sqlite3',
                                module=sqlite)

    # ___ process tables ____
    tables = ['charactercreator_character',
              'charactercreator_character_inventory',
              'charactercreator_cleric',
              'charactercreator_fighter',
              'charactercreator_thief',
              'charactercreator_mage',
              'charactercreator_necromancer',
              'armory_item',
              'armory_weapon']

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
                  method='multi')
        verify_output(pgres_engine, table_name)

    return


def main():
    # __ Connect to postgres (SQLalchemy.engine) ____
    dbname = 'zoafqkfp'
    user = 'zoafqkfp'
    host = 'TODO'
    passw = 'TODO'
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
