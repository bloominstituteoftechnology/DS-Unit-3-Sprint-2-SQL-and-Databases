
query1 = """
SELECT
	count()
FROM charactercreator_character
"""

# bad because I didn't know you could pass multible tables

query2 = """
SELECT
	count(distinct charactercreator_cleric.character_ptr_id) as cleric_count,
	count(distinct charactercreator_fighter.character_ptr_id) as fighter_count,
	count(distinct charactercreator_mage.character_ptr_id) as mage_count,
	count(distinct charactercreator_necromancer.mage_ptr_id) as necromancer_count,
	count(distinct charactercreator_thief.character_ptr_id) as thief_count
FROM charactercreator_character
LEFT JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
LEFT JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
LEFT JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
LEFT JOIN charactercreator_necromancer ON charactercreator_character.character_id = charactercreator_necromancer.mage_ptr_id
LEFT JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
"""

query3 = """
SELECT 
	count()
FROM armory_item
"""

query4 = """
SELECT 
	count(distinct armory_weapon.item_ptr_id) as weapon_count,
	count(distinct armory_item.item_id) - count(distinct armory_weapon.item_ptr_id) as non_weapon
FROM armory_item
LEFT JOIN armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id
"""

query5 = """
SELECT
	charactercreator_character.character_id,
	charactercreator_character.name,
	count(charactercreator_character_inventory.item_id) as inventory_count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""

query6 = """
SELECT
	charactercreator_character.character_id,
	charactercreator_character.name,
	count(armory_weapon.item_ptr_id) as weapon_count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id
LIMIT 20
"""

query7 = """
SELECT avg(avg_items) from
(SELECT
	character_id,
	count(character_id) as avg_items
FROM charactercreator_character_inventory
GROUP BY character_id);
"""

query8 = """
SELECT avg(weapon_count) from
(SELECT
charactercreator_character.character_id,
	charactercreator_character.name,
	count(armory_weapon.item_ptr_id) as weapon_count
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character.character_id)
"""

queries = [query1,query2,query3,query4,query5,query6,query7,query8]