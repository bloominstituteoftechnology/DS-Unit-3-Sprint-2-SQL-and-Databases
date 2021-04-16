import pandas as pd
import helper
import sqlite3

print('-'*80)
results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM charactercreator_character')
print('How many total Characters are there? ', results[0][0])


print('-'*80)
print('How many of each specific subclass? ')
results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM charactercreator_character as cc INNER JOIN charactercreator_mage as mage on cc.character_id = mage.character_ptr_id')
print('\tHow many of each mage subclass? ', results[0][0])

results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM charactercreator_character as cc INNER JOIN charactercreator_thief as thief on cc.character_id = thief.character_ptr_id')
print('How many of each thief subclass? ', results[0][0])

results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM charactercreator_character as cc INNER JOIN charactercreator_cleric as cleric on cc.character_id = cleric.character_ptr_id')
print('How many of each cleric subclass? ', results[0][0])

results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM charactercreator_character as cc INNER JOIN charactercreator_fighter as fighter on cc.character_id = fighter.character_ptr_id')
print('How many of each fighter subclass? ', results[0][0])

print('-'*80)
results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM armory_item')
print('How many total items?', results[0][0])

print('-'*80)
results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT COUNT(*) FROM armory_item as item INNER JOIN armory_weapon as weapon ON item.item_id = weapon.item_ptr_id')
print('How many of the items are weapons? ', results[0][0])
results = helper.select_all_query(
    'rpg_db.sqlite3', 'SELECT (SELECT COUNT(*) FROM armory_item) - (SELECT COUNT(*) FROM armory_item as item INNER JOIN armory_weapon as weapon ON item.item_id = weapon.item_ptr_id)')
print('How many of the items are not weapons? ', results[0][0])


print('-'*80)
print('How many Items does each character have? (Return first 20 rows)')
query = '''SELECT character_id as `Character Id`, COUNT(item_id) as `Item Count` 
FROM charactercreator_character_inventory 
GROUP BY character_id LIMIT 20'''
conn = helper.create_connection('rpg_db.sqlite3')
df = pd.read_sql(query, conn)
print(df)

print('-'*80)
print('How many Weapons does each character have? (Return first 20 rows)')
query = '''SELECT cci.character_id as `Character Id`, COUNT(aw.item_ptr_id) as `Weapon Count`
FROM charactercreator_character_inventory as cci
INNER JOIN armory_item as ai ON cci.item_id = ai.item_id
INNER JOIN armory_weapon as aw ON ai.item_id = aw.item_ptr_id
GROUP BY cci.character_id
LIMIT 20;'''
conn = helper.create_connection('rpg_db.sqlite3')
df = pd.read_sql(query, conn)
print(df)
