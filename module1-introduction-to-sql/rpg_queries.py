from read_db import*

df = Load_Data('rpg_db.sqlite3')

print(df.make_query("*", "armory_item", "WHERE", "item_id = 1"))
