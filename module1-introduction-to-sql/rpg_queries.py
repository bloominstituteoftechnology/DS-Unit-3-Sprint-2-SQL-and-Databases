import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM charactercreator_character;'
print(f'Total Characters: {curs.execute(query).fetchall()[0][0]}')

query_cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
print(f'Total Clerics: {curs.execute(query_cleric).fetchall()[0][0]}')

query_fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
print(f'Total Fighters: {curs.execute(query_fighter).fetchall()[0][0]}')

query_mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
print(f'Total Mages: {curs.execute(query_mage).fetchall()[0][0]}')

query_necromancer = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
print(f'Total Necros: {curs.execute(query_necromancer).fetchall()[0][0]}')

query_thief = 'SELECT COUNT(*) FROM charactercreator_thief;'
print(f'Total Thieves: {curs.execute(query_thief).fetchall()[0][0]}')

query_item = 'SELECT COUNT(*) FROM armory_item;'
print(f'Total Items: {curs.execute(query_item).fetchall()[0][0]}')

query_item_wep = 'SELECT COUNT(*) FROM armory_weapon;'
print(f'Total Weapons: {curs.execute(query_item_wep).fetchall()[0][0]}')

print(f'Total Non-Weapon Items: {174 - 37}')

query_inventory = 'SELECT charactercreator_character_inventory.character_id, charactercreator_character.name, charactercreator_character_inventory.item_id FROM charactercreator_character, charactercreator_character_inventory WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character_inventory.character_id LIMIT 20;'
print(f'First 20 Rows of Characters and Item Count: {curs.execute(query_inventory).fetchall()}')


