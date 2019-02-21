import pymongo
import json
import urllib.request

connection_string = 'mongodb://<USERNAME>:<PASSWORD>@cluster0-shard-00-00-pjgev.mongodb.net:27017,cluster0-shard-00-01-pjgev.mongodb.net:27017,cluster0-shard-00-02-pjgev.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
client = pymongo.MongoClient(connection_string)
db = client.test


valeries_doc = {'favorite animal': 'dolphin'}

if not db.test.find_one(valeries_doc):
    db.test.insert_one(valeries_doc)

db.test.find_one(valeries_doc)

url = 'https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json'
response = urllib.request.urlopen(url)
rpg_data = json.loads(response.read().decode())

db_rpg = client.rpg
db_rpg.rpg.insert_many(rpg_data)

# 1. How many total Characters are there?
print('Character Counts')
total_char = db_rpg.rpg.find({'model': 'charactercreator.character'})
char_count = total_char.count()
print('Total Characters', char_count)

# 2. How many of each specific subclass?
for subclass in ['fighter', 'mage', 'cleric', 'thief']:
    sub_char = db_rpg.rpg.find({'model': 'charactercreator.'+subclass})
    print('Total', subclass, ':', sub_char.count())

# 3. How many total Items?
items_count = db_rpg.rpg.find({'model': 'armory.item'}).count()
print('Total Items:', items_count)

# 4. How many of the Items are weapons? How many are not?
weapons_count = db_rpg.rpg.find({'model': 'armory.weapon'}).count()
print('Total Weapons', weapons_count)
print('Total Non-Weapons', items_count - weapons_count)

# 5. How many Items does each character have? (Return first 20 rows)
print('\nCharacter Item Counts')
for character in total_char[:20]:
    print(character['fields']['name'], len(character['fields']['inventory']))

# 6. How many Weapons does each character have? (Return first 20 rows)
print('\nCharacter Weapon Counts')
total_char = db_rpg.rpg.find({'model': 'charactercreator.character'})
weapons =  db_rpg.rpg.find({'model': 'armory.weapon'})
weapons_keys = [weapon['pk'] for weapon in weapons]
for character in total_char[:20]:
    name = character['fields']['name']
    char_items = character['fields']['inventory']
    char_weapons = len([item for item in char_items if item in weapons_keys])
    print(name, char_weapons)

# 7. On average, how many Items does each Character have?
print('\nAverage Item and Weapon Counts')
total_char = db_rpg.rpg.find({'model': 'charactercreator.character'})
total_items = 0
total_weapons = 0
for character in total_char:
    char_items = character['fields']['inventory']
    total_items += len(char_items)
    total_weapons += len([item for item in char_items if item in weapons_keys])
avg_items = total_items / char_count
print('Average Items', avg_items)

# 8. On average, how many Weapons does each character have?
avg_weapons = total_weapons / char_count
print('Average Weapons', avg_weapons)
