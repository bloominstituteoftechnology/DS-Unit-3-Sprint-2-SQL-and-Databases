import sqlite3 as sql

query_list = ["How many total Characters are there?",
        "How many of each specific subclass (cleric)?",
        "How many of each specific subclass (fighter)?",
        "How many of each specific subclass (mage)?",
        "How many of each specific subclass (necromancer)?",
        "How many of each specific subclass (thief)?",
        "How many total Items?",
        "How many of the Items are weapons?",
        "How many are not weapons?",
        "How many Items does each character have? (Return first 20 rows)",
        "How many Weapons does each character have? (Return first 20 rows)",
        "On average, how many Items does each Character have?",
        "On average, how many Weapons does each character have?"]

query_commands = ["""SELECT COUNT(*)
        FROM charactercreator_character;""",
        """SELECT COUNT(*)
        FROM charactercreator_cleric;""",
        """SELECT COUNT(*)
        FROM charactercreator_fighter;""",
        """SELECT COUNT(*)
        FROM charactercreator_mage;""",
        """SELECT COUNT(*)
        FROM charactercreator_necromancer;""",
        """SELECT COUNT(*)
        FROM charactercreator_thief;""",
        """SELECT COUNT(*)
        FROM armory_item;""",
        """SELECT COUNT(*)
        FROM armory_weapon;""",
        """SELECT COUNT(*)
        FROM armory_item
        LEFT JOIN armory_weapon
        ON armory_item.item_id = armory_weapon.item_ptr_id
        WHERE armory_weapon.item_ptr_id IS NULL;""",
        """SELECT character.name AS character_name, item.name AS item_name
        FROM charactercreator_character as character,
        armory_item as item,
        charactercreator_character_inventory as inventory
        WHERE character.character_id = inventory.character_id
        AND item.item_id = inventory.item_id
        LIMIT 20;""",
        """SELECT character.name AS character_name, item.name as weapon_name
        FROM charactercreator_character as character,
        charactercreator_character_inventory as inventory,
        armory_item as item,
        armory_weapon as weapon
        WHERE weapon.item_ptr_id = item.item_id
        AND item.item_id = inventory.item_id
        AND character.character_id = inventory.character_id
        LIMIT 20;""",
        """SELECT AVG(item_count)
        FROM (SELECT character.character_id AS character_id, COUNT(item.item_id) AS item_count
        FROM charactercreator_character as character,
        charactercreator_character_inventory as inventory,
        armory_item as item
        WHERE character.character_id = inventory.character_id
        AND item.item_id = inventory.item_id
        GROUP BY character.character_id);""",
        """SELECT AVG(weapon_count)
        FROM (
        SELECT character.character_id as character_id, count(item.item_id) as weapon_count
        FROM charactercreator_character as character,
        charactercreator_character_inventory as inventory,
        armory_item as item,
        armory_weapon as weapon
        WHERE weapon.item_ptr_id = item.item_id
        AND item.item_id = inventory.item_id
        AND character.character_id = inventory.character_id
        GROUP BY character.character_id);"""]

# Establish the connection to db file
conn = sql.connect('rpg_db.sqlite3')

for i in range(len(query_list)):
    print(query_list[i])
    print(query_commands[i])
    curs = conn.cursor()
    curs.execute(query_commands[i])
    print(curs.fetchall())
    curs.close()

conn.close()
