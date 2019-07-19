#!/usr/bin/env python

def main():
    import sqlite3
    conn = sqlite3.connect('rpg_db.sqlite3')
    c = conn.cursor()
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
    print('How many total Items? ',res[0])
    print('How many of the Items are weapons? How many are not?')
    c.execute('SELECT COUNT(*) FROM armory_weapon')
    weapons = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM armory_item WHERE item_id \
        NOT IN (SELECT item_ptr_id FROM armory_weapon)')
    non_weapons = c.fetchone()[0]
    print('Weapons ', weapons)
    print('Non-weapons ', non_weapons)
    
    print('How many Items does each character have? (Return first 20 rows):')
    items = c.execute('''
        SELECT character_id,
        count(charactercreator_character_inventory.item_id) as items
        FROM charactercreator_character_inventory
        GROUP by character_id LIMIT 20
        ''').fetchall()
    for i in items:
        print(f'Character ID: {i[0]}, # of items {i[1]}')

    print('How many Weapons does each character have? (Return first 20 rows)')
    weapons = c.execute('''
        SELECT character_id, count(item_ptr_id) as weapons
        FROM charactercreator_character_inventory
        LEFT JOIN armory_weapon on
        charactercreator_character_inventory.item_id =
        armory_weapon.item_ptr_id
        GROUP by character_id LIMIT 20
        ''').fetchall()

    avg_i = c.execute('''
        SELECT AVG(items) FROM
        (SELECT character_id,
        count(charactercreator_character_inventory.item_id)
        as items
        FROM charactercreator_character_inventory
        GROUP by character_id)
        ''').fetchone()[0]

    avg_w = c.execute('''
        SELECT AVG(weapons) FROM
        (SELECT character_id, count(item_ptr_id) as weapons
        FROM charactercreator_character_inventory
        LEFT JOIN armory_weapon on
        charactercreator_character_inventory.item_id =
        armory_weapon.item_ptr_id
        GROUP by character_id)
        ''').fetchone()[0]
    for i in weapons:
        print(f'Character ID: {i[0]}, # of weapons {i[1]}')

    print('On average, how many Items does each Character have? ', avg_i)
    print('On average, how many Weapons does each Character have? ', avg_w)
if __name__ == "__main__":
    main()