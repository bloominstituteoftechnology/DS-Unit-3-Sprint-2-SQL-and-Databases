/* how many total characters are there? */
select count(*) from charactercreator_character;

/* how many of each specific class? 
cleric, fighter, mage, nectromancer thief*/

select count(*) from charactercreator_cleric;

select count(*) from charactercreator_fighter;

select count(*) from charactercreator_mage;

select count(*) from charactercreator_necromancer;

select count(*) from charactercreator_thief;

/* How many total items */

select count(item_id) from charactercreator_character_inventory;

/* how many distinct weapons? */

select count(*) from (
	select cci.item_id, aw.item_ptr_id 
	from charactercreator_character_inventory as cci 
	inner join armory_weapon as aw 
	on cci.item_id = aw.item_ptr_id group by item_id
	);
	
/* how many are NOT weapons (Same query except != is used in last line) */
select count(*) from (
	select cci.item_id, aw.item_ptr_id 
	from charactercreator_character_inventory as cci 
	inner join armory_weapon as aw 
	on cci.item_id != aw.item_ptr_id group by item_id
	);
	
/* How many items does each character have? return first 20 rows */
select character_id, count(item_id) from charactercreator_character_inventory group by character_id limit 20;

/* How many weapons does each character have? return first 20 rows */
select inv.character_id, count(aw.item_ptr_id)
	from charactercreator_character_inventory as inv 
	inner join armory_weapon as aw 
	on inv.item_id = aw.item_ptr_id 
	group by character_id
	limit 20;
	
/* On average, how many Items does each character have? */

select avg(item_count) from (
	select character_id, count(item_id) as item_count 
	from charactercreator_character_inventory 
	group by character_id);
	
/* On average, how many weapons does each character have? 
same query except */
select avg(weapon_count) from(
        select count(aw.item_ptr_id) as weapon_count
                from charactercreator_character_inventory as inv
                inner join armory_weapon as aw
                on inv.item_id = aw.item_ptr_id
                group by character_id);

