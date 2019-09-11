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

tables = curs.execute("""
      SELECT name
      FROM sqlite_master
      WHERE type='table';""").fetchall()

table_dict = {}
for table in tables:
    data = curs.execute('SELECT * FROM {}'.format(table)).fetchall()
    table_dict.append(dict(table, data))
table_dict.keys
