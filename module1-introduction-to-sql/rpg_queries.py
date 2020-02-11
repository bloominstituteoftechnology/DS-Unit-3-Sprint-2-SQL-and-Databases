import os
import sqlite3
import pandas as pd

RPG = os.path.join(os.path.dirname(__file__), "..", "SQL-Databases", "data", "rpg_db.sqlite3")

conn = sqlite3.connect(RPG)
curs = conn.cursor()

# How many total Characters are there?
query = '''SELECT COUNT(character_id)
           FROM charactercreator_character;
         '''
curs.execute(query)
total_characters = curs.fetchall()[0][0]
print(f'Total Characters: {total_characters}')

# How many of each specific subclass?
subclass = ['thief', 'cleric', 'fighter', 'mage']
for sub in subclass:
    query = f'SELECT COUNT(character_ptr_id) FROM charactercreator_{sub};'
    total_subclass = curs.execute(query).fetchall()[0][0]
    print(f'{sub}:', total_subclass)

query = "SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;"
total_necromancer = curs.execute(query).fetchall()[0][0]
print(f'Necromancer: {total_necromancer}')

# How many total Items?
query = "SELECT COUNT(item_id) FROM armory_item"
total_item = curs.execute(query).fetchall()[0][0]
print(f'Total of items are {total_item}')

# How many of the Items are not weapon?
query = """
           SELECT COUNT(item_id)
           FROM armory_item
           WHERE item_id NOT IN
           (
               SELECT item_ptr_id
               FROM armory_weapon
           )
        """
not_weapon = curs.execute(query).fetchall()[0][0]
print(f'Total regular items: {not_weapon}')

# How many Items does each character have? (Return first 20 rows)
query = """
           SELECT character_id, COUNT(item_id)
           FROM charactercreator_character_inventory
           GROUP BY character_id
           LIMIT 20;
        """
item_per_char = curs.execute(query).fetchall()
df = pd.DataFrame(item_per_char, columns = ['char_id', 'num_of_items'])
df = df.set_index('char_id')
print(df)

# How many Weapons does each character have? (Return first 20 rows)
query = """
           SELECT character_id, COUNT(item_id)
           FROM charactercreator_character_inventory
           WHERE item_id IN
           (
               SELECT item_ptr_id
               FROM armory_weapon
           )
           GROUP BY character_id
           LIMIT 20;
        """
weapon_per_char = curs.execute(query).fetchall()
df = pd.DataFrame(weapon_per_char, columns = ['char_id', 'num_of_weapons'])
df = df.set_index('char_id')
print(df)

# On average, how many Items does each Character have?
query = """
           SELECT AVG(item_count)
           FROM
           (
               SELECT COUNT(item_id) as item_count
               FROM charactercreator_character_inventory
               GROUP BY character_id
           );
        """
avg_item = curs.execute(query).fetchall()[0][0]
print(f'On average, each character has {avg_item} items')

# On average, how many Weapons does each Character have?
query = """
           SELECT AVG(weapon_count)
           FROM
           (
               SELECT COUNT (item_id) as weapon_count
               FROM charactercreator_character_inventory
               WHERE item_id IN
               (
                   SELECT item_ptr_id
                   FROM armory_weapon
               )
            GROUP BY character_id
           );
        """
avg_weapon = curs.execute(query).fetchall()[0][0]
print(f'On average, each character has {avg_weapon} weapons')