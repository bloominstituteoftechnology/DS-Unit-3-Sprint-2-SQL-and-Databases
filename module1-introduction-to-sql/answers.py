import pandas as pd
import sqlite3

# part 2 of assignment

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

"""
df = pd.read_csv('https://raw.githubusercontent.com/EvidenceN/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

query = df.to_sql(name='buddy', con=conn)
"""
curs = conn.cursor()

curs.execute('SELECT * FROM buddy').fetchall()

# get the names of the table
col_name_list = [tuple[0] for tuple in curs.description]
col_name_list

# - Count how many rows you have - it should be 249!

num_of_rows = curs.execute('SELECT count(*) FROM buddy').fetchall()
num_of_rows

#  - How many users who reviewed at least 100 `Nature` in the category also
  #reviewed at least 100 in the `Shopping` category?
    
nature_shopping = curs.execute("select count('User Id') from buddy where Nature >= 100 and Shopping >= 100").fetchall()
nature_shopping
# What are the average number of reviews for each category?

avg_sports = curs.execute('select round(avg(Sports), 0) from buddy').fetchall()
avg_sports

avg_religious = curs.execute('select round(avg(Religious), 0) from buddy').fetchall()
avg_religious

avg_Nature = curs.execute('select round(avg(Nature), 0) from buddy').fetchall()
avg_Nature

avg_Theatre = curs.execute('select round(avg(Theatre), 0) from buddy').fetchall()
avg_Theatre

avg_Shopping = curs.execute('select round(avg(Shopping), 0) from buddy').fetchall()
avg_Shopping

avg_Picnic = curs.execute('select round(avg(Picnic), 0) from buddy').fetchall()
avg_Picnic

curs.close()
conn.commit()

# establising second connection to rpg sql database

conn2 = sqlite3.connect('rpg_db.sqlite3')
curs2 = conn2.cursor()

# view all the table names
res = curs2.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
res

# - General overview of the dataset
char = curs2.execute('select * from charactercreator_character limit 10;').fetchall()
char

# character creator names of columns
char_name_list = [tuple[0] for tuple in curs2.description]
char_name_list

# - How many total Characters are there? total unique characters or total inventory of characters? assuming total number of characters and not including how much of each character in inentory. 

total_characters = curs2.execute('select count(*) from charactercreator_character;').fetchall()
total_characters

# - How many of each specific subclass in characters?
necromancer_subclass = curs2.execute('select count(*) from charactercreator_necromancer;').fetchall()
necromancer_subclass

cleric_subclass = curs2.execute('select count(*) from charactercreator_cleric;').fetchall()
cleric_subclass

fighter_subclass = curs2.execute('select count(*) from charactercreator_fighter;').fetchall()
fighter_subclass

mage_subclass = curs2.execute('select count(*) from charactercreator_mage;').fetchall()
mage_subclass

thief_subclass = curs2.execute('select count(*) from charactercreator_thief;').fetchall()
thief_subclass

# items table preview
arm = curs2.execute('select * from armory_item limit 10;').fetchall()
arm
type(arm)
# armory items column names
arm_name_list = [tuple[0] for tuple in curs2.description]
arm_name_list

# How many total Items?
total_armory = curs2.execute('select count(*) from armory_item;').fetchall()
total_armory

# How many of the Items are weapons? How many are not?

armory_weapon = curs2.execute('select count(*) from armory_weapon;').fetchall()
armory_weapon

not_weapon = total_armory[0][0] - armory_weapon[0][0]
not_weapon

# How many Items does each character have? (Return first 20 rows)

char_item = curs2.execute('select character_id, count(item_id) from charactercreator_character_inventory group by character_id limit 20;').fetchall()
char_item

# - How many Weapons does each character have? (Return first 20 rows)


weapon_char = curs2.execute('SELECT character_id,COUNT(item_ptr_id) FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE aw.item_ptr_id = ai.item_id AND ai.item_id = cci.item_id GROUP BY character_id LIMIT 20;').fetchall()
weapon_char
weapons = [tuple[0] for tuple in curs2.description]
weapons

# - On average, how many Items does each Character have?

avg_items = curs2.execute('select character_id, ROUND (AVG(item_id), 0) from charactercreator_character_inventory group by character_id LIMIT 20;').fetchall()
avg_items

# - On average, how many Weapons does each character have?

avg_weapons = curs2.execute ('SELECT character_id, avg(power) FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE aw.item_ptr_id = ai.item_id AND ai.item_id = cci.item_id GROUP BY character_id limit 20;').fetchall()
avg_weapons

curs2.close()
conn2.commit()


