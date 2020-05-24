import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")
c = conn.cursor()

print("""
-- How many total Characters are there?  """)
c.execute("""
    SELECT COUNT(character_id)
    FROM charactercreator_character;
""")
print(c.fetchone())


print("""
-- How many of each specific subclass?
-- cleric """)
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_cleric;
""")
print(c.fetchone())

print("-- fighter")
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_fighter;
""")
print(c.fetchone())

print("-- mage")
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_mage;
""")
print(c.fetchone())

print("-- necromancer")
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
""")
print(c.fetchone())

print("-- thief")
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_thief;
""")
print(c.fetchone())

print("""
-- How many total Items?  """)
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_character_inventory;
""")
print(c.fetchone())

print("""
-- How many of the Items are weapons? How many are not?  """)
c.execute("""
SELECT COUNT(*)
FROM charactercreator_character_inventory 
WHERE item_id IN (
	SELECT aw.item_ptr_id
	FROM armory_weapon aw);
""")
print(c.fetchone())

print("How many are not?")
c.execute("""
    SELECT COUNT(*)
    FROM charactercreator_character_inventory 
    WHERE item_id NOT IN (
            SELECT aw.item_ptr_id
            FROM armory_weapon aw);
""")
print(c.fetchone())

print("""
-- How many Items does each character have? (Return first 20 rows) """)
c.execute("""
    SELECT character_id, COUNT(*)
    FROM charactercreator_character_inventory 
    WHERE item_id NOT IN (
            SELECT aw.item_ptr_id
            FROM armory_weapon aw
    ) GROUP BY character_id
    LIMIT 20;
""")
print(c.fetchall())

print("""
-- How many Weapons does each character have? (Return first 20 rows) """)
c.execute("""
    SELECT character_id, COUNT(*)
    FROM charactercreator_character_inventory 
    WHERE item_id IN (
            SELECT aw.item_ptr_id
            FROM armory_weapon aw
    ) GROUP BY character_id
    LIMIT 20;
""")
print(c.fetchall())

print("""
 -- On average, how many Items does each Character have?  """)
c.execute("""
SELECT AVG(count_items)
FROM
(
    SELECT character_id, COUNT(*) AS count_items
    FROM charactercreator_character_inventory cci
    GROUP BY character_id );
""")
print(c.fetchone())

print("""
8 -- On average, how many Weapons does each character have?""")
c.execute("""
SELECT AVG(count_items)
FROM
(
    SELECT character_id, COUNT(*) AS count_items
    FROM charactercreator_character_inventory 
    WHERE item_id IN (
            SELECT aw.item_ptr_id
            FROM armory_weapon aw
    ) GROUP BY character_id );
""")
print(c.fetchone())

c.execute("""
        SELECT AVG(num_items) FROM (SELECT character_id, COUNT(*) as num_items FROM charactercreator_character_inventory GROUP BY character_id);
""")
print(c.fetchone())

conn.close()