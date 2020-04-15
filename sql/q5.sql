SELECT 
	x.character_name,
	x.item_name,
	count(x.character_name) as number_of_items
FROM (
	SELECT 
		chars.name as character_name,
		items.name as item_name
	FROM charactercreator_character_inventory as inv
	JOIN armory_item as items ON inv.item_id = items.item_id
	JOIN charactercreator_character as chars ON inv.character_id = chars.character_id

) x
GROUP BY x.character_name
ORDER BY number_of_items DESC
LIMIT 20