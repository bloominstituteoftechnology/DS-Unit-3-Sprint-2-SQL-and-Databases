-- SQLite
/*- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?*/
SELECT 'TOTAL' AS NAME, COUNT(*)
FROM charactercreator_character
UNION
SELECT 'CLERIC' 
AS NAME, COUNT(*)
FROM charactercreator_cleric
UNION
SELECT 'FIGHTER'
AS NAME, COUNT(*)
FROM charactercreator_fighter
UNION
SELECT 'MAGE'
AS NAME, COUNT(*)
FROM charactercreator_mage
UNION
SELECT 'NECROMANCER'
AS NAME, COUNT(*)
FROM charactercreator_necromancer
UNION
SELECT 'THIEF'
AS NAME, COUNT(*)
FROM charactercreator_thief;

SELECT COUNT(*)
AS NUMBER_OF_ITEMS
FROM charactercreator_character_inventory;

SELECT COUNT(armory_item.name)-COUNT(armory_weapon.power) AS ITEM_TOTAL,COUNT(armory_weapon.power) AS WEAPON_NUM
FROM charactercreator_character_inventory
INNER JOIN armory_item ON armory_item.item_id=charactercreator_character_inventory.item_id
LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id=charactercreator_character_inventory.item_id;

SELECT charactercreator_character_inventory.character_id, COUNT(armory_item.name), COUNT(armory_weapon.power)
FROM charactercreator_character_inventory
INNER JOIN armory_item ON armory_item.item_id=charactercreator_character_inventory.item_id
LEFT JOIN armory_weapon ON armory_weapon.item_ptr_id=charactercreator_character_inventory.item_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20;

select count(ai.item_id) - count(aw.item_ptr_id) as item_count
from charactercreator_character_inventory as cci
INNER JOIN armory_item as ai ON ai.item_id=cci.item_id
LEFT JOIN armory_weapon as aw ON aw.item_ptr_id=cci.item_id
group by cci.character_id;

select avg(item_count) as avg_item_num, avg(weap_count) as avg_weap_num FROM
(
    select count(ai.item_id) - count(aw.item_ptr_id) as item_count, count(aw.item_ptr_id) as weap_count
    from charactercreator_character_inventory as cci
    INNER JOIN armory_item as ai ON ai.item_id=cci.item_id
    LEFT JOIN armory_weapon as aw ON aw.item_ptr_id=cci.item_id
    group by cci.character_id
) t;