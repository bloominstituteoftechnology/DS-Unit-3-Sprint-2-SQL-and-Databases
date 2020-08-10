import sqlite3


def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# How many total Characters are there?
TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""


# How many of each specific subclass?
TOTAL_FIGHTERS = """
    SELECT COUNT(*)
    FROM charactercreator_fighter;
"""


TOTAL_MAGES = """
    SELECT COUNT(*)
    FROM charactercreator_mage;
"""


TOTAL_CLERICS = """
    SELECT COUNT(*)
    FROM charactercreator_cleric;
"""


TOTAL_THIEFS = """
    SELECT COUNT(*)
    FROM charactercreator_thief;
"""


TOTAL_NECROMANCERS = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
"""

# How many total Items?
TOTAL_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item;
"""


# How many of the Items are weapons? How many are not?
TOTAL_WEAPONS = """
    SELECT COUNT(*)
    FROM armory_weapon;
"""


TOTAL_NON_WEAPONS = """
    SELECT COUNT(*)
    FROM armory_item
    WHERE item_id < 138;
"""

# How many Items does each character have? (Return first 20 rows)
TOTAL_INVENTORY = """
    SELECT character_id, COUNT(*)
    FROM charactercreator_character_inventory
    GROUP BY character_id;
"""


# How many Weapons does each character have? (Return first 20 rows)
TOTAL_WEAPON_INVENTORY = """
    SELECT character_id, COUNT(*)
    FROM charactercreator_character_inventory, armory_weapon
    WHERE item_id = item_ptr_id
    GROUP BY character_id
"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    characters = execute_query(curs, TOTAL_CHARACTERS)
    fighters = execute_query(curs, TOTAL_FIGHTERS)
    mages = execute_query(curs, TOTAL_MAGES)
    clerics = execute_query(curs, TOTAL_CLERICS)
    thiefs = execute_query(curs, TOTAL_THIEFS)
    necromancers = execute_query(curs, TOTAL_NECROMANCERS)
    items = execute_query(curs, TOTAL_ITEMS)
    weapons = execute_query(curs, TOTAL_WEAPONS)
    non_weapons = execute_query(curs, TOTAL_NON_WEAPONS)
    total_inventory = execute_query(curs, TOTAL_INVENTORY)
    total_weapon_inventory = execute_query(curs, TOTAL_WEAPON_INVENTORY)

    print("There are %d total Characters." % (characters[0][0]))
    print("There are %d total Fighters." % (fighters[0][0]))
    print("There are %d total Mages." % (mages[0][0]))
    print("There are %d total Clerics." % (clerics[0][0]))
    print("There are %d total Thiefs." % (thiefs[0][0]))
    print("There are %d total Necromancers." % (necromancers[0][0]))
    print("There are %d total Items." % (items[0][0]))
    print("There are %d total Weapons." % (weapons[0][0]))
    print("There are %d total Non-Weapons." % (non_weapons[0][0]))

    for pair in total_inventory[:20]:
        print("Character %d has %d items." % (pair[0], pair[1]))
    for pair in total_weapon_inventory[:20]:
        print("Character %d has %d weapons." % (pair[0], pair[1]))

    num_items = 0
    num_weapons = 0
    for pair in total_inventory:
        num_items += pair[1]
    for pair in total_weapon_inventory:
        num_weapons += pair[1]
    print("On average, each Character has %f items?" % (num_items / characters[0][0]))
    print(
        "On average, each Character has %f weapons?" % (num_weapons / characters[0][0])
    )
