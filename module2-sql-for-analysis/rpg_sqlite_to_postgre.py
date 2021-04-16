# rpg_sqlite_to_postgre


import os
import sqlite3
import psycopg2
from dotenv import load_dotenv


# Connect to rpg_db.sqlite3 with SQLite

DB_FILEPATH = os.path.join(os.path.dirname(__file__),
 "..", "module1-introduction-to-sql", "data", "rpg_db.sqlite3")

sqlite_connection = sqlite3.connect(DB_FILEPATH)
sqlite_connection.row_factory = sqlite3.Row # allows us to reference rows as dicts
print("CONNECTION:", sqlite_connection)

sqlite_cursor = sqlite_connection.cursor()
print("CURSOR", sqlite_cursor)


# Load ElephantSQL credentials

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

postgre_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(postgre_connection))

postgre_cursor = postgre_connection.cursor()
print("CURSOR", type(postgre_cursor))


# Create charactercreator_character table

create_charactercreator_character_table = """
CREATE TABLE charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INTEGER NOT NULL,
    exp INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    wisdom INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_character_table)

characters = sqlite_cursor.execute('SELECT * FROM charactercreator_character;')

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  postgre_cursor.execute(insert_character)


# Create charactercreator_fighter table

create_charactercreator_fighter_table = """
CREATE TABLE charactercreator_fighter(
    character_ptr_id INTEGER NOT NULL,
    using_shield INT NOT NULL,
    rage INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_fighter_table)

fighters = sqlite_cursor.execute('SELECT * FROM charactercreator_fighter')

for fighter in fighters:
  insert_fighter = """
    INSERT INTO  charactercreator_fighter
    (character_ptr_id, using_shield, rage)
    VALUES """ + str(fighter[0:]) + ';'
  postgre_cursor.execute(insert_fighter)


# Create charactercreator_cleric table

create_charactercreator_cleric_table = """
CREATE TABLE charactercreator_cleric(
    character_ptr_id INTEGER NOT NULL,
    using_shield INT NOT NULL,
    mana INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_cleric_table)

clerics = sqlite_cursor.execute('SELECT * FROM charactercreator_cleric')

for cleric in clerics:
  insert_cleric = """
    INSERT INTO  charactercreator_cleric
    (character_ptr_id, using_shield, mana)
    VALUES """ + str(cleric[0:]) + ';'
  postgre_cursor.execute(insert_cleric)


# Create charactercreator_thief table

create_charactercreator_thief_table = """
CREATE TABLE charactercreator_thief(
    character_ptr_id INTEGER NOT NULL,
    is_sneaking INT NOT NULL,
    energy INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_thief_table)

thieves = sqlite_cursor.execute('SELECT * FROM charactercreator_thief')

for thief in thieves:
  insert_thief = """
    INSERT INTO  charactercreator_thief
    (character_ptr_id, is_sneaking, energy)
    VALUES """ + str(thief[0:]) + ';'
  postgre_cursor.execute(insert_thief)


# Create charactercreator_mage table

create_charactercreator_mage_table = """
CREATE TABLE charactercreator_mage(
    character_ptr_id INTEGER NOT NULL,
    has_pet INT NOT NULL,
    mana INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_mage_table)

mages = sqlite_cursor.execute('SELECT * FROM charactercreator_mage;')

for mage in mages:
  insert_mage = """
    INSERT INTO  charactercreator_mage
    (character_ptr_id, has_pet, mana)
    VALUES """ + str(mage[0:]) + ';'
  postgre_cursor.execute(insert_mage)


# Create charactercreator_necromancer table

create_charactercreator_necromancer_table = """
CREATE TABLE charactercreator_necromancer(
    mage_ptr_id INTEGER NOT NULL,
    talisman_charged INT NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_necromancer_table)

necromancers = sqlite_cursor.execute('SELECT * FROM charactercreator_necromancer')

for necromancer in necromancers:
  insert_necromancer = """
    INSERT INTO  charactercreator_necromancer
    (mage_ptr_id, talisman_charged)
    VALUES """ + str(necromancer[0:]) + ';'
  postgre_cursor.execute(insert_necromancer)


# Create armory_item table

create_armory_item_table = """
CREATE TABLE armory_item(
    item_id INTEGER,
    name VARCHAR(30),
    "value" INTEGER,
    weight INTEGER
);"""

postgre_cursor.execute(create_armory_item_table)

items = sqlite_cursor.execute('SELECT * FROM armory_item;')

for item in items:
  insert_item = """
    INSERT INTO armory_item
    (name, value, weight)
    VALUES """ + str(item[1:]) + ';'
  postgre_cursor.execute(insert_item)


# Create charactercreator_character_inventorytable

create_charactercreator_character_inventory_table = """
CREATE TABLE charactercreator_character_inventory(
    id INTEGER,
    character_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL
);"""

postgre_cursor.execute(create_charactercreator_character_inventory_table)

ids = sqlite_cursor.execute('SELECT * FROM charactercreator_character_inventory;')

for identification in ids:
  insert_id = """
    INSERT INTO charactercreator_character_inventory
    (character_id, item_id)
    VALUES """ + str(identification[1:]) + ';'
  postgre_cursor.execute(insert_id)


# Create armory_weapon table

create_armory_weapon_table = """
CREATE TABLE armory_weapon(
    item_ptr_id INTEGER NOT NULL,
    power INTEGER NOT NULL
);"""

postgre_cursor.execute(create_armory_weapon_table)

weapons = sqlite_cursor.execute('SELECT * FROM armory_weapon;')

for weapon in weapons:
  insert_weapon = """
    INSERT INTO armory_weapon
    (item_ptr_id, power)
    VALUES """ + str(weapon[0:]) + ';'
  postgre_cursor.execute(insert_weapon)


# Commit changes so they persist

postgre_connection.commit()


# Close the connection

postgre_cursor.close()
