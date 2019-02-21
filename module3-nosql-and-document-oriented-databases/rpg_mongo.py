#!/usr/bin/env python
import os
import pymongo

def num_total_characters(coll):
    count = coll.count_documents({'model': 'charactercreator.character'})
    print('Number of total characters:', count)

def num_characters_in_each_subclass(coll):

    clerics = coll.count_documents({'model': 'charactercreator.cleric'})
    fighters = coll.count_documents({'model': 'charactercreator.fighter'})
    mages = coll.count_documents({'model': 'charactercreator.mage'})
    thieves = coll.count_documents({'model': 'charactercreator.thief'})

    print("Num characters in each subclass:")
    print("  Number of total clerics:", clerics)
    print("  Number of total fighters:", fighters)
    print("  Number of total mages:", mages)
    print("  Number of total thieves:", thieves)

def num_total_items(coll, print_result = True):
    num_items = coll.count_documents({'model': 'armory.item'})

    if print_result:
        print("Number of total items:", num_items)
    return num_items

def num_total_weapons(coll, print_result = True):
    num_weapons = coll.count_documents({'model': 'armory.weapon'})

    if print_result:
        print("Number of total weapons:", num_weapons)
    return num_weapons

def num_weapons_and_other(coll):
    num_weapons = num_total_weapons(coll, print_result = False)
    num_items = num_total_items(coll, print_result = False)
    print("Number of items that are weapons:", num_weapons)
    print("Number of items that are not weapons:", num_items - num_weapons)

# def character_inventory(coll):
#    # inventory = list(coll.find({'model': 'charactercreator.character.inventory'}))
#    # inventory = list(coll.find({'model': {$regex : ".*inventory.*"}}))
#    from bson.son import SON
#    import pprint
#    pipeline = [
#        {"$unwind": "$tags"},
#        {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
#        {"$sort": SON([("count", -1), ("_id", -1)])}
#    ]
#    print(inventory)

if __name__ == "__main__":
    mongo_atlas_username = os.environ['MONGO_ATLAS_USERNAME']
    mongo_atlas_password = os.environ['MONGO_ATLAS_PASSWORD']

    connection_string = "mongodb://<USERNAME>:<PASSWORD>@cluster0-shard-00-00-q42xu.mongodb.net:27017,cluster0-shard-00-01-q42xu.mongodb.net:27017,cluster0-shard-00-02-q42xu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
    connection_string = connection_string.replace("<USERNAME>",
                                                  mongo_atlas_username)
    connection_string = connection_string.replace("<PASSWORD>",
                                                  mongo_atlas_password)
    print(connection_string)

    client = pymongo.MongoClient(connection_string)

    db = client.rpg_database
    coll = db.rpg_collection

    num_total_characters(coll)
    num_characters_in_each_subclass(coll)
    num_total_items(coll)
    num_weapons_and_other(coll)
    # character_inventory(coll)
