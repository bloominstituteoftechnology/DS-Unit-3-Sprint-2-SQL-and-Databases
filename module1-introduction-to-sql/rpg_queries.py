import sqlite3
# Total number of characters
conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()
cur.execute('SELECT name FROM charactercreator_character')
all_rows = cur.fetchall()
print(f'The number of characters is {len(all_rows)}.')
# Number by class
classlist = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
curx = conn.cursor()
class_ = []
for charclass in classlist:
    curx.execute(f'SELECT * FROM charactercreator_{charclass}');
    class_ = curx.fetchall();
    print(f'Members of the {charclass} class: {len(class_)}')
# Number of items
cur6 = conn.cursor()
cur6.execute("SELECT * FROM armory_item")
itemrows = cur6.fetchall()
print(f'There are {len(itemrows)} items in total')
# Number of weapons
cur7 = conn.cursor()
cur7.execute("SELECT * FROM armory_weapon")
weaponrows = cur7.fetchall()
print(f'There are {len(weaponrows)} weapons in total')
# First 20 characters' number of item
print("First 20 characters' number of items")
cur8 = conn.cursor()
for i in range(20):
    cur8.execute(f"SELECT COUNT(*) FROM charactercreator_character_inventory \
    WHERE character_id = {i}")
    inven = cur8.fetchall()
    print(inven[0][0])
# First 20 characters' number of weapons
print("First 20 characters' number of weapons")
cur9 = conn.cursor()
for i in range(20):
    cur9.execute(f"SELECT COUNT(*) FROM charactercreator_character_inventory \
    WHERE character_id = {i} AND item_id IN \
    (SELECT item_ptr_id FROM armory_weapon)")
    weap = cur9.fetchall()
    print(weap[0][0])
# Average number of items
cur1 = conn.cursor()
inv = []
for i in range(len(all_rows)):
    cur1.execute(f"SELECT COUNT(*) FROM charactercreator_character_inventory \
    WHERE character_id = {i}")
    invno = cur1.fetchall()
    inv.append(invno)
inv_ = [item[0] for item in inv]
inv3 = [item[0] for item in inv_]
print(f'Average number of items: {sum(inv3) / len(inv3)}')
# Average number of weapons
cur2 = conn.cursor()
inven = []
for i in range(len(all_rows)):
    cur2.execute(f"SELECT COUNT(*) FROM charactercreator_character_inventory \
    WHERE character_id = {i} AND item_id IN \
    (SELECT item_ptr_id FROM armory_weapon)")
    invno = cur2.fetchall()
    inven.append(invno)
inven_ = [item[0] for item in inven]
inven3 = [item[0] for item in inven_]
print(f'Average number of weapons: {sum(inven3) / len(inven3)}')
conn.close()
# No need to commit since we're just reading off data
