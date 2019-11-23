import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

cur = conn.cursor()

#/*How many total Characters are there?*/
cur.execute("SELECT COUNT(character_id) FROM charactercreator_character;")
print('total characters: ',cur.fetchall())

#/*How many of each specific subclass?*/
cur.execute("""SELECT COUNT(character_id) FROM charactercreator_character
WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_mage);""")
print('number of mages: ',cur.fetchall())

cur.execute("""SELECT COUNT(character_id) FROM charactercreator_character
WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_thief);""")
print('number of thieves: ',cur.fetchall())

cur.execute("""SELECT COUNT(character_id) FROM charactercreator_character
WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_cleric);""")
print('number of clerics: ', cur.fetchall())

cur.execute("""SELECT COUNT(character_id) FROM charactercreator_character
WHERE character_id IN (SELECT character_ptr_id FROM charactercreator_fighter);""")
print('number of fighters: ', cur.fetchall())

#/*How many total Items?*/
cur.execute("""SELECT COUNT(item_id) FROM armory_item;""")
print('total items: ',cur.fetchall())

#/*How many of the Items are weapons? How many are not?*/
cur.execute("""SELECT COUNT(item_id) FROM armory_item
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon);""")
print('total weapons: ',cur.fetchall())

cur.execute("""SELECT COUNT(item_id) FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);""")
print('total non-weapons: ',cur.fetchall())

#/*How many Items does each character have? (Return first 20 rows)*/
cur.execute("""SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20;""")
print('items per character: ',cur.fetchall())

#/*How many Weapons does each character have? (Return first 20 rows)*/
cur.execute("""SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id LIMIT 20;"""
)
print('weapons per character: ',cur.fetchall())

#/*On average, how many Items does each Character have?*/
cur.execute("""SELECT AVG(itemcount) FROM (
SELECT character_id, COUNT(item_id) AS itemcount
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20
);""")
print('average items per character: ',cur.fetchall())

#/*On average, how many Weapons does each character have?*/
cur.execute("""SELECT AVG(weaponcount) FROM (
SELECT character_id, COUNT(item_id) AS weaponcount
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id LIMIT 20
);""")
print('average weapons per character: ',cur.fetchall())

cur.close()