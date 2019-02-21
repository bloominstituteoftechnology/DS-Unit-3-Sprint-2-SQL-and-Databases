"""Import data from titanic.csv file to PostgreSQL database."""

import pymongo
import csv


# Username and password to be set by user.
username = "TODO"
password = "TODO"
cluster = "TODO"
group = "TODO"

# Open titanic.csv and read through rows to add to data.
f = open('titanic.csv', 'r')
reader = csv.reader(f)
data = []
names = None
for i, row in enumerate(reader):
    if i == 0:
        names = row[:]
    else:
        d = {}
        for j, n in enumerate(names):
            d[n] = row[j]
        data.append(d)

# Access MondoDB, create rpg_db and charactercreator_character collection,
# and add data from json file.
s = "mongodb+srv://{}:{}@{}-{}.mongodb.net/admin".format(username,
                                                         password,
                                                         cluster,
                                                         group)
client = pymongo.MongoClient(s)
dbnames = client.list_database_names()
if 'titanic' in dbnames:
    client.drop_database('titanic')
titanic_db = client["titanic"]
x = titanic_db["titanic"].insert_many(data)
# Print number of objects added to MongoDB.
print(len(x.inserted_ids))
