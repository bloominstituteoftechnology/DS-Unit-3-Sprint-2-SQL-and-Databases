from load_data import*

df = Load_Data('rpg_db.sqlite3')

df.make_query("*", "armory_item", "LIMIT", "5")
