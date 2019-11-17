import sqlite3
!wget https://github.com/serinamarie/DS-Unit-3-Sprint-2-SQL-and-Databases/raw/master/module1-introduction-to-sql/rpg_db.sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')

# How many total Characters are there? 302
SELECT COUNT(character_id)
FROM charactercreator_character

# How many of each specific subclass?
    # Clerics =  75
    # Fighters = 68
    # Mages = 108
    # Necromancers = 11
    #Thieves = 51 */
SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric cc

SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter

SELECT COUNT(character_ptr_id)
FROM charactercreator_mage

SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer

SELECT COUNT(character_ptr_id)
FROM charactercreator_thief

# How many total Items? 174
SELECT COUNT
FROM armory_item

# How many of the Items are weapons? 37, 137 non-weapons
SELECT COUNT(item_ptr_id)
FROM armory_weapon

# How many Items does each character have?
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20

# How many Weapons does each character have?
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory cci
JOIN armory_weapon
WHERE item_id = item_ptr_id
GROUP BY character_id
LIMIT 20

# On average, how many Items does each Character have? 2.973
SELECT avg(c)
	FROM
	(
	SELECT character_id, COUNT(item_id) as c
	FROM charactercreator_character_inventory
	GROUP BY character_id
	)

# On average, how many Weapons does each character have? 1.309
SELECT avg(c)
	FROM
	(
	SELECT character_id, COUNT(item_id) as c
	FROM charactercreator_character_inventory cci
	JOIN armory_weapon
	WHERE item_id = item_ptr_id
	GROUP BY character_id
	)
