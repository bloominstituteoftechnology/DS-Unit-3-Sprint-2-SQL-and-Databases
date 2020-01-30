import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cur = sl_conn.cursor()

# Number of characters -- 302
sl_cur.execute("SELECT COUNT(character_id) FROM charactercreator_character")

sl_characters_table = sl_cur.fetchall()
print(sl_characters_table[0])
