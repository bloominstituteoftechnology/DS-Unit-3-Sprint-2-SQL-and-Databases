import os
import psycopg2 as pg
import sqlite3

from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")

# conn = pg.connect(dbname=db_name, user=db_user,
                    # password=db_pass, host=db_host)
rpg_db = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')

# pg_cur = conn.cursor()
# sl_cur = rpg_db.cursor()



# # Created and added all characters to pg
# sl_cur.execute('SELECT * FROM charactercreator_character;')
# results = sl_cur.fetchall()
# create_character_table = '''
#     CREATE TABLE charactercreator_character (
#         character_id SERIAL PRIMARY KEY,
#         name varchar(30),
#         level int,
#         exp int,
#         hp int,
#         strength int,
#         intelligence int,
#         dexterity int,
#         wisdom int
#     );
# '''

# pg_cur.execute(create_character_table)

# for result in results:
#     insert_result = """INSERT INTO charactercreator_character
#         (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
#         VALUES""" + str(result[1:])
#     print(insert_result)
#     pg_cur.execute(insert_result)

# conn.commit()
# conn.close()

create_item_table = """
    CREATE TABLE armory_item (
        item_id SERIAL PRIMARY KEY,
        name varchar(30),
        value int,
        weight int
    );
"""

insert_items = """INSERT INTO armory_item (item_id, name, value, weight) VALUES """

create_weapon_table = """
    CREATE TABLE armory_weapon (
        item_ptr_id int references armory_item(item_id),
        power int
    );
"""

insert_weapons = """INSERT INTO armory_weapon (item_ptr_id, power) VALUES"""

create_inventory_table = """
    CREATE TABLE charactercreator_character_inventory (
        id SERIAL PRIMARY KEY,
        character_id int references charactercreator_character(character_id),
        item_id int references armory_item(item_id)
    );
"""

insert_inventory = """INSERT INTO charactercreator_character_inventory 
                        (id, character_id, item_id) VALUES"""

create_cleric_table = """
    CREATE TABLE charactercreator_cleric (
        character_ptr_id int references charactercreator_character(character_id),
        using_shield int,
        mana int
    );
"""

insert_cleric = """INSERT INTO charactercreator_cleric 
                    (character_ptr_id, using_shield, mana) VALUES"""

create_fighter_table = """
    CREATE TABLE charactercreator_fighter (
        character_ptr_id int references charactercreator_character(character_id),
        using_shield int,
        rage int
    );
"""

insert_fighter = """ INSERT INTO charactercreator_fighter (character_ptr_id, using_shield, rage) VALUES"""

create_mage_table = """
    CREATE TABLE charactercreator_mage (
        character_ptr_id int references charactercreator_character(character_id) UNIQUE,
        has_pet int,
        mana int
    );
"""

insert_mage = """ INSERT INTO charactercreator_mage (character_ptr_id, has_pet, mana) VALUES"""

create_necromancer_table = """
    CREATE TABLE charactercreator_necromancer (
        mage_ptr_id int references charactercreator_mage(character_ptr_id) UNIQUE,
        talisman_charged int
    );
"""

insert_necromancer = """ INSERT INTO charactercreator_necromancer (mage_ptr_id, talisman_charged) VALUES"""

create_thief_table = """
    CREATE TABLE charactercreator_thief (
        character_ptr_id int references charactercreator_character(character_id),
        is_sneaking int,
        energy int
    );
"""

insert_thief = """ INSERT INTO charactercreator_thief (character_ptr_id, is_sneaking, energy) VALUES"""

def create_and_fill_table(table_name, creation_string, insert_result):
    conn = pg.connect(dbname=db_name, user=db_user,
                    password=db_pass, host=db_host)
    pg_cur = conn.cursor()
    sl_cur = rpg_db.cursor()
    results = sl_cur.execute(f'SELECT * FROM {table_name};').fetchall()
    pg_cur.execute(creation_string)

    for result in results:
        # print(result)
        pg_cur.execute(insert_result + str(result) + ";")

    conn.commit()
    conn.close()

tables = {
    # "armory_item": [create_item_table, insert_items],
    # "armory_weapon": [create_weapon_table, insert_weapons],
    # "charactercreator_character_inventory": [create_inventory_table, insert_inventory],
    # "charactercreator_cleric": [create_cleric_table, insert_cleric],
    # "charactercreator_fighter": [create_fighter_table, insert_fighter],
    "charactercreator_mage": [create_mage_table, insert_mage],
    "charactercreator_necromancer": [create_necromancer_table, insert_necromancer],
    "charactercreator_thief": [create_thief_table, insert_thief]
}

for name, strings in tables.items():
    create_and_fill_table(name, strings[0], strings[1])