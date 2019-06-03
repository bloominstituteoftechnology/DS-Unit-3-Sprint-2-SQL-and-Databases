import pandas
import sqlite3

connect = sql.connect('rpg_db.sqlite3')
curse = connect.cursor()


def total_char_count():
    '''Total all characters'''
    print(pd.read_sql_query('''SELECT COUNT(distinct character_id)
        FROM charactercreator_character;''', connect))
def char_count_fighter():
    '''Total fighter characters'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM charactercreator_fighter;''', connect))
def char_count_mage():
    '''Total fighter characters'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM charactercreator_mage;''', connect))
def char_count_cleric():
    '''Total fighter characters'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM charactercreator_cleric;''', connect))
def char_count_chief():
    '''Total fighter characters'''
    print(pd.read_sql_query('''SELECT COUNT(*)
        FROM charactercreator_chief;''', connect))





def total_item_count():
    '''Total items'''
    print(pd.read_sql_query('''SELECT COUNT(distinct item_id)
            FROM armory_item;''', connect))
