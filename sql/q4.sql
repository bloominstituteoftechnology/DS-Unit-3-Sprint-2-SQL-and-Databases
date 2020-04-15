-- find the amount of items that are wepons
-- and the amount of items that are not weapons
SELECT 
	count(i.item_id) as total_items,
	count(distinct w.item_ptr_id) as iswep
FROM armory_item as i
LEFT JOIN armory_weapon as w on i.item_id = w.item_ptr_id
-- ill do the rest in python
