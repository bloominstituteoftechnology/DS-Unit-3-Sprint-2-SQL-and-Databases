import sqlite3
import statistics as stats

conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()

q1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'
CharIds = c.execute(q1)
CharNum = CharIds.fetchone()[0]

q2 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
ClerIds = c.execute(q2)
ClerNum = ClerIds.fetchone()[0]

q3 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
FigIds = c.execute(q3)
FigNum = FigIds.fetchone()[0]

q4 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
MagIds = c.execute(q4)
MagNum = MagIds.fetchone()[0]

q5 = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
NecIds = c.execute(q5)
NecNum = NecIds.fetchone()[0]

q6 = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
ThfIds = c.execute(q6)
ThfNum = ThfIds.fetchone()[0]

q8 = 'SELECT COUNT(item_id) FROM armory_item;'
ItemIds = c.execute(q8)
ItemNum = ItemIds.fetchone()[0]

q9 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
WepIds = c.execute(q9)
WepNum = WepIds.fetchone()[0]

NonWepNum = ItemNum - WepNum

q10 = 'SELECT character_id, count(character_id)\
       FROM charactercreator_character_inventory\
       GROUP by character_id'

Items = c.execute(q10)
ItemRows = Items.fetchmany(20)
ItemList = Items.fetchall()

ItemCount = []
for i in range(len(ItemList)):
    ItemCount.append(ItemList[i][1])

AvgItems = stats.mean(ItemCount)
AvgItems = round(AvgItems, 2)

q11 = 'SELECT character_id, count(character_id)\
       FROM (SELECT *\
             FROM charactercreator_character_inventory cci, armory_weapon ai\
             WHERE cci.item_id = ai.item_ptr_id\
            )\
       GROUP BY character_id'

Weps = c.execute(q11)
WepRows = Weps.fetchmany(20)
WepList = Weps.fetchall()

WepCount = []
for i in range(len(WepList)):
    WepCount.append(WepList[i][1])

AvgWeps = stats.mean(WepCount)
AvgWeps = round(AvgWeps, 2)

print(f'There are {CharNum} Characters')
print(f'There are {ClerNum} Clerics')
print(f'There are {MagNum} Mages')
print(f'There are {ThfNum} Thiefs')
print(f'There are {FigNum} Fighters')
print(f'There are {NecNum} Necromancers')
print(f'There are {ItemNum} Items')
print(f'There are {WepNum} Weapons')
print(f'There are {NonWepNum} non-weapon Items')
print(f'On average a player has {AvgItems} Items')
print(f'On average a player has {AvgWeps} Weapons')
print('\nList of first 20 (CharacterID, number of items they have)')
print(ItemRows)
print('\nList of first 20 (CharacterID, number of weapons they have)')
print(WepRows)
