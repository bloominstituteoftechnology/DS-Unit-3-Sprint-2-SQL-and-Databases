import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# How many total Characters are there?
def total_characters():
    print(pd.read_sql_query("""SELECT COUNT(distinct character_id) as character_count
    FROM charactercreator_character;""", conn))


# How many of each specific subclass?
def subclass_count():
    print(pd.read_sql_query("""SELECT 'mages' as subclass, COUNT(*) as character_count
    FROM charactercreator_mage

    UNION

    SELECT 'clerics', COUNT(*)
    FROM charactercreator_cleric

    UNION

    SELECT 'fighter', COUNT(*)
    FROM charactercreator_fighter

    UNION

    SELECT 'thieves', COUNT(*)
    FROM charactercreator_thief;""", conn))


# How many total Items?
def total_items():
    print(pd.read_sql_query("""SELECT COUNT(distinct item_id) as item_count
        FROM armory_item;""", conn))


# How many of the Items are weapons? How many are not?
def weapon_items():
    print(pd.read_sql_query("""SELECT COUNT(*) as weapon_count
                    FROM armory_item
                    WHERE item_id IN
                        (SELECT distinct item_ptr_id
                        FROM armory_weapon);""", conn))


def nonweapon_items():
    print(pd.read_sql_query("""SELECT COUNT(*) as nonweapon_count
                    FROM armory_item
                    WHERE item_id NOT IN
                        (SELECT distinct item_ptr_id
                        FROM armory_weapon);""", conn))


# How many Items does each character have? (Return first 20 rows)
def character_items():
    print(pd.read_sql_query("""SELECT character_id, count(item_id) as item_count
                    FROM charactercreator_character_inventory
                    GROUP BY character_id
                    LIMIT 20;""", conn))


# How many Weapons does each character have? (Return first 20 rows)
def character_weapons():
    print(pd.read_sql_query("""SELECT character_id, count(item_id) as weapon_count
                    FROM charactercreator_character_inventory
                    WHERE item_id IN
                        (SELECT distinct item_ptr_id
                        FROM armory_weapon)
                    GROUP BY character_id
                    LIMIT 20;""", conn))


# On average, how many Items does each Character have?
def avg_items():
    print(pd.read_sql_query("""SELECT AVG(items) as average_items
                    FROM (
                        SELECT character_id, count(item_id) as items
                        FROM charactercreator_character_inventory
                        GROUP BY character_id);""", conn))


# On average, how many Weapons does each character have?
def avg_weapons():
    print(pd.read_sql_query("""SELECT AVG(items) as average_weapons
                    FROM (
                        SELECT character_id, count(item_id) as items
                        FROM charactercreator_character_inventory
                        WHERE item_id IN (
                                    SELECT distinct item_ptr_id
                                    FROM armory_weapon)
                        GROUP BY character_id);""", conn))
