import sqlite3 
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

def total_character_count():
    # How many total characters are there?
    print(pd.read_sql_query(
        '''SELECT COUNT(*) as character_count
           FROM charactercreator_character''',
        conn)
    )

def subclass_count():
    # How many of each specific subclass?
    print(pd.read_sql_query(
        '''SELECT 'mage' as subclass, COUNT(*) as character_count
        FROM charactercreator_mage

        UNION

        SELECT 'necromancer', COUNT(*)
        FROM charactercreator_necromancer

        UNION

        SELECT 'thief', COUNT(*)
        FROM charactercreator_thief

        UNION

        SELECT 'cleric', COUNT(*)
        FROM charactercreator_cleric

        UNION

        SELECT 'fighter', COUNT(*)
        FROM charactercreator_fighter
        ''',
        conn)
    )

def total_items():
    # How many total items?
    print(pd.read_sql_query(
        '''
        SELECT COUNT(*) FROM armory_item
        ''',
        conn)
    )

def total_weapons():
    # How many items are weapons?
    print(pd.read_sql_query(
        '''
        SELECT COUNT(*) FROM armory_weapon
        ''',
        conn)
    )

def total_non_weapons():
    # How many items are NOT weapons?
    print(pd.read_sql_query(
        '''
        SELECT COUNT(*) FROM armory_item
        WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
        ''',
        conn)
    )

def items_per_character():
    # How many items are NOT weapons?
    print(pd.read_sql_query(
        '''
        SELECT character_id, COUNT(item_id) as item_count
        FROM charactercreator_character_inventory
        GROUP BY character_id
        LIMIT 20
        ''',
        conn)
    )

# I'm too lazy to copy/paste the rest of the methods

curs.close()