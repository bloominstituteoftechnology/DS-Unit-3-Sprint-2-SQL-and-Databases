from load_data import*

df = Load_Data('rpg_db.sqlite3')

df.make_query("*", "charactercreator_character", "LIMIT 5")
