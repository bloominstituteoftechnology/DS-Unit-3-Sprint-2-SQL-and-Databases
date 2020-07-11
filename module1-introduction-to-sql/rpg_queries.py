import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")

totalCharacters = 'select count(*) from charactercreator_character'
distinctNames = 'select count(distinct(name)) from charactercreator_character'
countClerics = 'select count(*) from charactercreator_cleric'
TOTAL_ARMORY_ITEMS = "SELECT COUNT(*) FROM armory_item"
COUNT_WEAPONS = (f"SELECT count(*)"
                 f" FROM"
                 f" armory_item ai JOIN armory_weapon aw"
                 f" ON aw.item_ptr_id = ai.item_id"
                 )

tables= c.fetchall()

subclassTables = []
[subclassTables.append(tableName[0]) for tableName in tables if 'charactercreator' in tableName[0] and (
    '_inventory' not in tableName[0])]
subclassTables
len(subclassTables)

for t in subclassTables:
    c.execute(f"select count(*) from {t}")
    print(f"{t} count:  {c.fetchall()[0][0]}")

numArmoryItems = c.execute(TOTAL_ARMORY_ITEMS).fetchall()[0][0]
numWeapons = c.execute(COUNT_WEAPONS).fetchall()[0][0]
print(f" total number of armory items: {numArmoryItems}")
print(f" total number of armory weapons: {numWeapons}"
        f"     non weapon items: {numArmoryItems - numWeapons}"
)