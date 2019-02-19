import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# How many total Characters are there?
query1 = """SELECT COUNT(name) 
FROM charactercreator_character;"""
curs.execute(query1)
curs.fetchall()

## How many of each specific subclass?
query8 = """SELECT 'mages', COUNT(*) 
FROM charactercreator_mage

UNION

SELECT 'clerics', COUNT(*) 
FROM charactercreator_cleric

UNION

SELECT 'fighter', COUNT(*) 
FROM charactercreator_fighter

UNION

SELECT 'thieves', COUNT(*) 
FROM charactercreator_thief;"""

curs.execute(query8)
curs.fetchall()

# How many total Items?
query2 = """SELECT COUNT(name) 
FROM armory_item;"""
curs.execute(query2)
curs.fetchall()

# How many of the Items are weapons? 
query3 = """SELECT COUNT(power)  
FROM armory_weapon;"""
curs.execute(query3)
curs.fetchall()

# How many are not?
query9 = '''SELECT COUNT(*)
FROM armory_item
WHERE item_id NOT IN
            (SELECT item_ptr_id
            FROM armory_weapon);'''
            
# How many Items does each character have? (Return first 20 rows)
query4 = """SELECT character_id, COUNT(character_id) AS items
FROM charactercreator_character_inventory 
GROUP BY character_id
LIMIT 20;"""
curs.execute(query4)
curs.fetchall()

# How many Weapons does each character have? (Return first 20 rows)

query5 = """SELECT character_id, COUNT(character_id) AS weapons
FROM armory_weapon AS weapon,
charactercreator_character_inventory AS inventory
WHERE weapon.item_ptr_id = inventory.item_id
GROUP BY inventory.character_id
LIMIT 20;"""
curs.execute(query5)
curs.fetchall()


# On average, how many Items does each Character have?

query6 = """SELECT AVG(items)
FROM (
    SELECT character_id, COUNT(item_id) AS items
    FROM charactercreator_character_inventory
    GROUP BY character_id);"""
curs.execute(query6)
curs.fetchall()

# On average, how many Weapons does each character have?
query7 = """SELECT AVG(weapons)
FROM(
    SELECT character_id, COUNT(character_id) AS weapons
    FROM armory_weapon AS weapon,
    charactercreator_character_inventory AS inventory
    WHERE weapon.item_ptr_id = inventory.item_id
    GROUP BY inventory.character_id);"""
curs.execute(query7)
curs.fetchall()

