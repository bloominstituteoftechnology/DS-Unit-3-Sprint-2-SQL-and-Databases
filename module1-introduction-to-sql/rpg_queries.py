#!/usr/bin/env python

import os
import sqlite3
import pandas as pd
#from tabulate import tabulate

#create db connection
CONN = sqlite3.connect('rpg_db.sqlite3')
cursor = CONN.cursor()

# 1 How many total characters are there?
query = 'SELECT COUNT (character_id) FROM charactercreator_character;'
ch_count = cursor.execute(query).fetchall()
ch_count = str(ch_count).strip('[](),')
print("There are ", ch_count, "characters.")
cursor.close()
CONN.commit()

cursor2 = CONN.cursor()
# 2.1 mage
query2 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_mage;'
mage = cursor2.execute(query2).fetchall()
mage = str(mage).strip('[](),')
print("There are", mage, "mages.")
cursor2.close()
CONN.commit()

cursor3 = CONN.cursor()
# 2.2 necromancers
query3 = 'SELECT COUNT (mage_ptr_id) FROM charactercreator_necromancer;'
necromancer = cursor3.execute(query3).fetchall()
necromancer = str(necromancer).strip('[](),')
print("There are ", necromancer, "necromancers.")
cursor3.close()
CONN.commit()

cursor4 = CONN.cursor()
# 2.3 thief
query4 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_thief;'
thief = cursor4.execute(query4).fetchall()
thief = str(thief).strip('[](),')
print("There are ", thief, "thieves.")
cursor4.close()
CONN.commit()

cursor5 = CONN.cursor()
query5 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_cleric;'
cleric = cursor5.execute(query5).fetchall()
cleric = str(cleric).strip('[](),')
print("There are ", cleric, "clerics.")
cursor5.close()
CONN.commit()

cursor6 = CONN.cursor()
#2.5 fighter
query6 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_fighter;'
fighter = cursor6.execute(query6).fetchall()
fighter = str(ch_count).strip('[](),')
print("There are ", fighter, "figheters.")
cursor6.close()
CONN.commit()

cursor7 = CONN.cursor()
# 3 How many total items
query7 = 'SELECT COUNT (item_id) FROM armory_item;'
items = cursor7.execute(query7).fetchall()
items = str(items).strip('[](),')
print("There are ", items, "items.")
cursor7.close()
CONN.commit()

cursor8 = CONN.cursor()
# 4 How many of the items are weapons? How many are not?
query8 = 'SELECT COUNT (item_ptr_id) FROM armory_weapon;'
query9 = 'SELECT COUNT (item_id) FROM armory_item;'
weapons = cursor8.execute(query8).fetchall()
weapons = str(weapons).strip('[](),')
not_weapons = cursor8.execute(query9).fetchall()
not_weapons = str(weapons).strip('[](),')
print("There are ", weapons, "items that are weapons.")
cursor8.close()
CONN.commit()

cursor9 = CONN.cursor()
#5 How many items does each character have? (Return first 20 rows.)
query10 = 'SELECT COUNT (item_id), character_id FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
items_per_character = cursor9.execute(query10).fetchall()
item_per_character = str(items_per_character).strip('[](),')
#print(tabulate(items_per_character, headers=["characters", "items"]))
cursor9.close()
CONN.commit()

cursor10 =CONN.cursor()
#6 How many weapons does each character have?
query11 = 'SELECT COUNT (item_ptr_id), character_id FROM armory_weapon, charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
weapons_per_character = cursor10.execute(query11).fetchall()
weapons_per_character = str(weapons_per_character).strip('[](),')
print(weapons_per_character)
cursor10.close()
CONN.commit()
cursor11=CONN.cursor()

#7 On average, how many items does each character have?
query12 = 'SELECT COUNT (item_id) / COUNT (character_id) FROM charactercreator_character_inventory LIMIT 20;'
items_avg = cursor11.execute(query12).fetchall()
items_avg = str(items_avg).strip('[](),')
print("Each character has", items_avg, "item on average.")
cursor11.close()
CONN.commit()

cursor12=CONN.cursor()
#8 On average, how many weapons does each character have?
query13 = 'SELECT COUNT (item_id) / COUNT (character_id) FROM armory_weapon, charactercreator_character_inventory;'
weapons_avg = cursor12.execute(query13).fetchall()
weapons_avg = str(weapons_avg).strip('[](),')
print("Each character has" , weapons_avg, " weapon on average.")
cursor12.close()
CONN.commit()
