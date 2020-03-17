import sqlite3

DB_FILEPATH = 'rpg_db.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

query = f"""
SELECT
  count(distinct char.character_id),
  count(distinct m.character_ptr_id),
  SUM(n.talisman_charged IS NOT NULL) as necro_count,
  count(distinct c.character_ptr_id),
  count(distinct f.character_ptr_id),
  count(distinct t.character_ptr_id)
FROM charactercreator_character char
LEFT JOIN charactercreator_mage m ON m.character_ptr_id = char.character_id
LEFT JOIN charactercreator_necromancer n ON n.mage_ptr_id = m.character_ptr_id
LEFT JOIN charactercreator_cleric c ON c.character_ptr_id = char.character_id
LEFT JOIN charactercreator_fighter f ON f.character_ptr_id = char.character_id
LEFT JOIN charactercreator_thief t ON t.character_ptr_id = char.character_id

"""

result = cursor.execute(query).fetchall()[0]
print('', result[0], "Total Characters\n", result[1], "Mages\n", result[2], "Necromancers\n", result[3], "Clerics\n", result[3], "Fighters\n", result[4], "Thieves")