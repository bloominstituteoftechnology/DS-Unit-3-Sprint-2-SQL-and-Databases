# /MODULE2-SQL-FOR-ANALYSIS/rpg_elephant_data.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
import sqlite3


load_dotenv()

# Set path to rpg data
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), 
                    '..', 'module1-introduction-to-sql', 
                    'rpg_db.sqlite3')

DB_HOST = os.getenv("DB_HOST", default="You Don't Belong Here")
DB_NAME = os.getenv("DB_NAME", default="You Don't Belong Here")
DB_USER = os.getenv("DB_USER", default="You Don't Belong Here")
DB_PASSWORD = os.getenv("DB_PW", default="You Don't Belong Here")

# print(DB_HOST)
# print(DB_NAME)
# print(DB_USER)
# print(DB_PASSWORD)

#
# Create connection to rpg_data
#
sqlite_connection = sqlite3.connect(DATABASE_FILEPATH) 
sqlite_connection.row_factory = sqlite3.Row
sqlite_cursor = sqlite_connection.cursor()

postgres_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, 
                              password=DB_PASSWORD, host=DB_HOST)
print(f"CONNECTION: {type(postgres_connection)}")
postgres_cursor = postgres_connection.cursor()
print(f"CURSOR {type(postgres_cursor)}")

# for row in armory_item_info:
#     print(row[:])
# for row in armory_weapon_info:
#    print(row[:])
#for row in character_table_info:
 #   print(row[:])
# for row in character_inventory_info:
#    print(row[:])
# for row in cleric_info:
#    print(row[:])
# for row in fighter_info:
#    print(row[:])
# for row in mage_info:
#    print(row[:])
# for row in necromancer_info:
#    print(row[:])
# for row in thief_info:
#    print(row[:])

create_armory_item_table = """
                           DROP TABLE IF EXISTS armory_item;
                           CREATE TABLE IF NOT EXISTS armory_item (
                                item_id SERIAL PRIMARY KEY,
                                name VARCHAR(30),
                                value Int,
                                weight INT
                           );
                           """

create_armory_weapon_table = """
                           DROP TABLE IF EXISTS armory_weapon;
                           CREATE TABLE IF NOT EXISTS armory_weapon (
                                id SERIAL PRIMARY KEY,
                                item_ptr_id INT,
                                power INT
                           )
                           """

create_character_table = """
                         DROP TABLE IF EXISTS charactercreator_character;
                         CREATE TABLE IF NOT EXISTS charactercreator_character (
                             character_id SERIAL PRIMARY KEY,
                             name VARCHAR(30),
                             level INT,
                             exp INT,
                             hp INT,
                             strength INT,
                             intelligence INT,
                             dexterity INT,
                             wisdom INT
                         )   
                         """

create_character_inventory_table = """
                           DROP TABLE IF EXISTS charactercreator_character_inventory;
                           CREATE TABLE IF NOT EXISTS charactercreator_character_inventory (
                                id SERIAL PRIMARY KEY,
                                character_id INT,
                                item_id INT
                           )
                           """

create_cleric_table = """
                           DROP TABLE IF EXISTS charactercreator_cleric;
                           CREATE TABLE IF NOT EXISTS charactercreator_cleric (
                                character_ptr_id SERIAL PRIMARY KEY,
                                using_shield INT,
                                mana INT
                           )
                           """
       
create_fighter_table = """
                           DROP TABLE IF EXISTS charactercreator_fighter;
                           CREATE TABLE IF NOT EXISTS charactercreator_fighter (
                                character_ptr_id SERIAL PRIMARY KEY,
                                using_shield INT,
                                rage INT
                           )
                           """

create_mage_table = """
                           DROP TABLE IF EXISTS charactercreator_mage;
                           CREATE TABLE IF NOT EXISTS charactercreator_mage (
                                character_ptr_id SERIAL PRIMARY KEY,
                                has_pet INT,
                                mana INT
                           )
                           """

create_necromancer_table = """
                           DROP TABLE IF EXISTS charactercreator_necromancer;
                           CREATE TABLE IF NOT EXISTS charactercreator_necromancer (
                                id SERIAL PRIMARY KEY,
                                mage_ptr_id INT,
                                talisman_charged INT
                           )
                           """

create_thief_table = """
                           DROP TABLE IF EXISTS charactercreator_thief;
                           CREATE TABLE IF NOT EXISTS charactercreator_thief (
                                character_ptr_id SERIAL PRIMARY KEY,
                                is_sneaking INT,
                                energy INT
                           )
                           """

