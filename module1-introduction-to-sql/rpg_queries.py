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

cols = 'count(item_id)'
CHARACTER_JOIN_ITEM = (f"SELECT {cols} FROM charactercreator_character l"
                        f"JOIN charactercreator_character_inventory j"
                        f"ON"
                        f"l.character_id = j.character_id"
                        f"JOIN armory_item r ON"
                        f"j.item_id = r.item_id")

GROUPBY_CHARACTER = (F" GROUP BY character_id")
tables= c.fetchall()

subclassTables = []
[subclassTables.append(tableName[0]) for tableName in tables if 'charactercreator' in tableName[0] and (
    '_inventory' not in tableName[0])]
subclassTables
len(subclassTables)

print('\ncharacter counts by subclass:')
for t in subclassTables:
    c.execute(f"select count(*) from {t}")
    print(f"{t} count:  {c.fetchall()[0][0]}")

numArmoryItems = c.execute(TOTAL_ARMORY_ITEMS).fetchall()[0][0]
numWeapons = c.execute(COUNT_WEAPONS).fetchall()[0][0]
print(f" total number of armory items: {numArmoryItems}")
print(f" total number of armory weapons: {numWeapons}"
        f"     non weapon items: {numArmoryItems - numWeapons}"
        )
print(f"average ")  #sum and divide by total or find function


"""
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
"""
cols = 'count(j.item_id)'
CHARACTER_JOIN_ITEM = (f"SELECT {cols} FROM charactercreator_character l "
                        f"JOIN charactercreator_character_inventory j "
                        f"ON "
                        f"l.character_id = j.character_id "
                        f"JOIN armory_item r ON "
                        f"j.item_id = r.item_id ")

WHERE_ITEM_IS_WEAPON =(f"WHERE ")
GROUPBY_CHARACTER = (f" GROUP BY character_id")

ITEMS_PER_CHAR_FULL = CHARACTER_JOIN_ITEM + GROUPBY_CHARACTER  # fully composed query
AVG_IT_CHAR = f"SELECT avg(item_count) FROM ({ITEMS_PER_CHAR_FULL})" # Find avg item coutn

avgItemsPerCharacter = c.execute(AVG_IT_CHAR).fetchall()[0][0]
print (f"\nAverage Items Per Character: {avgItemsPerCharacter}")

print (ITEMS_PER_CHAR_FULL)
#plain SQL 
"""SELECT avg(item_count) 
   FROM ( select l.character_id, 
                count(j.item_id) item_count 
            FROM charactercreator_character l
            JOIN charactercreator_character_inventory j 
                ON l.character_id = j.character_id 
                JOIN armory_item r 
                ON j.item_id = r.item_id 
                GROUP BY l.character_id limit 20);
"""

