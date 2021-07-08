"""
This module adds the RPG database from earlier this week to MongoDB.
"""

import sqlite3
import numpy as np
import pandas as pd
import pymongo
# REMOVED PASSWORD
client = pymongo.MongoClient("mongodb://will_cotton:<password>@cluster0-shard-00-00-kwojs.mongodb.net:27017,cluster0-shard-00-01-kwojs.mongodb.net:27017,cluster0-shard-00-02-kwojs.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


table_titles = ['armory_item', 'armory_weapon', 'charactercreator_character',
                'charactercreator_character_inventory',
                'charactercreator_cleric', 'charactercreator_fighter',
                'charactercreator_mage', 'charactercreator_necromancer',
                'charactercreator_thief']

table_schema_dict = {}
for table in table_titles:
    query = 'PRAGMA table_info(' + table + ');'
    curs.execute(query)
    results = curs.fetchall()
    col_names = []
    for result in results:
        col_names.append(result[1])
    table_schema_dict[table] = col_names

tables_listed = []

for table in table_titles:
    col_names = table_schema_dict[table]
    query = "SELECT * FROM " + table + ";"
    curs.execute(query)
    rows = curs.fetchall()
    table_rows_list = []
    for row in rows:
        i = 0
        row_dicted = {}
        for item in row:
            row_dicted[col_names[i]] = item
            i += 1
        table_rows_list.append(row_dicted)
    tables_listed.append(table_rows_list)

for table in tables_listed:
    db.test.insert_many(table)
