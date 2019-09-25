import sqlite3 as sqp
import pandas as pd

connect = sql.connect('rpg_db.sqlite3')
curse = connect.cursor()

def total_char_count():
    '''Total all characters'''
    print(pd.read_sql_query('''SELECT COUNT(distinct character_id)
        FROM charactercreator_character;''', connect))
                       #Why is there an extra indent in line above

def sub_class():
    '''Grab population count of each subclass of characters'''
    print(pd.read_sql_query('''SELECT "mages", COUNT(*)
        From charactercreator_mage

        UNION

        SELECT "clerics", COUNT(*)
        FROM charactercreator_cleric

        UNION

        SELECT "fighter", COUNT(*)
        FROM charactercreator_fighter

        UNION

        SELECT "thieves", COUNT(*)
        FR
