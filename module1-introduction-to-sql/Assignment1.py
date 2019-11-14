import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

# Total characters
print('How many total Characters are there?')
cur.execute('SELECT * FROM charactercreator_character')
result = cur.fetchall()
print(f'There are {len(result)} characters.\n')

# Total of each subclass
print('How many of each specific subclass?')

# clerics
cur.execute('''
    SELECT *
    FROM charactercreator_character
    LEFT JOIN charactercreator_cleric
    ON character_id = character_ptr_id
    WHERE character_ptr_id IS NOT NULL
    ''')
result = cur.fetchall()
print(f'There are {len(result)} clerics.')

# fighters
cur.execute('''
    SELECT *
    FROM charactercreator_character
    LEFT JOIN charactercreator_fighter
    ON character_id = character_ptr_id
    WHERE character_ptr_id IS NOT NULL
    ''')
result = cur.fetchall()
print(f'There are {len(result)} fighters.')

# mages
cur.execute('''
    SELECT *
    FROM charactercreator_character
    LEFT JOIN charactercreator_mage
    ON character_id = character_ptr_id
    WHERE character_ptr_id IS NOT NULL
    ''')
result = cur.fetchall()
print(f'There are {len(result)} mages.')

# necromancers
cur.execute('''
    SELECT *
    FROM charactercreator_character
    LEFT JOIN charactercreator_necromancer
    ON character_id = mage_ptr_id
    WHERE mage_ptr_id IS NOT NULL
    ''')
result = cur.fetchall()
print(f'There are {len(result)} necromancers.')

# thiefs
cur.execute('''
    SELECT *
    FROM charactercreator_character
    LEFT JOIN charactercreator_cleric
    ON character_id = character_ptr_id
    WHERE character_ptr_id IS NOT NULL
    ''')
result = cur.fetchall()
print(f'There are {len(result)} thieves.\n')

# total items
print('How many total Items?')
cur.execute('SELECT * FROM armory_item')
result = cur.fetchall()
print(f'There are {len(result)} items.\n')

# Items as weapons
print('How many of the Items are weapons? How many are not?')
cur.execute('''
    SELECT *
    FROM armory_item ai
    LEFT JOIN armory_weapon
    ON item_id = item_ptr_id
    WHERE item_ptr_id IS NOT NULL
''')
result = cur.fetchall()
print(f'{len(result)} items are weapons.')
cur.execute('''
    SELECT *
    FROM armory_item ai
    LEFT JOIN armory_weapon
    ON item_id = item_ptr_id
    WHERE item_ptr_id IS NULL
''')
result = cur.fetchall()
print(f'{len(result)} items are not.')