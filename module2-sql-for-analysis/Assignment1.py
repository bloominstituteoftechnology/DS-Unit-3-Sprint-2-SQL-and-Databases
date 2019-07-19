"""
Creates a Posgresql version of the rpg_db sqlite3 database copies the data.
"""

import psycopg2
import sqlite3
import os

DB = 'testOne',
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'


def create_table(con):
    pgcur = con.cursor()
    tables = [
        'charactercreator_character',
        'armory_item',
        'armory_weapon',
        'charactercreator_cleric',
        'charactercreator_fighter',
        'charactercreator_mage',
        'charactercreator_thief',
        'charactercreator_necromancer',
        'charactercreator_character_inventory'
    ]
    for table in tables:
        try:
            pgcur.execute(f'DROP TABLE {table} CASCADE')
        except (psycopg2.ProgrammingError,
                psycopg2.InternalError) as e:
            # Table Does not exist yet.
            pass
    con.commit()
    pgcur.execute('''
        CREATE TABLE charactercreator_character(
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
    ''')

    pgcur.execute('''
        CREATE TABLE armory_item(
            item_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            value INT,
            weight INT
        )
    ''')

    pgcur.execute('''
        CREATE TABLE armory_weapon(
            item_ptr_id INT PRIMARY KEY REFERENCES armory_item (item_id),
            name VARCHAR(30),
            power INT
        )
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_cleric(
            character_ptr_id INT PRIMARY KEY REFERENCES charactercreator_character (character_id),
            using_shield INT,
            mana INTEGER
        )
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_fighter(
            character_ptr_id INT PRIMARY KEY REFERENCES charactercreator_character (character_id),
            using_shield INT,
            rage INTEGER
        )
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_mage(
            character_ptr_id INT PRIMARY KEY REFERENCES charactercreator_character (character_id),
            has_pet INT,
            mana INTEGER
        )
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_thief(
            character_ptr_id INT PRIMARY KEY REFERENCES charactercreator_character (character_id),
            is_sneaking INT,
            energy INTEGER
        )
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_necromancer(
            mage_ptr_id INT PRIMARY KEY REFERENCES charactercreator_mage (character_ptr_id),
            is_sneaking INTEGER,
            energy INTEGER
        )
        
    ''')

    pgcur.execute('''
        CREATE TABLE charactercreator_character_inventory(
            id SERIAL PRIMARY KEY,
            character_id INT REFERENCES charactercreator_character (character_id),
            item_id INT REFERENCES armory_item (item_id)
        )
    ''')
    con.commit()


def populate_table(sqlcon, pgcon):
    sqcur = sqlcon.cursor()
    pgcur = pgcon.cursor()
    tables = [
        'charactercreator_character',
        'armory_item',
        'armory_weapon',
        'charactercreator_character_inventory',
        'charactercreator_cleric',
        'charactercreator_fighter',
        'charactercreator_mage',
        'charactercreator_thief',
        'charactercreator_necromancer'
    ]
    for table in tables:
        res = sqcur.execute(f'SELECT * FROM {table}').fetchall()
        for row in res:
            tmplt = ', '.join(['%s' for _ in row])
            pgcur.execute(f'INSERT INTO {table} VALUES ({tmplt})', row)
        pgcon.commit()


def print_report(con):
    c = con.cursor()
    c.execute('SELECT count(*) FROM charactercreator_character')
    res = c.fetchone()
    print('How many total Characters are there?: ', res[0])
    print('How many of each specific subclass?')
    c.execute('''
        SELECT 
        ( SELECT COUNT(*) FROM charactercreator_necromancer ) AS necromancer,
        ( SELECT COUNT(*) FROM charactercreator_cleric ) AS cleric,
        ( SELECT COUNT(*) FROM charactercreator_fighter ) AS fighter,
        ( SELECT COUNT(*) FROM charactercreator_mage ) AS mage,
        ( SELECT COUNT(*) FROM charactercreator_thief ) AS thief
        ''')
    res = c.fetchone()
    print(f'Necromancer: {res[0]}')
    print(f'Cleric: {res[1]}')
    print(f'Fighter: {res[2]}')
    print(f'Mage: {res[3]}')
    print(f'Thief: {res[4]}')
    c.execute('SELECT COUNT(*) FROM armory_item')
    res = c.fetchone()
    print('How many total Items? ', res[0])
    print('How many of the Items are weapons? How many are not?')
    c.execute('SELECT COUNT(*) FROM armory_weapon')
    weapons = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM armory_item WHERE item_id \
        NOT IN (SELECT item_ptr_id FROM armory_weapon)')
    non_weapons = c.fetchone()[0]
    print('Weapons ', weapons)
    print('Non-weapons ', non_weapons)

    print('How many Items does each character have? (Return first 20 rows):')
    c.execute('''
        SELECT character_id,
        count(charactercreator_character_inventory.item_id) as items
        FROM charactercreator_character_inventory
        GROUP by character_id LIMIT 20
        ''')
    items = c.fetchall()
    for i in items:
        print(f'Character ID: {i[0]}, # of items {i[1]}')

    print('How many Weapons does each character have? (Return first 20 rows)')
    c.execute('''
        SELECT character_id, count(item_ptr_id) as weapons
        FROM charactercreator_character_inventory
        LEFT JOIN armory_weapon on
        charactercreator_character_inventory.item_id =
        armory_weapon.item_ptr_id
        GROUP by character_id LIMIT 20
        ''')
    weapons = c.fetchall()

    c.execute('''
        SELECT AVG(items) FROM
        (SELECT character_id,
        count(charactercreator_character_inventory.item_id)
        as items
        FROM charactercreator_character_inventory
        GROUP by character_id) AS FOO
        ''')
    avg_i = c.fetchone()[0]

    c.execute('''
        SELECT AVG(weapons) FROM
        (SELECT character_id, count(item_ptr_id) as weapons
        FROM charactercreator_character_inventory
        LEFT JOIN armory_weapon on
        charactercreator_character_inventory.item_id =
        armory_weapon.item_ptr_id
        GROUP by character_id) AS FOO
        ''')
    avg_w = c.fetchone()[0]
    for i in weapons:
        print(f'Character ID: {i[0]}, # of weapons {i[1]}')

    print('On average, how many Items does each Character have? ', avg_i)
    print('On average, how many Weapons does each Character have? ', avg_w)


def main():
    pgcon = psycopg2.connect(
        dbname=DB, user=USER, password=PASSWORD, host=HOST)
    sqlcon = sqlite3.connect('rpg_db.sqlite3')
    sqcur = sqlcon.cursor()
    pgcur = pgcon.cursor()
    create_table(pgcon)
    populate_table(sqlcon, pgcon)
    print_report(pgcon)


if __name__ == "__main__":
    main()
