"""Query rpg data from MongoDB."""

import os

import pandas as pd
import pymongo
from dotenv import load_dotenv

# establish environment
assert load_dotenv() == True, 'Unable to load .env'
MONGO_URL = os.getenv('MONGO_URL')
assert MONGO_URL is not None, 'MONGO_URL not found in environment'

DB_NAME = 'rpg_db'


def drop_collection_if_present(db, collection_name):
    """Drops a MongoDB collection if present in the database."""
    if collection_name in db.list_collection_names():
        db.drop_collection(collection_name)
    return


def main(client):
    assert DB_NAME in client.list_database_names()
    db = client[DB_NAME]
    # get all collections
    dfs = {
        collection: pd.DataFrame(list(db[collection].find())).drop(
            columns='_id',
            errors='ignore'
        )
        for collection in db.list_collection_names()
    }
    print('How many total Characters are there?')
    print(dfs['charactercreator_character']['character_id'].nunique(),
          len(db.charactercreator_character.distinct('character_id')))
    print()
    print('How many of each specific subclass?')
    print('cleric:',
          dfs['charactercreator_cleric']['character_ptr_id'].nunique(),
          len(db.charactercreator_cleric.distinct('character_ptr_id')))
    print('fighter:',
          dfs['charactercreator_fighter']['character_ptr_id'].nunique(),
          len(db.charactercreator_fighter.distinct('character_ptr_id')))
    print('mage:',
          dfs['charactercreator_mage']['character_ptr_id'].nunique(),
          len(db.charactercreator_mage.distinct('character_ptr_id')))
    print('necromancer:',
          dfs['charactercreator_necromancer']['mage_ptr_id'].nunique(),
          len(db.charactercreator_necromancer.distinct('mage_ptr_id')))
    print('thief:',
          dfs['charactercreator_thief']['character_ptr_id'].nunique(),
          len(db.charactercreator_thief.distinct('character_ptr_id')))
    print()
    print('How many total Items?')
    print(dfs['armory_item']['item_id'].nunique(),
          len(db.armory_item.distinct('item_id')))
    print()
    print('How many of the Items are weapons? How many are not?')
    # merge items and weapons dataframes
    df_itemweap = pd.merge(
        left=dfs['armory_item'],
        right=dfs['armory_weapon'],
        how='left',
        left_on='item_id',
        right_on='item_ptr_id'
    )
    # merge items and weapons collections
    drop_collection_if_present(db, 'armory_item_weapon')
    db.armory_item_weapon.insert_many([
        doc for doc in db.armory_item.aggregate([
            {
                '$lookup': {
                    'from': 'armory_weapon',
                    'localField': 'item_id',
                    'foreignField': 'item_ptr_id',
                    'as': 'weapon'
                }
            }
        ])
    ])
    print('weapons:',
           df_itemweap['item_ptr_id'].notnull().sum(),
           len(db.armory_weapon.distinct('item_ptr_id')))
    print('not weapons:',
           df_itemweap['item_ptr_id'].isnull().sum(),
           db.armory_item.count_documents({'item_id':
                {'$nin': db.armory_weapon.distinct('item_ptr_id')}}),
           db.armory_item_weapon.count_documents({
               'weapon': {'$size' : 0}
           }))
    print()
    print('How many Items does each character have? (Return first 20 rows)')
    for i in dfs['charactercreator_character']['character_id'][:20]:
        print(i, len(dfs['charactercreator_character_inventory'][dfs['charactercreator_character_inventory']['character_id']==i]))
    print()
    print('How many Weapons does each character have? (Return first 20 rows)')
    print('On average, how many Items does each Character have?')
    print('On average, how many Weapons does each character have?')

if __name__ == '__main__':
    client = pymongo.MongoClient(MONGO_URL)
try:
    main(client)
finally:
    client.close()
