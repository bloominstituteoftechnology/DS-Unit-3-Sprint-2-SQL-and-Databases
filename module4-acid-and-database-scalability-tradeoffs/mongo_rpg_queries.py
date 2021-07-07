import pymongo
from db import ACCESS

# connect to MongoDB
client = pymongo.MongoClient(ACCESS)
db = client.test

# How many total Characters are there?
q1 = db.test.count_documents({'model': 'charactercreator.character'})
print("Number of characters:", q1)

# How many of each specific subclass?
clerics = db.test.count_documents({'model': 'charactercreator.cleric'})
print("Number of clerics:", clerics)

fighters = db.test.count_documents({'model': 'charactercreator.fighter'})
print("Number of fighters:", fighters)

mages = db.test.count_documents({'model': 'charactercreator.mage'})
print("Number of mages:", mages)

necro = db.test.count_documents({'model': 'charactercreator.necromancer'})
print("Number of necromancers:", necro)

thieves = db.test.count_documents({'model': 'charactercreator.thief'})
print("Number of thieves:", thieves)

# How many total Items?
items = db.test.count_documents({'model': 'armory.item'})
print("Number of items:", items)

# How many of the Items are weapons? How many are not?
weapons = db.test.count_documents({'model': 'armory.weapon'})
print("Number of weapons:", weapons)

print(f"Number of non-weapons: {items-weapons}")

# How many Items does each character have? (Return first 20 rows)
inventories = list(db.test.find({'model': 'charactercreator.character'},
                                {'fields.inventory': 1, '_id': 0}).limit(20))
# print(inventories)
