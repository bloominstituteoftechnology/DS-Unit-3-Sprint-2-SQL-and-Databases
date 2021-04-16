#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


print("\nHow many total characters are there?")
query = "select count(*) from charactercreator_character;"
print(curs.execute(query).fetchall()[0][0])




print("\nHow many of each specific class?")
class_list = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
for cls in class_list:
    query = f"select count(*) from charactercreator_{cls};"
    print(f"{cls}:",curs.execute(query).fetchall()[0][0])




print("\nHow many total items?")
query = "select count(item_id) from charactercreator_character_inventory;"
print(curs.execute(query).fetchall()[0][0])




print("\nHow many distinct weapons?")
query = """
select count(*) from (
        select cci.item_id, aw.item_ptr_id
        from charactercreator_character_inventory as cci
        inner join armory_weapon as aw
        on cci.item_id = aw.item_ptr_id group by item_id
        );
"""
print(curs.execute(query).fetchall()[0][0])




print("\nHow many are NOT weapons") #(Same query except != is used in last line) 
query = """
select count(*) from (
        select cci.item_id, aw.item_ptr_id
        from charactercreator_character_inventory as cci
        inner join armory_weapon as aw
        on cci.item_id != aw.item_ptr_id group by item_id
        );
"""
print(curs.execute(query).fetchall()[0][0])




print("\nHow many items does each character have? return first 20 rows")
query = "select character_id, count(item_id) from charactercreator_character_inventory group by character_id limit 20;"
response = curs.execute(query).fetchall()
for char,count in response:
    print(f"char id: {char}\titem count: {count}") 




print("\nHow many weapons does each character have? return first 20 rows")
query = """
select inv.character_id, count(aw.item_ptr_id)
        from charactercreator_character_inventory as inv
        inner join armory_weapon as aw
        on inv.item_id = aw.item_ptr_id
        group by character_id
        limit 20;
"""
response = curs.execute(query).fetchall()
for char,count in response:
    print(f"char id: {char}\tweapon count: {count}")




print("\nOn average, how many Items does each character have?")
query = """
select avg(item_count) from (
        select character_id, count(item_id) as item_count
        from charactercreator_character_inventory
        group by character_id);
"""
print(curs.execute(query).fetchall()[0][0])




print("\nOn average, how many weapons does each character have")
query = """
select avg(weapon_count) from(
        select count(aw.item_ptr_id) as weapon_count
                from charactercreator_character_inventory as inv
                inner join armory_weapon as aw
                on inv.item_id = aw.item_ptr_id
                group by character_id);
"""
print(curs.execute(query).fetchall()[0][0])



curs.close()
conn.commit()

