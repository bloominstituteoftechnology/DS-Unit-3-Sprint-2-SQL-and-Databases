# Imports
import sqlite3
import os

# Set path to database
DATABASE_FILEPATH = os.path.join(os.path.dirname(__file__), 'rpg_db.sqlite3') 

# Instantiate connection using filepath
connection = sqlite3.connect(DATABASE_FILEPATH) 
connection.row_factory = sqlite3.Row
print(type(connection)) # Check connection type

# Instantiate cursor
cursor = connection.cursor() 
print(type(cursor)) # Check cursor Type

# Create two empty lists for future use in average lists
item_avg_list = [] # Set item average list to empty for future use
weapon_avg_list = [] # Set weapon average list to empty for future use


# Create empty dictionary for use in future statement on subclass counts
sub_dict = {} # Set sub_dict to empty for future use


"""--------------------------------------- SQL COMMAND CODE ---------------------------------------"""


# SQL commands to select number of unique characters
num_chars = """ 
            SELECT 
                count(distinct character_id) as char_count 
            FROM 
                charactercreator_character
            """ 

# SQL commands to select counts for mage subclass
num_mage =  """
            SELECT 
                count(DISTINCT character_id) as mage_count 
            FROM 
                charactercreator_character 
            JOIN 
                charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
            """

# SQL commands to select counts for fighter subclass
num_fighter = """
              SELECT 
                count(DISTINCT character_id) as fighter_count 
              FROM 
                charactercreator_character 
              JOIN 
                charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
              """

# SQL commands to select counts for cleric subclass
num_cleric = """
             SELECT 
                count(DISTINCT character_id) as cleric_count 
             FROM 
                charactercreator_character 
             JOIN 
                charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
             """

# SQL commands to select counts for thief subclass
num_thief = """
            SELECT 
                count(DISTINCT character_id) as thief_count 
            FROM 
                charactercreator_character 
            JOIN 
                charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
            """

# SQL commands to select total number of items in character_inventory
total_items = """
              SELECT 
                count(item_id) as total_items 
              FROM 
                charactercreator_character_inventory
              """

# SQL commands to select total number of weapons in character inventory
num_weapons = """
              SELECT 
                count(item_ptr_id) as weapon_count 
              FROM 
                charactercreator_character_inventory 
              JOIN 
                armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
              """

# SQL commands to select total number of non-weapons in character inventory
num_non_weapons = """
                  SELECT 
                    count(item_id) as non_weapon_count 
                  FROM 
                    charactercreator_character_inventory 
                  WHERE 
                    item_id < 138
                  """

# SQL commands to select the first 20 rows of items per character
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

# SQL commands to select the first 20 rows of weapons per character
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


"""--------------------------------------- SQL EXECUTION CODE ---------------------------------------"""


# Instantiate execution; set execution to variable
num_chars_result = cursor.execute(num_chars).fetchall() 

# Return values from SQL subclass count execution
mage_result = cursor.execute(num_mage).fetchall() # Execute mage count
fighter_result = cursor.execute(num_fighter).fetchall() # Execute fighter count
cleric_result = cursor.execute(num_cleric).fetchall() # Execute cleric count
thief_result = cursor.execute(num_thief).fetchall() # Execute thief count

# Return total item count from SQL execution of total_items
item_result = cursor.execute(total_items).fetchall()

# Return weapon and non-weapon counts from SQL execution of num_weapons and num_non_weapons
weapons_result = cursor.execute(num_weapons).fetchall() # Execute num weapons
non_weapons_result = cursor.execute(num_non_weapons).fetchall() # Execute num non-weapons

# Return item per character and weapon per character lists from SQL execution of item_per_character and weapon_per_character
item_per_result = cursor.execute(item_per_character).fetchall() # Return item per character list
weapon_per_result = cursor.execute(weapon_per_character).fetchall() # Return weapon per character list


"""--------------------------------------- SQL RELAY CODE ---------------------------------------"""


# Return values from SQL execution
for row in num_chars_result:
    print(f"\nUnique Character Count: {row['char_count']}") # Print statement on unique character count
    item_avg_list.append(row['char_count']) # Append character count to item average list for future use
    weapon_avg_list.append(row['char_count']) # Append character count to weapon average list for future use

# Add resulting SQL subclass counts to previously created sub_class dictionary "sub_dict"
for row in mage_result:
    sub_dict.update({"mage": row['mage_count']}) # Add mage count to sub_dict
for row in fighter_result:
    sub_dict.update({"fighter": row['fighter_count']}) # Add fighter count to sub_dict
for row in cleric_result:
    sub_dict.update({"cleric": row['cleric_count']}) # Add cleric count to sub_dict
for row in thief_result:
    sub_dict.update({"thief": row['thief_count']}) # Add thief count to sub_dict

# Using key/value pairs in sub_dict print out a message relating subclass name and its corresponding count
for subclass, count in sub_dict.items():
    print(f"Unique {subclass} count: {count}")

# Check to ensure the sub_class counts in sub_dict match the unique character count
print(f"Check sum equals unique character count: {sum(sub_dict.values())}\n")

# Relay message indicating total number of character_inventory items
for row in item_result:
    print(f"Total Number of Items: {row['total_items']}")
    item_avg_list.append(row['total_items']) # Append total items count to previously created item average list for future use

# Relay weapon and non-weapon item counts in character inventories
for row in weapons_result:
    print(f"Total Number of Weapons: {row['weapon_count']}") # Relay message with weapon count
    weapon_avg_list.append(row['weapon_count']) # Append weapon count to previously created weapon average list for future use
for row in non_weapons_result:
    print(f"Total Number of Non-Weapon Items: {row['non_weapon_count']}\n") # Relay message with non-weapon count

# Relay message with first 20 characters and how many items they carry
for row in item_per_result:
    print(f"{row['name']} carries {row['items_per_character']} item(s).")

# Print newline
print("\n")

# Relay message with first 20 characters and how many weapons they carry
for row in weapon_per_result:
    print(f"{row['name']} carries {row['weapon_count']} weapon(s).")

# Relay message with average number of items held per character
print(f"\nThe average number of items held per character is {item_avg_list[1]/item_avg_list[0]:.2f}")

# Relay message with average number of weapons held per character
print(f"The average number of weapons held per character is {weapon_avg_list[1]/weapon_avg_list[0]:.2f}\n")


