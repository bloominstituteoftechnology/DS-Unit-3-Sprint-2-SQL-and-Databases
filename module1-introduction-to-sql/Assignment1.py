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
print(f'{len(result)} items are not.\n')

# How many items for each character
# I'm not sure I'm doing this one right... RETURN TO THIS ONE!
print('How many Items does each character have? (Return first 20 rows)')
cur.execute('''
    SELECT name, character_id, COUNT(*) item_id
    FROM charactercreator_character_inventory cci
    INNER JOIN charactercreator_character cc
    USING (character_id) 
    GROUP BY character_id
    ORDER BY character_id
    LIMIT 20;
''')
result = cur.fetchall()
print('There are anywhere from 1 to 5 items for each of the first 20 characters\n')

# How many items are weapons?
print('How many Weapons does each character have? (Return first 20 rows)')
cur.execute('''
    SELECT character_id, name, item_id, item_ptr_id, COUNT(*) item_id
    FROM charactercreator_character_inventory cci
    INNER JOIN charactercreator_character cc
    USING (character_id) 
    INNER JOIN armory_weapon
    ON item_id = item_ptr_id
    GROUP BY character_id
    ORDER BY character_id
    LIMIT 20;
''')
result = cur.fetchall()
print('There are 1 to 2 items per character that are weapons.\n')

# Average number of items
print('On average, how many items does each character have?')
cur.execute('''
    CREATE TABLE average_items AS
	    SELECT name, character_id, COUNT(*) item_id
	    FROM charactercreator_character_inventory cci
	    INNER JOIN charactercreator_character cc
	    USING (character_id)
	    GROUP BY character_id
	    ORDER BY character_id
''')
cur.execute('''
    SELECT AVG(item_id)
    FROM average_items
''')
result = cur.fetchall()
print(f'There is an average of {result} items per character')

# Average number of weapons
print('On average, how many weapons does each character have?')
cur.execute('''
    CREATE TABLE average_weapon AS
	    SELECT character_id, name, item_ptr_id, COUNT(*) item_id
	    FROM charactercreator_character_inventory cci
	    INNER JOIN charactercreator_character cc
	    USING (character_id) 
	    INNER JOIN armory_weapon aw
	    ON item_id = item_ptr_id
	    GROUP BY character_id
	    ORDER BY character_id
''')
cur.execute('''
    SELECT AVG(item_id)
    FROM average_weapon
''')
result = cur.fetchall()
print(f'There is an average of {result} weapons per character')