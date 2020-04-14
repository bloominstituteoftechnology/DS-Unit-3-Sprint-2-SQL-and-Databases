



-- On average, how many Weapons does each character have?
-- assumption: include chars that don't have any weapons
-- intermediate step: 
--   302 rows (row per char)
--   two columns: one for the character, second for the weapon count
SELECT avg(weapon_count) as avg_weapons_per_char
FROM (
    SELECT 
      c.character_id
      ,c.name 
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory i ON c.character_id = i.character_id
    LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
    GROUP BY c.character_id
) subq