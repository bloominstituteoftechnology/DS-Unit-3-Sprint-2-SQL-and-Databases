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


