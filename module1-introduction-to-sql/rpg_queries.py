import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# How many total Characters are there?
q1 = "SELECT COUNT(*) FROM charactercreator_character;"  # 302

# How many of each specific subclass?
q2_cleric = "SELECT COUNT(*) FROM charactercreator_cleric;"  # 75
q2_fighter = "SELECT COUNT(*) FROM charactercreator_fighter;"  # 68
q2_mage = "SELECT COUNT(*) FROM charactercreator_mage;"  # 108
q2_necro = "SELECT COUNT(*) FROM charactercreator_necromancer;"  # 11
q2_thief = "SELECT COUNT(*) FROM charactercreator_thief;"  # 51

# How many total Items?
q3 = "SELECT COUNT(*) FROM armory_item;"  # 174

# How many of the Items are weapons? How many are not?
q4_weapons = """SELECT COUNT(*) FROM armory_item INNER JOIN armory_weapon
                ON armory_item.item_id = armory_weapon.item_ptr_id;"""  # 37
q4_nonweapons = """SELECT COUNT(*) FROM armory_item LEFT JOIN armory_weapon
                   ON armory_item.item_id = armory_weapon.item_ptr_id
                   WHERE armory_weapon.item_ptr_id IS NULL;"""  # 137

# How many Items does each character have? (Return first 20 rows)
q5 = """SELECT COUNT(*) FROM charactercreator_character as cc,
        charactercreator_character_inventory as cci
        WHERE cc.character_id = cci.character_id
        GROUP BY cc.character_id LIMIT 20;"""

# How many Weapons does each character have? (Return first 20 rows)
q6 = """SELECT COUNT(*) FROM charactercreator_character as cc,
        charactercreator_character_inventory as cci, armory_item as ai,
        armory_weapon as aw WHERE cc.character_id = cci.character_id AND
        cci.item_id = ai.item_id AND ai.item_id = aw.item_ptr_id
        GROUP BY cc.character_id LIMIT 20;"""

# On average, how many Items does each Character have?
q7 = """SELECT AVG(count) FROM
        (SELECT COUNT(*) as count FROM charactercreator_character as cc,
        charactercreator_character_inventory as cci
        WHERE cc.character_id = cci.character_id
        GROUP BY cc.character_id);"""  # 2.9

# On average, how many Weapons does each character have?
q8 = """SELECT AVG(count) FROM
        (SELECT COUNT(*) as count FROM charactercreator_character as cc,
        charactercreator_character_inventory as cci, armory_item as ai,
        armory_weapon as aw WHERE cc.character_id = cci.character_id AND
        cci.item_id = ai.item_id AND ai.item_id = aw.item_ptr_id
        GROUP BY cc.character_id);"""  # 1.3

print("Number of characters:", curs.execute(q1).fetchall()[0][0])
print("Number of clerics:", curs.execute(q2_cleric).fetchall()[0][0])
print("Number of fighters:", curs.execute(q2_fighter).fetchall()[0][0])
print("Number of mages:", curs.execute(q2_mage).fetchall()[0][0])
print("Number of necromancers:", curs.execute(q2_necro).fetchall()[0][0])
print("Number of thieves:", curs.execute(q2_thief).fetchall()[0][0])
print("Number of items:", curs.execute(q3).fetchall()[0][0])
print("Number of weapons:", curs.execute(q4_weapons).fetchall()[0][0])
print("Number of nonweapons:", curs.execute(q4_nonweapons).fetchall()[0][0])
print("How many items each of the first twenty characters have:",
      curs.execute(q5).fetchall())
print("How many weapons each of the first twenty characters have:",
      curs.execute(q6).fetchall())
print("Average items per character:", curs.execute(q7).fetchall()[0][0])
print("Average weapons per character:", curs.execute(q8).fetchall()[0][0])
curs.close()
conn.commit()
