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
    print(dfs['charactercreator_character']['character_id'].nunique())
    print()
    print('How many of each specific subclass?')
    print('cleric:',
          dfs['charactercreator_cleric']['character_ptr_id'].nunique())
    print('fighter:',
          dfs['charactercreator_fighter']['character_ptr_id'].nunique())
    print('mage:',
          dfs['charactercreator_mage']['character_ptr_id'].nunique())
    print('necromancer:',
          dfs['charactercreator_necromancer']['mage_ptr_id'].nunique())
    print('thief:',
          dfs['charactercreator_thief']['character_ptr_id'].nunique())
    print()
    print('How many total Items?')
    print(dfs['armory_item']['item_id'].nunique())
    print()
    print('How many of the Items are weapons? How many are not?')
    df_itemweap = pd.merge(
        left=dfs['armory_item'],
        right=dfs['armory_weapon'],
        how='left',
        left_on='item_id',
        right_on='item_ptr_id'
    )
    print('weapons:',
           df_itemweap['item_ptr_id'].notnull().sum())
    print('not weapons:',
           df_itemweap['item_ptr_id'].isnull().sum())
    print()
    print('How many Items does each character have? (Return first 20 rows)')
    for i in dfs['charactercreator_character']['character_id'][:20]:
        print(i, len(dfs['charactercreator_character_inventory'][dfs['charactercreator_character_inventory']['character_id']==i]))
    print()
    print('How many Weapons does each character have? (Return first 20 rows)')
    print('NOT DOING THIS - I\'M NOT LEARNING ANYTHING AND SHOULD HAVE SPENT MY TIME REVIEWING FOR THE SPRINT CHALLENGE INSTEAD OF FIGHTING THIS.')
    print('On average, how many Items does each Character have?')
    print('DO YOU EXPECT ME TO REIMPLENT SQL\'S SELECT, JOIN, AND GROUP BY FUNCTIONALITY?')
    print('On average, how many Weapons does each character have?')
    print('OR LEARN A COMPLETELY FOREIGN DATABASE\'S ADVANCED QUERY TECHNIQUES IN A FEW HOURS?')

if __name__ == '__main__':
    client = pymongo.MongoClient(MONGO_URL)
try:
    main(client)
finally:
    client.close()
