import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()

c.execute('SELECT COUNT(character_id)'
          'FROM charactercreator_character;')
print('Number of Characters: ', c.fetchone()[0])

c.execute('SELECT COUNT(character_ptr_id)'
          'FROM charactercreator_cleric;')
print('Number of Clerics: ', c.fetchone()[0])

c.execute('SELECT COUNT(character_ptr_id)'
          'FROM charactercreator_fighter;')
print('Number of Fighters: ', c.fetchone()[0])

c.execute('SELECT COUNT(character_ptr_id)'
          'FROM charactercreator_mage;')
print('Number of Mages: ', c.fetchone()[0])

c.execute('SELECT COUNT(mage_ptr_id)'
          'FROM charactercreator_necromancer;')
print('Number of Necromancers: ', c.fetchone()[0])

c.execute('SELECT COUNT(character_ptr_id)'
          'FROM charactercreator_thief;')
print('Number of Thieves: ', c.fetchone()[0])

c.execute('SELECT COUNT(DISTINCT item_id)'
          'FROM charactercreator_character_inventory;')
print('Total number of Items: ', c.fetchone()[0])

'''
OR
c.execute('SELECT COUNT(item_id)'
          'FROM armory_item;')
print('Total number of Items: ', c.fetchone()[0])
'''

c.execute('SELECT COUNT(item_ptr_id)'
          'FROM armory_weapon;')
print('Total Weapons: ', c.fetchone()[0])

c.execute('SELECT COUNT(item_id) FROM'
          '(SELECT item_id FROM armory_item '
          'EXCEPT SELECT item_ptr_id FROM armory_weapon);')
print('Total Non-Weapon Items: ', c.fetchone()[0])

print('Number of items for first 20: ')
for i in range (0,20):
    c.execute('SELECT name, COUNT(item_id) FROM '
              'charactercreator_character as cc, '
              'charactercreator_character_inventory as cci '
              'WHERE cc.character_id = cci.character_id '
              'GROUP BY cc.name LIMIT 20;') 
              #LIMIT 20 USED IN SQL BUT NOT NEEDED BECAUSE
              # OF THE FOR LOOP
    print(c.fetchall()[i])

print('Number of weapons: ')
for i in range (0,20):
    c.execute('SELECT name, COUNT(item_id) FROM '
              'armory_weapon as aw, '
              'charactercreator_character as cc, '
              'charactercreator_character_inventory as cci '
              'WHERE cc.character_id = cci.character_id '
              'AND aw.item_ptr_id = cci.item_id '
              'GROUP BY cc.name LIMIT 20;') 
              #LIMIT 20 USED IN SQL BUT NOT NEEDED BECAUSE
              # OF THE FOR LOOP
    print(c.fetchall()[i])

c.execute('SELECT AVG(item_count) FROM '
          '(SELECT name, COUNT(item_id) as item_count FROM '
          'charactercreator_character as cc, '
          'charactercreator_character_inventory as cci '
          'WHERE cc.character_id = cci.character_id GROUP BY cc.name);')
print('Average Number of Items: ', c.fetchone()[0])

c.execute('SELECT AVG(weapon_count) FROM '
          '(SELECT name, COUNT(item_id) as weapon_count FROM '
          'armory_weapon as aw, '
          'charactercreator_character as cc, '
          'charactercreator_character_inventory as cci '
          'WHERE cc.character_id = cci.character_id '
          'AND aw.item_ptr_id = cci.item_id GROUP BY cc.name);')
print('Average Number of Weapons: ', c.fetchone()[0])