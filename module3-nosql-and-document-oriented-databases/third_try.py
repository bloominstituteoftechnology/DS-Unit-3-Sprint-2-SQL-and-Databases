'''
This file is the assignment Unit 3 Sprint 3 Module 3.
Wednesday, Sept. 11 2019

The objective is to move data from a sqlite db to a mongo db

Information necessary for connecting to MongoDB
-----------------
IP: 75.39.26.83
Username: jayson
password: layson
------------------'''

import sqlite3
import pymongo

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

chars = curs.execute('SELECT * FROM charactercreator_character').fetchall()

chars_dict = {'characters': chars}

# Open connection to MongoDB

client = pymongo.MongoClient("mongodb://jayson:layson@cluster0-shard-00-00-nxctz.mongodb.net:27017,cluster0-shard-00-01
