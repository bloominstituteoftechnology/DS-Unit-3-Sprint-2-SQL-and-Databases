import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

"""How many total Characters are there?"""
quest1 = 'SELECT COUNT(*) FROM charactercreator_character;'
answ1 = curs.execute(quest1)
print(f'Total characters: {answ1.fetchone()[0]}')

"""How many of each specific subclass?"""
def subclass(title):
    quest2 = 'SELECT COUNT(*) FROM charactercreator_' + title + ';'
    answ2 = curs.execute(quest2)
    print(f'Total subclass of {title}: {answ2.fetchone()[0]}')
subclass('fighter')
subclass('cleric')
subclass('mage')
subclass('thief')

"""How many total Items?"""
quest3 = 'SELECT COUNT(*) FROM armory_item;'
answ3 = curs.execute(quest3)
print(f'Total number of Items: {answ3.fetchone()[0]}')

"""How many of the Items are weapons? How many are not?"""
quest4 = 'SELECT COUNT(*) FROM armory_weapon;'
answ4 = curs.execute(quest4)
print (f'Total number of Weapons: {answ4.fetchone()[0]}')

quest4a = 'SELECT COUNT(aw.item_ptr_id) FROM armory_item AS ai, armory_weapon AS aw WHERE ai.item_id != aw.item_ptr_id;'
answ4a = curs.execute(quest4a)
print(f'Total number of non-weapon items: {answ4a.fetchone()[0]}')

"""How many Items does each character have? (Return first 20 rows)"""
quest5 = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20;'
answ5 = curs.execute(quest5)
print (f'Total number of Items of the first 20 characters: {answ5.fetchall()}')

"""How many Weapons does each character have? (Return first 20 rows)"""
quest6 = 'SELECT cci.character_id, COUNT(aw.item_ptr_id) FROM armory_item AS ai, armory_weapon AS aw, charactercreator_character_inventory AS cci WHERE cci.item_id = ai.item_id AND ai.item_id = aw.item_ptr_id GROUP BY cci.character_id LIMIT 20;'
answ6 = curs.execute(quest6)
print(f'Total number of weapons each character has: {answ6.fetchall()}'')

"""On average, how many Items does each Character have?"""
quest7 = 'SELECT AVG(ct) FROM (SELECT COUNT(item_id) AS ct FROM charactercreator_character_inventory GROUP BY character_id);'
answ7 = curs.execute(quest7)
print (f'Average items per character: {answ7.fetchone()[0]}')

"""On average, how many Weapons does each character have?"""
quest8 = 'SELECT AVG(ct) FROM (SELECT COUNT(aw.item_ptr_id) as ct FROM armory_item AS ai, armory_weapon AS aw, charactercreator_character_inventory AS cci WHERE cci.item_id = ai.item_id AND ai.item_id = aw.item_id GROUP BY cci.character_id);'
answ8 = curs.execute(quest8)
print(f'Average weapons per character: {answ8.fetchone()[0]}')
