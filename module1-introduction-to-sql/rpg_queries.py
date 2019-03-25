import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Count all characters
total_chars = """
SELECT COUNT(*) FROM charactercreator_character
"""

# Count each subclass
subclass_count = """
SELECT COUNT(*) FROM charactercreator_cleric
UNION
SELECT COUNT(*) FROM charactercreator_fighter
UNION
SELECT COUNT(*) FROM charactercreator_mage
UNION
SELECT COUNT(*) FROM charactercreator_thief;
"""

# Count all items
total_items = """
SELECT COUNT(*) FROM armory_item;
"""

# Count weapons, non-weapons
weapons_nonweapons = """
SELECT COUNT(*) FROM armory_weapon
UNION
SELECT (SELECT COUNT(*) AS non_weapon FROM armory_item) 
- (SELECT COUNT(*) AS weapon FROM armory_weapon);
"""

# Items of each character (20 rows)
items_per_char = """
SELECT c.character_id, c.name, i.item_id
FROM charactercreator_character AS c
INNER JOIN charactercreator_character_inventory AS i
ON c.character_id = i.character_id
LIMIT 20;
"""

# Weapons of each character (20 rows)
weapons_per_char = """
SELECT c.character_id, c.name, i.item_id
FROM charactercreator_character AS c
INNER JOIN charactercreator_character_inventory AS i
ON c.character_id = i.character_id
WHERE i.item_id IN (SELECT item_ptr_id FROM armory_weapon)
LIMIT 20;
"""

# Average items
def avg_items():
    items_per_char = """
    SELECT c.character_id, c.name, i.item_id
    FROM charactercreator_character AS c
    INNER JOIN charactercreator_character_inventory AS i
    ON c.character_id = i.character_id;
    """
    df = pd.DataFrame(curs.execute(items_per_char).fetchall())
    counts = df[0].value_counts()
    return counts.mean()
    
# Average weapons
def avg_weapons():
    weapons_per_char = """
    SELECT c.character_id, c.name, i.item_id
    FROM charactercreator_character AS c
    INNER JOIN charactercreator_character_inventory AS i
    ON c.character_id = i.character_id
    WHERE i.item_id IN (SELECT item_ptr_id FROM armory_weapon);
    """
    df = pd.DataFrame(curs.execute(items_per_char).fetchall())
    counts = df[0].value_counts()
    return counts.mean()


