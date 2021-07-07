"""Code for importing rpg data into a mongo db"""

"""
After completing this assignment I am seeing how simple, yet 'cowboy'
pymongo is compared to its SQL counterparts. You can easily create
new tables without having to make a CREATE TABLE statement.
One downside of this is that there is nothing enforcing what
kind of data is input into these tables. Between SQL packages,
you can easily transfer table data, where with mongo, you have to
write tons of for loops, and the column names have to be manually entered,
making it hard to write simple functions to automate the transfer of data.
I have not played around with it, but I do like that I can query
the elephantSQL once I have uploaded a table so I can see that
what I have done is actually working.
"""

import sqlite3
import pymongo

password = 'L7bBVGuzHz8QjX4j'

client = pymongo.MongoClient(f"mongodb://admin:{password}@cluster0-shard-00-00-pafox.mongodb.net:27017,cluster0-shard-00-01-pafox.mongodb.net:27017,cluster0-shard-00-02-pafox.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

sl_conn = sqlite3.connect('/Users/FluffyBear/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
character_list = sl_curs.execute(get_characters).fetchall()

for character in character_list:
    db.charactercreator_character.insert_one({
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'hp': character[3],
        'exp': character[4],
        'strength': character[5],
        'dexterity': character[6],
        'intelligence': character[7],
        'wisdom': character[8]
    })

get_mages = 'SELECT * FROM charactercreator_mage;'
mage_list = sl_curs.execute(get_mages).fetchall()

for mage in mage_list:
    db.charactercreator_mage.insert_one({
        'character_ptr_id': mage[0],
        'has_pet': mage[1],
        'mana': mage[2]
    })

get_necromancers = 'SELECT * FROM charactercreator_necromancer;'
necromancer_list = sl_curs.execute(get_necromancers).fetchall()

for necromancer in necromancer_list:
    db.charactercreator_necromancer.insert_one({
        'mage_ptr_id': necromancer[0],
        'talisman_charged': necromancer[1]
    })

get_fighters = 'SELECT * FROM charactercreator_fighter;'
fighter_list = sl_curs.execute(get_fighters).fetchall()

for fighter in fighter_list:
    db.charactercreator_fighter.insert_one({
        'character_ptr_id': fighter[0],
        'using_shield': fighter[1],
        'rage': fighter[2]
    })

get_thiefs = 'SELECT * FROM charactercreator_thief;'
thief_list = sl_curs.execute(get_thiefs).fetchall()

for thief in thief_list:
    db.charactercreator_thief.insert_one({
        'character_ptr_id': thief[0],
        'is_sneaking': thief[1],
        'energy': thief[2]
    })

get_clerics = 'SELECT * FROM charactercreator_cleric;'
cleric_list = sl_curs.execute(get_clerics).fetchall()

for cleric in cleric_list:
    db.charactercreator_cleric.insert_one({
        'character_ptr_id': cleric[0],
        'using_shield': cleric[1],
        'mana': cleric[2]
    })

get_char_items = 'SELECT * FROM charactercreator_character_inventory;'
char_item_list = sl_curs.execute(get_char_items).fetchall()

for item in char_item_list:
    db.charactercreator_character_inventory.insert_one({
        'id': item[0],
        'character_id': item[1],
        'item_id': item[2]
    })

get_items = 'SELECT * FROM armory_item;'
item_list = sl_curs.execute(get_items).fetchall()

for item in item_list:
    db.armory_item.insert_one({
        'item_id': item[0],
        'name': item[1],
        '"value"': item[2],
        'weight': item[3]
    })

get_weapons = 'SELECT * FROM armory_weapon;'
weapon_list = sl_curs.execute(get_weapons).fetchall()

for weapon in weapon_list:
    db.armory_weapon.insert_one({
        'item_ptr_id': weapon[0],
        'power': weapon[1]
    })

sl_curs.close()
