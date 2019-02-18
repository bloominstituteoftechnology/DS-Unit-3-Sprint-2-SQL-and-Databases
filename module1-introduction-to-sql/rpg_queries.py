"""Sqlite queries for rpg_db."""

import sqlite3


def count_characters(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT COUNT(character_id)
    FROM charactercreator_character;""").fetchone()[0]


def count_character_class(cursor, subclass):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT COUNT(*)
    FROM charactercreator_{}""".format(subclass)).fetchone()[0]


def count_items(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT COUNT(*)
    FROM armory_item""").fetchone()[0]


def count_weapons(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT COUNT(*)
    FROM armory_weapon""").fetchone()[0]


def count_non_weapons(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT COUNT(*)
    FROM armory_item
    WHERE item_id
    NOT IN (SELECT item_ptr_id FROM armory_weapon)""").fetchone()[0]


def avg_item_count_character(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT AVG(item_ct)
    FROM(
        SELECT COUNT(item_id) as item_ct
        FROM charactercreator_character_inventory
        GROUP BY character_id
    )""").fetchone()[0]


def avg_weapon_count_character(cursor):
    """Returns the number of characters from sqlite cursor.

    Args:
        cursor (sqlite3.Cursor): cursor to sqlite database
    Returns:
        (int) Number of characters.
    """
    return cursor.execute("""SELECT AVG(item_ct)
    FROM(
        SELECT COUNT(item_id) as item_ct
        FROM charactercreator_character_inventory
        WHERE item_id
        IN (SELECT item_ptr_id FROM armory_weapon)
        GROUP BY character_id
    )""").fetchone()[0]

if __name__ == "__main__":
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    print("COUNT CHARACTERS:", count_characters(curs))
    for sub in ["cleric", "fighter", "mage", "necromancer", "thief"]:
        out_str = "COUNT {} CHARACTERS:".format(sub.upper())
        print(out_str, count_character_class(curs, sub))
    print("COUNT ITEMS:", count_items(curs))
    print("COUNT WEAPONS:", count_weapons(curs))
    print("COUNT NONWEAPONS:", count_non_weapons(curs))
    print("AVG ITEMS PER CHARACTER:", avg_item_count_character(curs))
    print("AVG WEAPONS PER CHARACTER:", avg_weapon_count_character(curs))
