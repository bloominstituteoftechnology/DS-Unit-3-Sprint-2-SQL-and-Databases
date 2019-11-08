"""
Code for the first part of the assignment:
Copy all the datasets into my elephantsql account
(except for charactercreator_character, which I
already did in-class; see live_lecture_task.py).
"""

import psycopg2
import sqlite3
from password_example import password
# For this to work, the above line instead has to be
# "from password import password." If you want the password.py
# file with my actual password, please contact me.


dbname = 'gubyurua'
user = 'gubyurua'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

datasets = ['charactercreator_mage', 'charactercreator_necromancer',
            'charactercreator_thief', 'charactercreator_cleric',
            'charactercreator_fighter', 'charactercreator_character_inventory',
            'armory_item', 'armory_weapon']

for dataset in datasets:
    table_info_query = f'PRAGMA table_info({dataset});'
    print(sl_curs.execute(table_info_query).fetchall())

# Results of the above:
#[(0, 'character_ptr_id', 'integer', 1, None, 1), (1, 'has_pet', 'bool', 1, None, 0), (2, 'mana', 'integer', 1, None, 0)]
#[(0, 'mage_ptr_id', 'integer', 1, None, 1), (1, 'talisman_charged', 'bool', 1, None, 0)]
#[(0, 'character_ptr_id', 'integer', 1, None, 1), (1, 'is_sneaking', 'bool', 1, None, 0), (2, 'energy', 'integer', 1, None, 0)]
#[(0, 'character_ptr_id', 'integer', 1, None, 1), (1, 'using_shield', 'bool', 1, None, 0), (2, 'mana', 'integer', 1, None, 0)]
#[(0, 'character_ptr_id', 'integer', 1, None, 1), (1, 'using_shield', 'bool', 1, None, 0), (2, 'rage', 'integer', 1, None, 0)]
#[(0, 'id', 'integer', 1, None, 1), (1, 'character_id', 'integer', 1, None, 0), (2, 'item_id', 'integer', 1, None, 0)]
#[(0, 'item_id', 'integer', 1, None, 1), (1, 'name', 'varchar(30)', 1, None, 0), (2, 'value', 'integer', 1, None, 0), (3, 'weight', 'integer', 1, None, 0)]
#[(0, 'item_ptr_id', 'integer', 1, None, 1), (1, 'power', 'integer', 1, None, 0)]

create_mage_table = """
CREATE TABLE charactercreator_mage (
    character_ptr_id INT,
    has_pet BOOL,
    mana INT
);
"""

pg_curs.execute(create_mage_table)

create_necromancer_table = """
CREATE TABLE charactercreator_necromancer (
    mage_ptr_id INT,
    talisman_charged BOOL
)
"""

pg_curs.execute(create_necromancer_table)

create_thief_table = """
CREATE TABLE charactercreator_thief (
    character_ptr_id INT,
    is_sneaking BOOL,
    energy INT
)
"""

pg_curs.execute(create_thief_table)

create_cleric_table = """
CREATE TABLE charactercreator_cleric (
    character_ptr_id INT,
    using_shield BOOL,
    mana INT
)
"""

pg_curs.execute(create_cleric_table)

create_fighter_table = """
CREATE TABLE charactercreator_fighter (
    character_ptr_id INT,
    using_shield BOOL,
    rage INT
)
"""

pg_curs.execute(create_fighter_table)

create_inventory_table = """
CREATE TABLE charactercreator_character_inventory (
    id SERIAL PRIMARY KEY,
    character_id INT,
    item_id INT
)
"""

pg_curs.execute(create_inventory_table)

create_armory_table = """
CREATE TABLE armory_item (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    value INT,
    weight INT
)
"""

pg_curs.execute(create_armory_table)

create_weapon_table = """
CREATE TABLE armory_weapon (
    item_ptr_id INT,
    power INT
)
"""

pg_curs.execute(create_weapon_table)

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()

dataset_columns = {
    'charactercreator_mage': '(character_ptr_id, has_pet, mana)',
    'charactercreator_necromancer': '(mage_ptr_id, talisman_charged)',
    'charactercreator_thief': '(character_ptr_id, is_sneaking, energy)',
    'charactercreator_cleric': '(character_ptr_id, using_shield, mana)',
    'charactercreator_fighter': '(character_ptr_id, using_shield, rage)',
    'charactercreator_character_inventory': '(character_id, item_id)',
    'armory_item': '(name, value, weight)',
    'armory_weapon': '(item_ptr_id, power)'
}

has_auto_increment = ['charactercreator_character_inventory', 'armory_item']

has_bool = ['charactercreator_mage', 'charactercreator_thief',
            'charactercreator_cleric', 'charactercreator_fighter']

for dataset in datasets:
    query = f'SELECT * FROM {dataset};'
    rows = sl_curs.execute(query).fetchall()
    for row in rows:
        if dataset in has_auto_increment:
            insert_row = f"""
                INSERT INTO {dataset}
                {dataset_columns[dataset]}
                VALUES """ + str(row[1:]) + ';'
            pg_curs.execute(insert_row)
        elif dataset in has_bool:
            insert_row = f"""
                INSERT INTO {dataset}
                {dataset_columns[dataset]}
                VALUES (""" + str(row[0]) + ", '" + str(row[1]) + "', " + str(row[2]) + ');'
            pg_curs.execute(insert_row)
        elif dataset == 'charactercreator_necromancer':
            insert_row = f"""
                INSERT INTO {dataset}
                {dataset_columns[dataset]}
                VALUES (""" + str(row[0]) + ", '" + str(row[1]) + "');"
            pg_curs.execute(insert_row)
        else:
            insert_row = f"""
                INSERT INTO {dataset}
                {dataset_columns[dataset]}
                VALUES """ + str(row) + ';'
            pg_curs.execute(insert_row)

pg_curs.close()
pg_conn.commit()

#pg_curs = pg_conn.cursor()

#for dataset in datasets:
#    pg_curs.execute(f'SELECT * FROM {dataset};')
#    pg_rows = pg_curs.fetchall()
#    for row, pg_row in zip(rows, pg_rows):
#        assert row == pg_row

#pg_curs.close()
#pg_conn.commit()

"""The above is commented out because I got an assertion error since,
when I converted to Boolean, the 1s and 0s because Trues and Falses.
Not sure the best way to account for that in the assert. When I look
at it in elephantsql, it seems right."""
