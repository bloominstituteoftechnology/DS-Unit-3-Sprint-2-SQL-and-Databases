# ./usr/bin/env python
" Importing from JSON to MongoDB"

from dotenv import load_dotenv
import os
import pymongo
import requests
load_dotenv()
MongoDB_URL = os.getenv("MongoDB_URL")
rpg_URL = 'https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json'

client = pymongo.MongoClient(MongoDB_URL)
database = client.rpg_database
collection = database.rpg_collection
response = requests.get(rpg_URL)
data = response.json()

result = collection.insert_many(data)

# The main difference I experienced between MongoDB and 
# SQL is that in SQL I could visualize the data in actual
# tables, the way that I'm used to seeing it.  The relations
# between datapoints on different tables are much clearer,
# which I guess is what I'd expect of relational databases.


characters = collection.count_documents(
    {'model':"charactercreator.character"})
clerics = collection.count_documents(
    {'model':"charactercreator.cleric"})
fighters = collection.count_documents(
    {'model':"charactercreator.fighter"})
mages = collection.count_documents(
    {'model':"charactercreator.mage"})
necromancers = collection.count_documents(
    {'model':"charactercreator.necromancer"})
thiefs = collection.count_documents(
    {'model':"charactercreator.thief"})


# items = sl_con.execute(
#     'SELECT * FROM armory_item;').fetchall()
# weapons = sl_con.execute(
#     'SELECT * FROM armory_weapon;').fetchall()
# non_weapons = sl_con.execute("""
#     SELECT armory_item.item_id
#        FROM armory_item LEFT JOIN armory_weapon
#        ON armory_item.item_id = armory_weapon.item_ptr_id
#        WHERE armory_weapon.item_ptr_id IS NULL;
#     """).fetchall()

print(f'Total Characters: {characters}')
print(f'Clerics:          {clerics}')
print(f'Fighters:         {fighters}')
print(f'Mages:            {mages}')
print(f'Necromancers:     {necromancers}')
print(f'Thiefs:           {thiefs}')
print()
# print(f'Total Items:      {len(items)}')
# print(f'Weapons:          {len(weapons)}')
# print(f'Non-Weapons:      {len(non_weapons)}')