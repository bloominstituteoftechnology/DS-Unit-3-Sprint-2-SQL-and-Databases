import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()

### PART 1
char = c.execute('SELECT * FROM charactercreator_character').fetchall()
print('# of characters',len(char))

#Subclasses: Mage, thief, cleric, fighter
mage = c.execute('SELECT * FROM charactercreator_mage').fetchall()
thief = c.execute('SELECT * FROM charactercreator_thief').fetchall()
cleric = c.execute('SELECT * FROM charactercreator_cleric').fetchall()
fighter = c.execute('SELECT * FROM charactercreator_fighter').fetchall()
print('# of Mages: ',len(mage))
print('# of Thieves: ',len(thief))
print('# of Clerics: ',len(cleric))
print('# of Fighters: ',len(fighter))

# items found in armory_item
item = c.execute('SELECT * FROM armory_item').fetchall()
print('# of items: ', len(item))

# weapons found in armory_weapon
weapon = c.execute('SELECT * FROM armory_weapon').fetchall()
print('# of weapons: ',len(weapon))

# items for a character found in charactercreator_character_inventory
char_inv = c.execute('SELECT character_id, count(item_id) FROM charactercreator_character_inventory GROUP BY character_id').fetchall()
print('20 rows of (character id, # of items): ',char_inv[:20])

# weapon ownership by a character can be compared between ..._inventory and armory_weapon
char_w = c.execute('SELECT character_id, count(item_id) as weapons FROM charactercreator_character_inventory as c, armory_weapon as w WHERE c.item_id = w.item_ptr_id GROUP BY character_id').fetchall()
print('20 rows of (character_id, # of weapons): ',char_w[:20])

# use sub query to get average
ave_item = c.execute('''SELECT avg(items)
                        FROM (SELECT count(item_id) as items
                        FROM charactercreator_character_inventory as c 
                        GROUP BY character_id )''').fetchall()
ave_weapon = c.execute('''SELECT avg(weapons)
                        FROM (SELECT count(item_id) as weapons
                        FROM charactercreator_character_inventory as c, armory_weapon as w
                        WHERE c.item_id = w.item_ptr_id 
                        GROUP BY character_id )''').fetchall()
print('Average items per character: ',ave_item)
print('Average weapons per character: ',ave_weapon)

