import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
import sqlite3

load_dotenv()




# "How was working with MongoDB different from working with
# PostgreSQL? What was easier, and what was harder?"
 # With MongoDB, I didnt have to first create a table to store my file but instead I created a collection. 
 # MongoDB seemed less fussy about how I stored the .json file into the collection in comparison
 # to all the issues I ran into trying to store the rpg.sqlite3 file into a PostgreSQL table
 # this could have been particular to the way I went about it - and the relative ease of
 # MongoDB could be due to all the time I spent the day before trying to figure out
 # how to pass in a file from sqlite3.
 # For sqlite3 i used a copy_from to load the csv, and for mongoDB I 
 # used a json.load to copy the the json file.


# Let's try to store the RPG data in our MongoDB

FILEPATH = os.path.join(os.path.dirname(__file__),"testdata.json")


MONGO_DB_USER = os.getenv("MONGO_DB_USER", default="OOPS")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD", default="OOPS")
MONGO_CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = "mongodb+srv://Kyle_Yates_Mongo:LAMBDADS13@cluster0-t0nfl.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)

rpg_db = client['rpg_db'] # "test_database" or whatever you want to call it

with open(FILEPATH) as f:
    file_data = json.load(f)

rpg_db.insert_many(file_data)

#---------------------------------------------------------------------------------------------

# HOW TO DELETE ALL DOCUMENTS IN A COLLECTION
# AND CHECK TO SEE HOW MANY WERE DELETED:

# x = collection.delete_many({})

# print(x.deleted_count, " documents deleted.")

# Code for loading data

# HOW TO DROP THE COLLECTION FROM THE DATABASE

# rpg_db.collection.drop()

# # HOW TO PRINT ALL EXISITING COLLECTIONS IN THE DATABASE

# all_coll = rpg_db.list_collection_names()

# print(all_coll)

# #---------------------------------------------------------------------------------------------

client.close()

# rpg_db.collection.find( { status: "D" } )

# RUN THE QUERIES BELOW IN MONGODB QUERIES:
# https://docs.mongodb.com/manual/tutorial/query-documents/


# query = "SELECT COUNT(*) from charactercreator_character"

# results = curs.execute(query).fetchone()

# print ("total characters: ", results)

# rpg_db.collection.find( { status: "D" } )

# query2 = "SELECT COUNT(*) from charactercreator_cleric"

# results2 = curs.execute(query2).fetchone()

# print ("total clerics: ", results2)

# query3 = "SELECT COUNT(*) from charactercreator_fighter"

# results3 = curs.execute(query3).fetchone()

# print ("total fighters: ", results3)

# query4 = "SELECT COUNT(*) from charactercreator_mage"

# results4 = curs.execute(query4).fetchone()

# print ("total mages: ", results4)

# query5 = "SELECT COUNT(*) from charactercreator_necromancer"

# results5 = curs.execute(query5).fetchone()

# print ("total necromancers: ", results5)

# query6 = "SELECT COUNT(*) from charactercreator_thief"

# results6 = curs.execute(query6).fetchone()

# print ("total thieves: ", results6)

# query7 = "SELECT COUNT(*) from armory_item"

# results7 = curs.execute(query7).fetchone()

# print ("total items: ", results7)

# # " - How many of the Items are weapons? How many are not? "

# query8 = "SELECT COUNT(*) from armory_weapon"

# results8 = curs.execute(query8).fetchone()

# print ("total weapons: ", results8) 

# print ("non-weapon items: ",results7[0] - results8[0])

# # "How many Items does each character have? (Return first 20 rows)"

# query9 = """
# SELECT character_id, 
#     COUNT(item_id)
# FROM charactercreator_character_inventory
# GROUP BY character_id
# LIMIT 20
# """

# results9 = curs.execute(query9).fetchall()
# print ("--------------------------------------------------------------")
# print("How many items does each character have? (Return first 20 rows)")
# print ("--------------------------------------------------------------")
# for i in results9:
#     print("Character ID:",i[0], "# of Items:", i[1])
# # print ("total items per character: ", results9)


# print ("----------------------------------------------------------------")

# # How many Weapons does each character have? (Return first 20 rows)

# query10 = """
# SELECT character_id, 
#     COUNT(item_id)
# FROM charactercreator_character_inventory
# WHERE item_id > 137 and item_id < 175
# GROUP BY character_id
# LIMIT 20
# """

# results10 = curs.execute(query10).fetchall()

# print("How many Weapons does each character have? (Return first 20 rows)")
# print ("----------------------------------------------------------------")
# for i in results10:
#     print("Character ID:",i[0], "# of Weapons:", i[1])


# # On average, how many Items does each Character have?
# # Need to take # of weapons column and add every value
# # then divide by the total number of values.

# query11 = """
# SELECT character_id, 
#     COUNT(item_id)
# FROM charactercreator_character_inventory
# WHERE item_id > 137 and item_id < 175
# GROUP BY character_id
# """


# print ("-------------------------------------------------------")
# results11 = curs.execute(query11).fetchall()

# total = 0
# for i in results11:
#     total += i[1]

# print ("Average weapons of each character: ", total/len(results11))
# print ("-------------------------------------------------------")


# # On average, how many Items does each Character have?



# query12 = """
# SELECT character_id, 
#     COUNT(item_id)
# FROM charactercreator_character_inventory
# GROUP BY character_id
# """

# results12 = curs.execute(query12).fetchall()

# total2 = 0
# for i in results12:
#     total2 += i[1]

# print ("Average items of each character: ", total2/len(results12))

# print ("-------------------------------------------------------")


# client.close()

# print("DOCS:", collection.count_documents({}))


