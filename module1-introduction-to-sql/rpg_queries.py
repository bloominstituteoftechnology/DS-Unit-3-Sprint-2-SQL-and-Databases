import sqlite3
import os

DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3')

connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row
print(type(connection))

cursor = connection.cursor()
print(type(cursor))
#print(dir(cursor))

num_chars = ("SELECT count(distinct character_id) as char_count FROM charactercreator_character")

result = cursor.execute(num_chars).fetchall()

item_avg_list = []

weapon_avg_list = []

for row in result:
    print(f"Unique Character Count: {row['char_count']}")
    item_avg_list.append(row['char_count'])
    weapon_avg_list.append(row['char_count'])

sub_dict = {}

num_mage =  """
            SELECT count(DISTINCT character_id) as mage_count FROM charactercreator_character JOIN 
            charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
            """

num_fighter = """
              SELECT count(DISTINCT character_id) as fighter_count FROM charactercreator_character JOIN 
              charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
              """

num_cleric = """
             SELECT count(DISTINCT character_id) as cleric_count FROM charactercreator_character JOIN 
             charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
             """

num_thief = """
            SELECT count(DISTINCT character_id) as thief_count FROM charactercreator_character JOIN 
            charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
            """

mage_result = cursor.execute(num_mage).fetchall()
fighter_result = cursor.execute(num_fighter).fetchall()
cleric_result = cursor.execute(num_cleric).fetchall()
thief_result = cursor.execute(num_thief).fetchall()

for row in mage_result:
    sub_dict.update({"mage": row['mage_count']})
for row in fighter_result:
    sub_dict.update({"fighter": row['fighter_count']})
for row in cleric_result:
    sub_dict.update({"cleric": row['cleric_count']})
for row in thief_result:
    sub_dict.update({"thief": row['thief_count']})

for subclass, count in sub_dict.items():
    print(f"Unique {subclass} count: {count}")

print(f"Check sum equals unique character count: {sum(sub_dict.values())}")

total_items = "SELECT count(item_id) as total_items FROM charactercreator_character_inventory"

item_result = cursor.execute(total_items).fetchall()

for row in item_result:
    print(f"Total Number of Items: {row['total_items']}")
    item_avg_list.append(row['total_items'])

num_weapons = """
              SELECT count(item_ptr_id) as weapon_count FROM charactercreator_character_inventory JOIN armory_weapon 
              ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
              """
num_non_weapons = """
                  SELECT count(item_id) as non_weapon_count FROM charactercreator_character_inventory WHERE item_id < 138
                  """

weapons_result = cursor.execute(num_weapons).fetchall()
non_weapons_result = cursor.execute(num_non_weapons).fetchall()

for row in weapons_result:
    print(f"Total Number of Weapons: {row['weapon_count']}")
    weapon_avg_list.append(row['weapon_count'])
for row in non_weapons_result:
    print(f"Total Number of Non-Weapon Items: {row['non_weapon_count']}")

item_per_character = """
                     SELECT 
                        charactercreator_character.character_id, charactercreator_character.name, 
                        count(charactercreator_character_inventory.character_id) as items_per_character 

                     FROM 
                        charactercreator_character 

                     INNER JOIN 
                        charactercreator_character_inventory 
                        ON charactercreator_character.character_id = charactercreator_character_inventory.character_id 

                     WHERE 
                        charactercreator_character_inventory.character_id in (charactercreator_character.character_id) 

                     GROUP BY 
                        charactercreator_character.character_id
                        
                     LIMIT
                        20
                     """

weapon_per_character = """
                       SELECT
                        charactercreator_character.character_id,
                        charactercreator_character.name,
                        count(charactercreator_character_inventory.item_id) as weapon_count
                       
                       FROM 
                        charactercreator_character
                       
                       INNER JOIN
                        charactercreator_character_inventory ON
                        charactercreator_character.character_id = charactercreator_character_inventory.character_id
                       
                       WHERE
                        charactercreator_character_inventory.character_id in (charactercreator_character.character_id) AND
                        item_id >= 138 
                       
                       GROUP BY 
                        charactercreator_character.character_id
                       
                       LIMIT
                        20
                       """
item_per_result = cursor.execute(item_per_character).fetchall()
weapon_per_result = cursor.execute(weapon_per_character).fetchall()

for row in item_per_result:
    print(f"{row['name']} carries {row['items_per_character']} item(s).")

for row in weapon_per_result:
    print(f"{row['name']} carries {row['weapon_count']} weapon(s).")

print(f"The average number of items held per character is {item_avg_list[1]/item_avg_list[0]:.2f}")
print(f"The average number of weapons held per character is {weapon_avg_list[1]/weapon_avg_list[0]:.2f}")

