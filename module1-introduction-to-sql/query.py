# Define query
# How many total characters are there
GET_CHARACTERS = """
    SELECT COUNT(*) AS Total_Char 
    FROM charactercreator_character;
    
"""
# How many of each specific subclass?
GET_CHARACTER_SUBCLASS = """
    SELECT COUNT(DISTINCT(name)) AS sub_class
    FROM charactercreator_character;
    
"""
# How many total Items?
GET_TOTAL_ITEMS = """
    SELECT COUNT(*) AS Total_Items
    FROM armory_item;
"""
# How many of the Items are weapons? 
GET_ITEMS_ARE_WEAPONS = """
    SELECT COUNT(item_id) AS items_weapons
    FROM   armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON aw.item_ptr_id = ai.item_id; 
"""
# How many are not?
GET_ITEMS_ARE_NOT_WEAPONS = """
    SELECT COUNT(*) AS items_not_weapons
    FROM   armory_item AS ai
    INNER JOIN armory_weapon AS aw
    ON aw.item_ptr_id != ai.item_id; 
"""
# How many Items does each character have? (Return first 20 rows)
GET_ITEMS_PER_CHARACTER = """
    SELECT
        cc.character_id,
        COUNT(DISTINCT ai.item_id) AS item_per_character
    FROM charactercreator_character AS cc
    LEFT JOIN charactercreator_character_inventory AS ci
    ON cc.character_id = ci.character_id
    LEFT JOIN armory_item AS ai
    ON ci.item_id = ai.item_id
    GROUP BY cc.character_id
    LIMIT 20

"""
# How many Weapons does each character have? (Return first 20 rows)
GET_ITEMS_PER_CHARACTER = """
    SELECT
        cc.character_id,
        COUNT(DISTINCT aw.item_ptr_id) AS weapon_per_character
    FROM charactercreator_character AS cc
    LEFT JOIN charactercreator_character_inventory AS ci
    ON cc.character_id = ci.character_id
    LEFT JOIN armory_weapon AS aw
    ON ci.item_id = aw.item_ptr_id
    GROUP BY cc.character_id
    LIMIT 20

"""
# On average, how many Items does each character have?
GET_ITEMS_PER_CHARACTER = """
        SELECT AVG(item_per_character) AS avg_weapon_per_char
        FROM (
            SELECT
                cc.character_id,
                COUNT(DISTINCT ai.item_id) AS item_per_character
            FROM charactercreator_character AS cc
            LEFT JOIN charactercreator_character_inventory AS ci
            ON cc.character_id = ci.character_id
            LEFT JOIN armory_item AS ai
            ON ci.item_id = ai.item_id
            GROUP BY cc.character_id

        )  
"""
# On average, how many Weapons does each character have?
GET_WEAPON_PER_CHARACTER = """
    SELECT AVG(weapon_count) AS avg_weapon_per_char
    FROM (
        SELECT
            cc.character_id,
            COUNT(DISTINCT aw.item_ptr_id) AS weapon_count
        FROM charactercreator_character AS cc
        LEFT JOIN charactercreator_character_inventory AS ci
        ON cc.character_id = ci.character_id
        LEFT JOIN armory_weapon AS aw
        ON ci.item_id = aw.item_ptr_id
        GROUP BY cc.character_id

    ) subq 
"""

QUERY_LIST = [GET_CHARACTERS, GET_CHARACTER_NAMES, GET_CHARACTER_SUBCLASS,
            GET_ITEMS, GET_ITEMS_ARE_NOT_WEAPONS, GET_ITEMS_ARE_WEAPONS,
            GET_ITEMS_PER_CHARACTER, GET_SUBCLASS, GET_TOTAL_ITEMS, GET_WEAPON_PER_CHARACTER]