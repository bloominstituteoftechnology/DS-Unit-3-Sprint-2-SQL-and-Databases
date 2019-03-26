import pandas as pd
import sqlite3

subclass = ["charactercreator_cleric",
            "charactercreator_fighter",
            "charactercreator_mage",
            "charactercreator_necromancer",
            "charactercreator_thief"]
conn = sqlite3.connect('data/rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM charactercreator_character;'
curs.execute(query).fetchall()
print("There are", curs.execute(query).fetchall()[0][0], "Characters in the rpg_db database\n")

for character in subclass:
    query = "SELECT COUNT(*) FROM " + character + ';'
    curs.execute(query).fetchall()
    print("There are", curs.execute(query).fetchall()[0][0], "Characters in the", character, "table")

query = 'SELECT COUNT(*) FROM armory_item;'
items = curs.execute(query).fetchall()[0][0]
print("\nThere are", items, "Items in the armory_item table")

query = 'SELECT item_ptr_id FROM armory_weapon;'
weapons = curs.execute(query).fetchall()
print("\nThere are", len(weapons), "weapons in the armory_weapon table")
print("There are", items - len(weapons), "non-weapon items in the rpg_db database")