postgres_cursor.execute(create_armory_item_table)
postgres_cursor.execute(create_armory_weapon_table)
postgres_cursor.execute(create_character_table)
postgres_cursor.execute(create_character_inventory_table)
postgres_cursor.execute(create_cleric_table)
postgres_cursor.execute(create_fighter_table)
postgres_cursor.execute(create_mage_table)
postgres_cursor.execute(create_necromancer_table)
postgres_cursor.execute(create_thief_table)

armory_item_info = sqlite_cursor.execute('PRAGMA table_info(armory_item);').fetchall()
armory_weapon_info = sqlite_cursor.execute('PRAGMA table_info(armory_weapon);').fetchall()
character_table_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_character);').fetchall()
character_inventory_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_character_inventory);').fetchall()
cleric_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_cleric);').fetchall()
fighter_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_fighter);').fetchall()
mage_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_mage);').fetchall()
necromancer_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_necromancer);').fetchall()
thief_info = sqlite_cursor.execute('PRAGMA table_info(charactercreator_thief);').fetchall()

get_items = """
                 SELECT
                    *
                 FROM
                    armory_item
                 """

get_weapons = """
                 SELECT
                    *
                 FROM
                    armory_weapon
                 """

get_characters = """
                 SELECT
                    *
                 FROM
                    charactercreator_character
                 """

get_inventories = """
                 SELECT
                    *
                 FROM
                    charactercreator_character_inventory
                 """

get_clerics = """
                 SELECT
                    *
                 FROM
                    charactercreator_cleric
                 """

get_fighters = """
                 SELECT
                    *
                 FROM
                    charactercreator_fighter
                 """

get_mages = """
                 SELECT
                    *
                 FROM
                    charactercreator_mage
                 """

get_necromancers = """
                 SELECT
                    *
                 FROM
                    charactercreator_necromancer
                 """

get_thieves = """
                 SELECT
                    *
                 FROM
                    charactercreator_thief
                 """
items = sqlite_cursor.execute(get_items).fetchall()
weapons = sqlite_cursor.execute(get_weapons).fetchall()
characters = sqlite_cursor.execute(get_characters).fetchall()
inventories = sqlite_cursor.execute(get_inventories).fetchall()
clerics = sqlite_cursor.execute(get_clerics).fetchall()
fighters = sqlite_cursor.execute(get_fighters).fetchall()
mages = sqlite_cursor.execute(get_mages).fetchall()
necromancers = sqlite_cursor.execute(get_necromancers).fetchall()
thieves = sqlite_cursor.execute(get_thieves).fetchall()

for item in items:
    item_table_insert = """
    INSERT INTO 
        armory_item (name, value, weight)
    VALUES
    """ + str(item[1:])
    postgres_cursor.execute(item_table_insert)

for weapon in weapons:
    weapon_table_insert = """
    INSERT INTO
        armory_weapon (item_ptr_id, power)
    VALUES
    """ + str(weapon[:])
    postgres_cursor.execute(weapon_table_insert)

for character in characters:
    character_table_insert = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES 
    """ + str(character[1:])
    postgres_cursor.execute(character_table_insert)

for inventory in inventories:
    inventory_table_insert = """
    INSERT INTO 
        charactercreator_character_inventory (character_id, item_id)
    VALUES
    """ + str(inventory[1:])
    postgres_cursor.execute(inventory_table_insert)

for cleric in clerics:
    cleric_table_insert = """
    INSERT INTO
        charactercreator_cleric (using_shield, mana)
    VALUES
    """ + str(cleric[1:])
    postgres_cursor.execute(cleric_table_insert)

for fighter in fighters:
    fighter_table_insert = """
    INSERT INTO
        charactercreator_fighter (using_shield, rage)
    VALUES
    """ + str(fighter[1:])
    postgres_cursor.execute(fighter_table_insert)

for mage in mages:
    mage_table_insert = """
    INSERT INTO
        charactercreator_mage (has_pet, mana)
    VALUES
    """ + str(mage[1:])
    postgres_cursor.execute(mage_table_insert)

for necromancer in necromancers:
    necromancer_table_insert = """
    INSERT INTO
        charactercreator_necromancer (mage_ptr_id, talisman_charged)
    VALUES
    """ + str(necromancer[:])
    postgres_cursor.execute(necromancer_table_insert)

for thief in thieves:
    thief_table_insert = """
    INSERT INTO
        charactercreator_thief (is_sneaking, energy)
    VALUES
    """ + str(thief[1:])
    postgres_cursor.execute(thief_table_insert)


postgres_connection.commit()

postgres_cursor.close()
postgres_connection.close()


