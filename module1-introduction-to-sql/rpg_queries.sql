-- SQLite

--How many total Characters are there?
SELECT COUNT(character_id) 
FROM charactercreator_character;

-- How many of each specific subclass?
SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;

SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer;

SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;

SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric;

SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;

--How many total Items?
SELECT COUNT(item_id) 
FROM armory_item;

--How many of the Items are weapons?
SELECT COUNT(item_ptr_id)
FROM armory_weapon;

--How many Items does each character have? (Return first 20 rows)
SELECT character_id,item_id
FROM charactercreator_character_inventory
LIMIT 20;

--How many Weapons does each character have?
SELECT character_id,item_id
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
LIMIT 20;

--On average, how many Items does each Character have?

--On average, how many Weapons does each character have?

