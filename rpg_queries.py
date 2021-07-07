"""Code for querying rpg_db.sqlite3"""

"""
Questions:
How many total characters are there?
    302
How many of each specific subclass
    Cleric: 75
    Mage: 108
    Fighter: 68
    Thief: 51
    Necormancer: 11
How many total items?
    174
How many of the items are weapons? how many are not?
    37 weapons, 137 non-weapons
How many items does each character have? (Return first 20 rows)

How many weapons does each character have? (Return first 20 rows)

On average, how many items does each character have?

On average, how many weapons does each character have?

"""
import sqlite3

conn = sqlite3.connect('C:/Users/Phatdeluxe/lamdata/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')

curs = conn.cursor()

total_chars = 'SELECT count(*) FROM charactercreator_character;'

is_mage = 'SELECT count(*) FROM charactercreator_mage;'

is_cleric = 'SELECT count(*) FROM charactercreator_cleric;'

is_fighter = 'SELECT count(*) FROM charactercreator_fighter;'

is_thief = 'SELECT count(*) FROM charactercreator_thief;'

is_necromancer = 'SELECT count(*) FROM charactercreator_necromancer;'

item_count = 'SELECT count(*) FROM armory_item;'

weapons_count = 'SELECT count(*) FROM armory_weapon'

non_weapon_count = '''SELECT COUNT(*) 
FROM(SELECT item_id 
FROM armory_item 
EXCEPT 
SELECT item_ptr_id 
FROM armory_weapon);'''

char_items = 'SELECT character_id, COUNT(*) FROM charactercreator_character_inventory GROUP BY character_id HAVING COUNT(*) >= 0 LIMIT 20;'

char_weapons = 'SELECT character_id, item_id FROM charactercreator_character_inventory FULL OUTER JOIN armory_weapon ON item_id = item_ptr_id'

curs.execute(total_chars)
curs.execute(non_weapon_count)
curs.execute(char_weapons)
report = curs.fetchall()
print(report)
