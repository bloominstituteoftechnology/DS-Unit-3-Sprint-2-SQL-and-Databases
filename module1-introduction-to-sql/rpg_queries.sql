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
SELECT AVG(count_items)\
FROM (\
SELECT COUNT(cci.item_id ) AS count_items\
FROM charactercreator_character_inventory AS cci\
GROUP BY cci.character_id);
--On average, how many Weapons does each character have?
SELECT AVG(weapon_count)\
FROM (SELECT cci.character_id, \
SUM (CASE WHEN cci.item_id IN (\
SELECT ai.item_id FROM armory_item AS ai, \
armory_weapon AS aw \
WHERE ai.item_id = aw.item_ptr_id)\
THEN 1 ELSE 0 END) AS weapon_count\
FROM charactercreator_character_inventory AS cci\
GROUP BY cci.character_id );
