import sqlite3

conn = connect("rpg_db.sqlite3")

curs1 = conn.cursor()
Q1_sql_command = '''SELECT character_id as ID
FROM charactercreator_character AS char_sheet;''' 
curs1.execute(Q1_sql_command)


curs2 = conn.cursor()
Q2_sql_command = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric AS cleric;'''
curs2.execute(Q2_sql_command)
curs2 = conn.cursor()
Q2_sql_command = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter AS fight;'''
curs2.execute(Q2_sql_command)
curs2 = conn.cursor()
Q2_sql_command = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_mage AS mage;'''
curs2.execute(Q2_sql_command)
curs2 = conn.cursor()
Q2_sql_command = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_thief AS thief;'''
curs2.execute(Q2_sql_command)
curs2 = conn.cursor()
Q2_sql_command = '''SELECT COUNT(character_ptr_id)
FROM charactercreator_necro AS necro;'''
curs2.execute(Q2_sql_command)


curs3 = conn.cursor()
Q3_sql_command = '''SELECT COUNT(item_id)
FROM armory_item AS item;'''
curs3.execute(Q3_sql_command)


curs4 = conn.cursor()
Q4_sql_command = '''SELECT COUNT(item_id)
FROM armory_item AS item
JOIN armory_weapon AS weap
ON item.item_id = weap.item_ptr_id;'''
curs4.execute(Q4_sql_command)
curs4 = conn.cursor()
Q4_sql_command = '''SELECT COUNT(item_id)
FROM armory_item
LEFT OUTER JOIN armory_weapon
ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id IS null'''
curs4.execute(Q4_sql_command)


curs5 = conn.cursor()
Q5_sql_command = '''SELECT inv.character_id, COUNT(inv.item_id)
FROM charactercreator_character_inventory as inv
GROUP BY inv.character_id
LIMIT 20;'''
curs5.execute(Q5_sql_command)


curs6 = conn.cursor()
Q6_sql_command = '''SELECT inv.character_id, COUNT(inv.item_id)
FROM charactercreator_character_inventory as inv
JOIN armory_weapon AS weap
WHERE inv.item_id = weap.item_ptr_id
GROUP BY inv.character_id
LIMIT 20;'''
curs6.execute(Q6_sql_command)


curs7 = conn.cursor()
Q7_sql_command = '''SELECT AVG(a)
from(
SELECT COUNT(inv.item_id) AS a
FROM charactercreator_character_inventory as inv
GROUP BY inv.character_id
)as c'''
curs7.execute(Q7_sql_command)


curs8 = conn.cursor()
Q8_sql_command = '''SELECT AVG(a)
from(
SELECT inv.character_id, COUNT(inv.item_id) AS a
FROM charactercreator_character_inventory as inv
JOIN armory_weapon AS weap
WHERE inv.item_id = weap.item_ptr_id
GROUP BY inv.character_id
)as c'''
curs8.execute(Q8_sql_command)


conn.commit()
conn.close()
