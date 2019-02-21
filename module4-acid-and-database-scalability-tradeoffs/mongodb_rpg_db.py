"""MongoDB queries for rpg_db."""

import pymongo


def count_characters(db):
    """Returns the number of characters from MongoDB database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (int) Number of characters
    """
    agg_dict = [
        {
            "$count": "count"
        }
    ]
    agg_res = db["charactercreator.character"].aggregate(agg_dict)
    return list(agg_res)[0]["count"]


def count_character_class(db, subclass):
    """Returns the number of characters of subclass from MongoDB database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
        subclass (str): name of character class
    Returns:
        (int) Number of characters of subclass
    """
    agg_dict = [
        {
            "$count": "count"
        }
    ]
    agg_res = db["charactercreator.{}".format(subclass)].aggregate(agg_dict)
    return list(agg_res)[0]["count"]


def count_items(db):
    """Returns the number of items from MongoDB database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (int) Number of items
    """
    agg_dict = [
        {
            "$count": "count"
        }
    ]
    agg_res = db["armory.item"].aggregate(agg_dict)
    return list(agg_res)[0]["count"]


def count_weapons(db):
    """Returns the number of weapons from MongoDB database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (int) Number of weapons
    """
    agg_dict = [
        {
            "$count": "count"
        }
    ]
    agg_res = db["armory.weapon"].aggregate(agg_dict)
    return list(agg_res)[0]["count"]


def count_non_weapons(db):
    """Returns the number of nonweapon items from MongoDB database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (int) Number of nonweapon items
    """
    agg_dict = [
        {
            "$lookup":
            {
                'from': 'armory.weapon',
                'localField': 'pk',
                'foreignField': 'pk',
                'as': 'weapons_doc'
            }
        },
        {
            "$match":
            {
                "weapons_doc":
                {
                    "$eq": []
                }
            }
        },
        {
            "$count": "count"
        }
    ]
    agg_res = db["armory.item"].aggregate(agg_dict)
    return list(agg_res)[0]["count"]


def avg_item_count_character(db):
    """Returns the average number of items per character from MongoDB
    database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (float) Average number of items per character
    """
    agg_dict = [
        {
            "$lookup":
            {
                'from': 'armory.item',
                'localField': 'inventory',
                'foreignField': 'pk',
                'as': 'items_doc'
            }
        },
        {
            "$project":
            {
                "numberOfItems": {"$size": "$items_doc"}
            }
        },
        {
            "$group":
            {
                "_id": None,
                "avgItem": {"$avg": "$numberOfItems"}
            }
        }
    ]
    agg_res = db["charactercreator.character"].aggregate(agg_dict)
    return list(agg_res)[0]["avgItem"]


def avg_weapon_count_character(db):
    """Returns the average number of weapons per character from MongoDB
    database.

    Args:
        cursor (pymongo.database.Database): MongoDB database
    Returns:
        (float) Average number of weapons per character
    """
    agg_dict = [
        {
            "$lookup":
            {
                'from': 'armory.weapon',
                'localField': 'inventory',
                'foreignField': 'pk',
                'as': 'weapons_doc'
            }
        },
        {
            "$project":
            {
                "numberOfWeapons": {"$size": "$weapons_doc"}
            }
        },
        {
            "$group":
            {
                "_id": None,
                "avgWeapon": {"$avg": "$numberOfWeapons"}
            }
        }
    ]
    agg_res = db["charactercreator.character"].aggregate(agg_dict)
    return list(agg_res)[0]["avgWeapon"]


if __name__ == "__main__":
    # Username and password to be set by user.
    username = "TODO"
    password = "TODO"
    cluster = "TODO"
    group = "TODO"

    # Create access to MondoDB rpg database.
    s = "mongodb+srv://{}:{}@{}-{}.mongodb.net/rpg_db".format(username,
                                                              password,
                                                              cluster,
                                                              group)
    client = pymongo.MongoClient(s)
    rpg_db = client["rpg_db"]

    # Print results.
    print("COUNT CHARACTERS:", count_characters(rpg_db))
    for sub in ["cleric", "fighter", "mage", "necromancer", "thief"]:
        out_str = "COUNT {} CHARACTERS:".format(sub.upper())
        print(out_str, count_character_class(rpg_db, sub))
    print("COUNT ITEMS:", count_items(rpg_db))
    print("COUNT WEAPONS:", count_weapons(rpg_db))
    print("COUNT NONWEAPONS:", count_non_weapons(rpg_db))
    print("AVG ITEMS PER CHARACTER:", avg_item_count_character(rpg_db))
    print("AVG WEAPONS PER CHARACTER:", avg_weapon_count_character(rpg_db))
