#using SQL queries answer the folowing
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3')

print('Verifying connection and cursor are instantiated')
print('----------------------------------------------------------')
con = sqlite3.connect(DB_FILEPATH)

#using row factory.  essentially returns a dict, instead of a tuple
con.row_factory = sqlite3.Row

print('Connection:', con)

cur = con.cursor()
print('Cursor:', cur)
print('----------------------------------------------------------')

#How may total Characters are there?
#TODO stretch: make this section a single query
q1 = '''
SELECT count(distinct c.character_id) as character_count
FROM charactercreator_character as c
'''

a1 = cur.execute(q1).fetchone()

print('There are', a1['character_count'], 'total Characters in the db')

character_count = a1['character_count']

#How many of each subclass?
#Watch that mage and necromancer don't duplicate

#cleric
q2 = '''
SELECT count(distinct clr.character_ptr_id) as cleric_count
FROM charactercreator_cleric as clr
'''

cleric_count = cur.execute(q2).fetchone()['cleric_count']

print('There are', cleric_count, 'Clerics')

#fighter
q3 = '''
SELECT count(distinct ftr.character_ptr_id) as fighter_count
FROM charactercreator_fighter as ftr
'''

fighter_count = cur.execute(q3).fetchone()['fighter_count']

print('There are', fighter_count, 'Fighters')

#mage - try to do with only sql
#based of my D&D 2nd edition mages are generalists wizards
#and necromancers are specialist wizards.  So even though
#we built this DB with necromancers as a subclass of mage
#my D&D purist would like to know how many mages (excluding necromancers)
#there are.  Basically an excuse to try and do a more complex sql query.

#for my future self, I am left joining mages and necromancers, but I'm only
#interested in mages that are not necromancers.  So any mages that are not
#necromancers won't have an entry in necromancer table, and thus will not have
#any data in the columns that come from the necromancer table. So I only look
#at the entries that have NULL in necro columns
q4 = '''
SELECT count(distinct mag.character_ptr_id) as mage_count
FROM charactercreator_mage as mag
LEFT JOIN charactercreator_necromancer as ncr
ON mag.character_ptr_id = ncr.mage_ptr_id
WHERE ncr.mage_ptr_id IS NULL
'''

mage_count = cur.execute(q4).fetchone()['mage_count']

print('There are', mage_count, 'Mages, that are not Necromancers')

#necromancer
q5 = '''
SELECT count(distinct ncr.mage_ptr_id) as necro_count
FROM charactercreator_necromancer as ncr
'''

necro_count = cur.execute(q5).fetchone()['necro_count']

print('There are', necro_count, 'Necromancers')

#thief
q6 = '''
SELECT count(distinct thf.character_ptr_id) as thief_count
FROM charactercreator_thief as thf
'''

thief_count = cur.execute(q6).fetchone()['thief_count']

print('There are', thief_count, 'Thieves')

#Quick Sanity check
total = cleric_count + fighter_count + mage_count + necro_count + thief_count

print('Did I count correctly?', total == character_count)
print('----------------------------------------------------------')

#How many total Items?
#TODO stretch: make this section a single query
q7 = '''
SELECT count(distinct inv.id) as item_count
FROM charactercreator_character_inventory as inv
'''

item_count = cur.execute(q7).fetchone()['item_count']

print('There are', item_count, 'total items')

#How many of the items are weapons? - inner join makes this pretty easy
q8 = '''
SELECT count(distinct inv.id) as weapon_count
FROM charactercreator_character_inventory as inv
INNER JOIN armory_weapon as wpn
ON inv.item_id = wpn.item_ptr_id
'''

weapon_count = cur.execute(q8).fetchone()['weapon_count']

#How many of the items are not weapons? - lets do with a 
q9 = '''
SELECT count(distinct inv.id) as not_weapon_count
FROM charactercreator_character_inventory as inv
LEFT JOIN armory_weapon as wpn
ON inv.item_id = wpn.item_ptr_id
WHERE wpn.item_ptr_id IS NULL
'''

not_weapon_count = cur.execute(q9).fetchone()['not_weapon_count']

print(f'{weapon_count} of which are weapons and {not_weapon_count} are not')
print('----------------------------------------------------------')

#How many items does each character have? First 20 rows
#How many Weapons does each character have? First 20 rows
q10 = '''
SELECT 
    cha.character_id
    ,cha.name
    ,count(distinct item_id) as total_items
    ,count(distinct item_ptr_id) as total_weapons
FROM charactercreator_character as cha
LEFT JOIN charactercreator_character_inventory as inv ON cha.character_id = inv.character_id
LEFT JOIN armory_weapon as wpn ON inv.item_id = wpn.item_ptr_id
GROUP BY cha.character_id
LIMIT 20
'''

response = cur.execute(q10).fetchall()

for row in response:
    id = row['character_id']
    items = row['total_items']
    weapons = row['total_weapons']

    #Names make for very ugly printing.  I'm using IDs, since names weren't
    #mentioned in the requirements.
    print(f'Character {id} has {items} items, {weapons} of which are weapons')

print('----------------------------------------------------------')

#Average, how many items does each Character have?
#Average, how many weapons does each character have?
#Lets use a subquery to do this

q11 = '''
SELECT
    avg(total_items) as average_items
    ,avg(total_weapons)as average_weapons
FROM (''' + q10.replace('LIMIT 20', '') + ')'

#weird flex but ok.  Probably would have been better off actually writing
#out the whole query for readability.  Oh well it works now lol.
resp2 = cur.execute(q11).fetchone()

print('Each characters has an average of', resp2['average_items'], 'items')
print('Each character has an average of', resp2['average_weapons'], 'weapons')
print('----------------------------------------------------------')
