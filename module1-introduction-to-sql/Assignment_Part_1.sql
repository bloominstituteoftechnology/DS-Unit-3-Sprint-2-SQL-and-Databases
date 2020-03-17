-- How many total Characters are there?
SELECT COUNT() FROM charactercreator_character cc;


-- How many of each specific subclass?
SELECT COUNT(character_ptr_id) FROM charactercreator_cleric cc;
SELECT COUNT(character_ptr_id) FROM charactercreator_fighter cf;
SELECT COUNT(character_ptr_id) FROM charactercreator_mage cm;
SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer cn; -- THESE ARE A SUBCLASS OF MAGE
SELECT COUNT(character_ptr_id) FROM charactercreator_thief ct;

SELECT COUNT(DISTINCT charactercreator_cleric.character_ptr_id)as cleric
     , COUNT(DISTINCT charactercreator_fighter.character_ptr_id) as fighter
     , COUNT(DISTINCT charactercreator_mage.character_ptr_id) as mage
     -- , COUNT(DISTINCT charactercreator_necromancer.mage_ptr_id) as nec
     , COUNT(DISTINCT charactercreator_thief.character_ptr_id) as theif
FROM charactercreator_cleric
   , charactercreator_fighter
   , charactercreator_mage
   -- , charactercreator_necromancer
   , charactercreator_thief;
   


-- How many total Items?
SELECT COUNT(DISTINCT armory_item.item_id) 
FROM armory_item;



-- How many of the Items are weapons? How many are not?
SELECT COUNT(DISTINCT armory_item.item_id) as 'total items'
     , COUNT(DISTINCT armory_weapon.item_ptr_id) as weapons
     , (COUNT(DISTINCT armory_item.item_id)) - (COUNT(DISTINCT armory_weapon.item_ptr_id)) as 'non-weapons'
FROM armory_item
   , armory_weapon;
  

  
-- How many Items does each character have? (Return first 20 rows)
SELECT cc.character_id
     , cc.name 
     , COUNT(cci.item_id) AS 'num of items' 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
GROUP BY cc.character_id
LIMIT 20;



-- How many Weapons does each character have? (Return first 20 rows)
SELECT cc.character_id
     , cc.name 
     , COUNT(aw.item_ptr_id ) AS 'num of weapons' 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
LEFT JOIN armory_weapon aw
ON cci.item_id = aw.item_ptr_id
-- WHERE cci.item_id = aw.item_ptr_id 
GROUP BY cc.character_id
LIMIT 20;



/*
-- (HOW MANY WEAPONS DO THE CHARACTERS WITH WEAPONS HAVE?)
*/
SELECT cc.character_id
     , cc.name 
     , COUNT(aw.item_ptr_id ) AS 'num of weapons' 
FROM charactercreator_character cc
JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
JOIN armory_weapon aw
ON aw.item_ptr_id
WHERE cci.item_id = aw.item_ptr_id 
GROUP BY cc.character_id
LIMIT 20;



-- On average, how many Items does each Character have?
SELECT AVG(num_of_items)
FROM
(SELECT cc.character_id
     , cc.name 
     , COUNT(cci.item_id) AS num_of_items 
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
GROUP BY cc.character_id);



-- On average, how many Weapons does each character have?
SELECT AVG(num_of_weapons)
FROM 
(SELECT cc.character_id
     , cc.name 
     , COUNT(aw.item_ptr_id ) AS num_of_weapons
FROM charactercreator_character cc
LEFT JOIN charactercreator_character_inventory cci 
ON cc.character_id = cci.character_id
LEFT JOIN armory_weapon aw
ON cci.item_id = aw.item_ptr_id
-- WHERE cci.item_id = aw.item_ptr_id 
GROUP BY cc.character_id);