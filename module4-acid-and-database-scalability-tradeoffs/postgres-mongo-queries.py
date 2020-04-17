
import pymongo
import psycopg2
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def main():
    mongo_queries()

    postgres_queries()

def mongo_queries():
    #connect to mongo db
    USER = os.getenv('MONGO_USER', default = 'oops')
    PASSWORD = os.getenv('MONGO_PASSWORD', default = 'oops')
    CLUSTER = os.getenv('MONGO_CLUSTER', default = 'oops')

    uri = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.mongodb.net/test?retryWrites=true&w=majority'

    client = pymongo.MongoClient(uri)

    db = client['rpg_db']

    
    # How many total Characters are there?
    tot_char = db['charactercreator_character'].count_documents({})
    print('Total Characters:', tot_char)

    # How many of each subclass?
    tot_cleric = db['charactercreator_cleric'].count_documents({})
    tot_fighter = db['charactercreator_fighter'].count_documents({})
    tot_mage = db['charactercreator_mage'].count_documents({})
    tot_necro = db['charactercreator_necromancer'].count_documents({})
    tot_thief = db['charactercreator_thief'].count_documents({})
    print('Clerics:', tot_cleric)
    print('Fighters:', tot_fighter)
    print('Mages:', tot_mage - tot_necro)
    print('Necromancer:', tot_necro)
    print('Thieves:', tot_thief)
    print('Sum:', tot_cleric + tot_fighter + (tot_mage - tot_necro) + tot_necro + tot_thief)

    # How many total items?
    tot_items = db['armory_item'].count_documents({})
    print('Total Items:', tot_items)

    # How many items are weapons? 
    tot_weapons = db['armory_weapon'].count_documents({})
    print('Total Weapons:', tot_weapons)

    # How many are not?
    # there is a cooler way to do this with filters, projections and using the
    # find method. Its also really cumbersome, so I'm doing it the easy way.
    print('Total Non-Weapons:', tot_items - tot_weapons)

    # How many items does each character have? (first 20)
    
    #this projection is to clear all the fields exept character_id, which I
    # will then use to count the documents for each. This is not very mongolike
    # because this is a clone of an sql database.  Ideally I'd keep a list of
    # the mongo hashes, or something like that.
    proj = {'_id': 0, 'dexterity': 0, 'exp': 0, 'hp': 0, 'intelligence': 0,
            'level': 0, 'name': 0, 'strength': 0, 'wisdom': 0}
    to_find = db['charactercreator_character'].find({}, projection = proj).limit(20)

    for doc in to_find:
        id = doc['character_id']

        # I only want item id
        proj = {'_id': 0, 'id': 0, 'character_id': 0}
        item_list = list(db['charactercreator_character_inventory'].find(doc, proj))

        # I could get this with a query, but it is also implicit with how I'm
        # identifying weapons.  So lets reduce the queries, thus reducing server
        # load.  Here is how I'd do it with a single query:
        # item_count = db['charactercreator_character_inventory'].count_documents(doc)
        item_count = len(item_list)

        # I can't see away around querying every single item idea a character
        # has.  This seem absurdly inefficient.  I'm blaming my inexperience 
        # and no clear pymongo documentation for array based searching (which
        # mongodb does support from the shell)
        prepped = [{'item_ptr_id': i['item_id']} for i in item_list]

        weapon_count = 0

        for i in prepped:
            weapon_count += db['armory_weapon'].count_documents(i)

        print(f'Character {id} has {item_count} items, of which {weapon_count} are weapons')

    # How many weapons does each character have? (first 20)
    
    # okay same concept, but now I need to search

    # Average, how many items does each character have?
    # TODO

    # Average, how many Weapons does each character have?
    # TODO

def postgres_queries():
    #Connect to postgres
    #TODO
    pass

    # How many passengers survived, and how many died?
    #TODO

    # How many passengers were in each class?
    # TODO

    # How many passengers survived/died within each class?
    # TODO

    # What was the average age of survivors vs nonsurvivors?
    # TODO

    # WHat was the average age of each passenger class?
    # TODO

    #What was the average fare by passenger class? By survival?
    # TODO

    # How many siblings/spouses aboard on average, by passenger class? by Survival?
    # TODO

    # How many paretns/children aboard on average, by passenger class? by survival?
    # TODO

    # Do any passengers have the same name?
    # TODO




if __name__ == "__main__":
    main()