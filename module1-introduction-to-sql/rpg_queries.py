from load_query import*

df = Load_Data('rpg_db.sqlite3')

print("#1 How many total Characters are there?")
df1 = df.make_query("COUNT(DISTINCT(name))", "charactercreator_character")
print(df1[0][0])
print("\n")
print("#2 How many of each specific subclass?")
df2 = df.make_query("COUNT(DISTINCT(character_id)) AS inv_count, COUNT(DISTINCT(character_ptr_id)) AS inv_count",
              "charactercreator_character_inventory, charactercreator_cleric"), df.make_query("COUNT(DISTINCT(fighter.character_ptr_id)), COUNT(DISTINCT(mage.character_ptr_id))",
              "charactercreator_fighter AS fighter, charactercreator_mage as mage"), df.make_query("COUNT(DISTINCT(necromancer.mage_ptr_id)) AS necromancer_characters, COUNT(DISTINCT(thief.character_ptr_id)) AS thief_characters",
              "charactercreator_necromancer AS necromancer, charactercreator_thief AS thief")
print(df2)
print("\n")
print("#3 How many total Items?")
df3 = df.make_query("COUNT(item_id)", "armory_item")
print(df3)
print("\n")
print("#4 How many of the Items are weapons? How many are not?")
df4 = df.make_query("COUNT(item_ptr_id)", "armory_weapon"),
df5 = df.make_query("COUNT(item_id)", "armory_item", "WHERE NOT EXISTS", "(SELECT item_ptr_id FROM armory_weapon WHERE armory_weapon.item_ptr_id = armory_item.item_id)")
print(df4)
print(df5)
print("\n")
print("#5 How many Items does each character have? (Return first 20 rows)")
df6 = df.make_query("character_id, COUNT(item_id)", "charactercreator_character_inventory", "GROUP BY character_id", "LIMIT 20")
print(df6)
print("\n")
print("#6 How many Weapons does each character have? (Return first 20 rows)")
df7 = df.make_query("COUNT(item_id)", "charactercreator_character_inventory AS inventory",
              "JOIN armory_weapon as weapon ON weapon.item_ptr_id = inventory.item_id",
              "GROUP BY character_id LIMIT 20")
print(df7)
print("\n")
print("#7 On average, how many Items does each Character have?")
df8 = df.make_query("AVG(num_items)",
              "(SELECT character_id, COUNT(item_id) as num_items FROM charactercreator_character_inventory GROUP BY character_id) AS grouped")
print(df8)
print("\n")
print("#8 On average, how many Weapons does each character have?")
df9 = df.make_query("AVG(weapon_items)",
              "(SELECT character_id, COUNT(item_id) as weapon_items FROM charactercreator_character_inventory WHERE EXISTS (SELECT item_ptr_id FROM armory_weapon WHERE armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id) GROUP BY character_id)")
print(df9)