#  ________ rpg_postgres.py ______

import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def create_pg_table(df, table_name):
    # ___ Convert to postgres DB____
    df.to_sql('titanic',
              if_exists='replace',
              con=engine,
              method='multi')
    
    return

def run_conversion(engine):
    # ___ load SQlite into df   ____
    tables="""
    charactercreator_character
    charactercreator_character_inventory
    charactercreator_cleric
    charactercreator_fighter
    charactercreator_thief
    charactercreator_mage
    charactercreator_necromancer
    armory_item
    armory_weapon
    """

    # ___ Convert to postgres DB____
    create_pg_table(df, table_name)

    return


def main():
    # __ Connect to postgres (SQLalchemy.engine) ____
    dbname = 'zoafqkfp'
    user = 'zoafqkfp'
    host = 'stampy.db.elephantsql.com'
    passw = 'MCJu21HwCynkStIs3FOmV-xHXSAXOSDD'
    eng_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    engine = create_engine(eng_str)

    # ____ Port sqlite to postgres ___
    run_conversion(engine)

    # ______  Print postgres table
    query = """
    SELECT *
    FROM public.titanic
    LIMIT 10 ;
    """
    for row in engine.execute(query).fetchall():
        print(row)

    # ___ end main ___________
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
