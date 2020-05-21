import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = 'SELECT COUNT(*) FROM armory_item;'
curs.execute(query)
result = curs.execute(query).fetchall()
print(result)


# 1. How many total Chracters are there?
query_1 = 'SELECT COUNT(*) FROM charactercreator_character;'
ans_1 = curs.execute(query_1).fetchone()
print(f'How many total Characters are there? {ans_1}')

# 2. How many of each specfic subclass?
query_21 = 'SELECT COUNT(*) FROM charactercreator_cleric;'
query_22 = 'SELECT COUNT(*) FROM charactercreator_fighter;'
query_23 = 'SELECT COUNT(*) FROM charactercreator_mage;'
query_24 = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
query_25 = 'SELECT COUNT(*) FROM charactercreator_thief;'

ans_21 = curs.execute(query_21).fetchone()
ans_22 = curs.execute(query_22).fetchone()
ans_23 = curs.execute(query_23).fetchone()
ans_24 = curs.execute(query_24).fetchone()
ans_25 = curs.execute(query_25).fetchone()

print(f'How many of the subclass, cleric? {ans_21}')
print(f'How many of the subclass, fighter? {ans_22}')
print(f'How many of the subclass, mage? {ans_23}')
print(f'How many of the subclass, necromancer? {ans_24}')
print(f'How many of the subclass, thief? {ans_25}')

# 3. How many total items?
query_3 = 'SELECT COUNT(*) FROM armory_item;'
ans_3 = curs.execute(query_3).fetchone()
print(f'How many total items? {ans_3}')

# 4. How many of the items are weapons? How many are not?
query_41 = 'SELECT COUNT(*) FROM armory_item ai INNER JOIN armory_weapon aw on ai.item_id = aw.item_ptr_id;'
query_42 = 'SELECT COUNT(*) FROM armory_item ai LEFT JOIN armory_weapon aw on ai.item_id = aw.item_ptr_id WHERE aw.item_ptr_id IS NULL;'

ans_41 = curs.execute(query_41).fetchone()
ans_42 = curs.execute(query_42).fetchone()

print(f'How many of the items are weapons? {ans_41}')
print(f'How many of the items are not  weapons? {ans_42}')

# 5. How many items does each chracter have? (Return first 20 rows)
query_5 = 'select cc.name as character_name, cc.character_id, count(cci.id) as item_num from charactercreator_character cc inner join charactercreator_character_inventory cci on cci.character_id = cc.character_id group by cc.character_id LIMIT 20;'

ans_5 = curs.execute(query_5).fetchall()
print('How many items does each character have? (return first 20 rows)')
print(ans_5)

# 6. How many Weapons does each chracter have? (Return first 20 rows)
query_6 = 'select cc.name as character_name, cc.character_id, count(cci.id) as weapon_num from charactercreator_character cc inner join charactercreator_character_inventory cci on cci.character_id = cc.character_id inner join armory_item ai on ai.item_id = cci.item_id inner join armory_weapon aw on aw.item_ptr_id = ai.item_id group by cc.character_id LIMIT 20;'

ans_6 = curs.execute(query_6).fetchall()
print('How many Weapons does each chracter have? (Return first 20 rows)')
print(ans_6)

# 7. On average, how many items does each chracter have?
query_7 = 'select avg(item_num) from (select cc.name as character_name, cc.character_id, count(cci.id) as item_num from charactercreator_character cc inner join charactercreator_character_inventory cci on cci.character_id = cc.character_id group by cc.character_id LIMIT 20);'

ans_7 = curs.execute(query_7).fetchone()
print('On average, how many items does each character have?')
print(ans_7)

# 8. On average, how many Weapons does each chracter have?
query_8 = 'select avg(weapon_num) from (select cc.name as character_name, cc.character_id, count(cci.id) as weapon_num from charactercreator_character cc inner join charactercreator_character_inventory cci on cci.character_id = cc.character_id inner join armory_item ai on ai.item_id = cci.item_id inner join armory_weapon aw on aw.item_ptr_id = ai.item_id group by cc.character_id LIMIT 20);'

ans_8 = curs.execute(query_8).fetchone()
print('On average, how many Weapons does each character have?')
print(ans_8)
