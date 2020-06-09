import sqlite3
conn = sqlite3.connect('/Users/user/Documents/GitHub/Lambda/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')
c = conn.cursor()


#How many total Characters there?
c1 = c
print(c1.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall())

#How many of each specific subclass?

print(len(c1.execute('SELECT * FROM charactercreator_character;').fetchall()[0][2:]))

#How many total items?

print(c1.execute('SELECT COUNT(*) FROM armory_item;').fetchall())

#How many of the Items are weapons? 

print(c1.execute('SELECT COUNT(*) FROM armory_weapon;').fetchall())

# How many are not?

print(len(c1.execute('SELECT * FROM armory_item;').fetchall()) - len(c1.execute('SELECT * FROM armory_weapon;').fetchall()))

# How many Items does each character have? (Return first 20 rows)

print(c1.execute('SELECT character_id, count(*) FROM charactercreator_character_inventory GROUP BY item_id LIMIT 20;').fetchall())

# How many Weapons does each character have? (Return first 20 rows)

print(c1.execute('SELECT cci.character_id,count(*) FROM armory_weapon as aw, charactercreator_character_inventory as cci WHERE cci.item_id = aw.item_ptr_id GROUP BY cci.character_id LIMIT 20;').fetchall())

# On average, how many Items does each Character have?

table = c1.execute('SELECT character_id, count(*) FROM charactercreator_character_inventory GROUP BY item_id;').fetchall()[:]

print(sum([x[1] for x in table]) / len(table))

# On average, how many Weapons does each character have?

table = c1.execute('SELECT cci.character_id,count(*) FROM armory_weapon as aw, charactercreator_character_inventory as cci WHERE cci.item_id = aw.item_ptr_id GROUP BY cci.character_id;').fetchall()

print(sum([x[1] for x in table]) / len(table))