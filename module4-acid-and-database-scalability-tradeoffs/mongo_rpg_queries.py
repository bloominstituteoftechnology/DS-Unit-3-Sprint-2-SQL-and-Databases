""" Using the previously setup mongodb collection
answer the following questions:


- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?
"""
import pymongo
import json
client = pymongo.MongoClient(
    "mongodb+srv://foobarfoobar:foobarfoobar@cluster0.vvgzp.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# rpgmdb.rpgdata # collection
c = db["rpg_data"]


c.estimated_document_count()
#collection =  db.test_collection
table_names_list = c.distinct("model")

# first set of questions:
# list containing all characters
characters = list(c.find({"model": "charactercreator.character"}))
print(f"The number of characters is {len(characters)}")

char_types = []
for t in table_names_list:
    if ("charactercreator" in t) and (".character" not in t):
        char_types.append(t)

for subclass in char_types:
    sc = list(c.find({'model': subclass}))
    print(f"The number of {subclass}s is {len(sc)}")

all_items = list(c.find({"model": "armory.item"}))
print(f"The number of total Items is: {len(all_items)}")
all_weapons = list(c.find({"model": "armory.weapon"}))
num_weapons = len(all_weapons)
print(f"\n  {num_weapons} of total Items are weapons. {len(all_items) - num_weapons} are not.")

""" number of items for each of the first 20 characters"""
for i in range(0, 20):
    print(f"The character {characters[i]['fields']['name']} has "
          f"{ len(characters[i]['fields']['inventory'])} items"
          )

"""For the first 20 characters, print the number of Weapons """

all_weapons_ids = [x['pk'] for x in all_weapons]

for i in range(0, 20):
    char_items = characters[i]['fields']['inventory']
    char_weapon_count = 0

    for item in char_items:  # check if each item in char inv is a weapon
        if item in all_weapons_ids:
            char_weapon_count += 1
    print(f"The character {characters[i]['fields']['name']} has "
          f"{char_weapon_count} weapons"
          )

total_weapon_count = 0                # initialize counter
for i in range(0, len(characters)):    # for all characters
    char_items = characters[i]['fields']['inventory']
    for item in char_items:  # check if each item in char inv is a weapon
        if item in all_weapons_ids:
            total_weapon_count += 1

print(f"""the average of the number of items per character is the total number of items
divided by the number of characters! {len(all_items)  / len(characters)} \n
Similarly the average number of weapons per charaacter is : {total_weapon_count / len(characters)}""")
