import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print('Number of characters')
print(curs.execute("SELECT COUNT(*) FROM charactercreator_character").fetchall())

print('Number of characters who are clerics')
print(curs.execute("\
SELECT COUNT(*) \
FROM charactercreator_character \
INNER JOIN charactercreator_cleric \
ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id; \
").fetchall())

print('Number of characters who are fighters')
print(curs.execute("\
SELECT COUNT(*) \
FROM charactercreator_character \
INNER JOIN charactercreator_fighter \
ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id; \
").fetchall())

print('Number of characters who are mages')
print(curs.execute("\
SELECT COUNT(*) \
FROM charactercreator_character \
INNER JOIN charactercreator_mage \
ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id; \
").fetchall())

print('Number of characters who are thieves')
print(curs.execute("\
SELECT COUNT(*) \
FROM charactercreator_character \
INNER JOIN charactercreator_thief \
ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id; \
").fetchall())

print('Total items')
print(curs.execute("SELECT COUNT(*) FROM armory_item").fetchall())

print('Number of items that are weapons')
print(curs.execute("SELECT COUNT(*) FROM armory_weapon").fetchall())

print('Number of items that are not weapons: ' + str(174-37))

print('Number of items the first 20 characters have')
print(curs.execute("\
SELECT charactercreator_character_inventory.character_id, COUNT(*) FROM \
charactercreator_character_inventory \
GROUP BY charactercreator_character_inventory.character_id \
LIMIT 20; \
").fetchall())

print('Number of weapons the first 20 characters have')
print(curs.execute("\
SELECT charactercreator_character_inventory.character_id, COUNT(*) FROM \
charactercreator_character_inventory \
WHERE charactercreator_character_inventory.item_id  IN (SELECT armory_weapon.item_ptr_id FROM armory_weapon) \
GROUP BY charactercreator_character_inventory.character_id \
LIMIT 20; \
").fetchall())

print('On average, how many Items does each Character have?')
print(curs.execute("\
SELECT AVG(theCount) FROM \
(SELECT charactercreator_character_inventory.character_id, COUNT(*) AS theCount FROM \
charactercreator_character_inventory \
GROUP BY charactercreator_character_inventory.character_id); \
").fetchall())

print('On average, how many Weapons does each character have?')
print(curs.execute("\
SELECT AVG(theCount) FROM \
(SELECT charactercreator_character_inventory.character_id, COUNT(*) AS theCount FROM \
charactercreator_character_inventory \
WHERE charactercreator_character_inventory.item_id  IN (SELECT armory_weapon.item_ptr_id FROM armory_weapon) \
GROUP BY charactercreator_character_inventory.character_id); \
").fetchall())

curs.close()