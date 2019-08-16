import pymongo
import sqlite3

conn = sqlite3.connect('/Users/oliver/Desktop/Lambda_Projects/DS-Unit-3-Sprint-2-SQL-and-Databases-master/module1-introduction-to-sql/rpg_db.sqlite3')
curs = conn.cursor()

print(dir(conn))

client = pymongo.MongoClient("mongodb://Admin:uMMziEJm4iGV3HwB@cluster0-shard-00-00-bbrvd.mongodb.net:27017,cluster0-shard-00-01-bbrvd.mongodb.net:27017,cluster0-shard-00-02-bbrvd.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

characters = 'SELECT * FROM charactercreator_character;'
keys = ('character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom')
df = curs.execute(characters).fetchall()

def get_list_of_dict(keys, list_of_tuples):
    list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
    return list_of_dict

docs = get_list_of_dict(keys, df)
# db.test.remove({})
# db.test.insert_many(docs)

column_names = "PRAGMA table_info(charactercreator_character);"
print(list(curs))
print(list(db.test.find()))
