#!/usr/bin/env python

import pymongo
from pymongo.operations import InsertOne
import dns
import sqlite3 as sql
import pandas as pd
import regex
import re
import os
from dotenv import load_dotenv


load_dotenv()


connection_string = os.getenv('ATLAS_CONNECTION_STRING')


client = pymongo.MongoClient(connection_string)


db = client.get_database()


collection_name = 'characters'
db.drop_collection(collection_name)
db.create_collection(collection_name)

rpg_db = sql.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
cursor = rpg_db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


if rpg_db.execute('SELECT w.power FROM armory_weapon w WHERE w.item_ptr_id = 139 ').fetchone()[0] == 0:
    L = rpg_db.execute('SELECT count(*) from armory_weapon').fetchone()[0]
    for i in range(L):
        rpg_db.execute(
            f" \
            UPDATE armory_weapon \
                SET power = {i} \
            WHERE armory_weapon.item_ptr_id = {i+138} \
            "
        )
    rpg_db.commit()

if rpg_db.execute('SELECT i.value FROM armory_item i WHERE i.item_id = 1 ').fetchone()[0] == 0:
    L = rpg_db.execute('SELECT count(*) from armory_item').fetchone()[0]
    for i in range(L):
        rpg_db.execute(
            f""" 
            UPDATE armory_item 
                SET value = {i + 100}, 
                    weight = {i + 1000} 
            WHERE armory_item.item_id = {i+1} 
            """
        )
    rpg_db.commit()


q = """SELECT sql FROM sqlite_master
WHERE tbl_name = 'charactercreator_character' AND type = 'table'"""
columns = rpg_db.execute(q).fetchall()


q = columns[0][0]
q = q[q.index('AUTOINCREMENT'):]
r = regex.findall("(?<=(?:NOT NULL|AUTOINCREMENT),\s\")(\w+)\"\s(\w+)", q)
print(r)


r.insert(0, ('_id', 'integer'))


q = """
SELECT d.model AS model FROM django_content_type AS d
WHERE d.app_label=="charactercreator" and d.model != "character"
ORDER BY d.model
"""
# ensure 'mage' is before 'necromancer'
c = rpg_db.execute(q).fetchall()
type_columns = {}
for m in c:
    q = f"""
      SELECT * FROM charactercreator_{m[0]} LIMIT 0
      """
    co = rpg_db.execute(q).description
    type_columns[m[0]] = list(map(lambda x: f'cc.{x[0]}', co))
    if m[0] == 'necromancer':
        type_columns['necromancer'].remove('cc.mage_ptr_id')
    else:
        type_columns[m[0]].remove('cc.character_ptr_id')
    qs = ""
    for qc in type_columns[m[0]]:
        qs += f'{qc},'
    type_columns[m[0]] = qs[:-1]

type_columns['mage_necromancer'] = type_columns['mage'].replace('cc.', 'm.')
print(type_columns)
print(type_columns['mage'])

requests = []
for ch in rpg_db.execute('SELECT * FROM charactercreator_character').fetchall():
    d = {}
    for n, i in zip(r, range(len(r))):
        d[n[0]] = ch[i]
    w = list(rpg_db.execute(
        f"""
        SELECT w.power,item.item_id, item.name, item.value, item.weight
        FROM armory_weapon AS w JOIN armory_item AS item 
        ON item.item_id = w.item_ptr_id
		JOIN charactercreator_character_inventory i ON
		i.item_id = item.item_id 
		WHERE i.character_id = {ch[0]}
        """
    ).fetchall())
    wl = [{'power': r[0], 'id': r[1], 'name': r[2],
           'value': r[3], 'weight': r[4]} for r in w]
    d['weapons'] = wl
    it = list(rpg_db.execute(
        f"""
        SELECT item.item_id, item.name, item.value, item.weight FROM charactercreator_character_inventory as i JOIN
        armory_item AS item on item.item_id = i.item_id
        WHERE i.character_id = {ch[0]}
        AND item.item_id NOT IN (SELECT DISTINCT item_ptr_id FROM armory_weapon) 
        """
    ).fetchall())
    il = [{'id': r[0], 'name': r[1], 'value': r[2], 'weight': r[3]}
          for r in it]
    d['items'] = il
    for m in type_columns.keys():
        q = f"""
         SELECT {type_columns['necromancer']}, {type_columns['mage_necromancer']} 
         FROM charactercreator_necromancer AS cc JOIN
         charactercreator_mage AS m ON
         cc.mage_ptr_id = m.character_ptr_id
         WHERE cc.mage_ptr_id = {ch[0]}
         """ \
        \
        if m == 'necromancer' else \
             \
            f"""
         SELECT {type_columns[m]}
         FROM charactercreator_{m} AS cc
         WHERE cc.character_ptr_id = {ch[0]}            
         """
        # print('q', q, 'm', m, 'ct', ct)
        ct = rpg_db.execute(q).fetchone()
        if m == 'mage' and ct:
            q = f"""
            SELECT *
            FROM charactercreator_necromancer AS cc 
            WHERE cc.mage_ptr_id = {ch[0]}
            """
            cn = rpg_db.execute(q).fetchone()
            if cn:
                continue  # only necromancer adds necromancer
        if ct:
            columns = f"{type_columns['necromancer']}, {type_columns['mage_necromancer']}" if m == 'necromancer' else type_columns[m]
            md = {}
            for s, i in zip(columns.split(','), range(len(ct))):
                md[s[s.index('.') + 1:]] = ct[i]

            d[m] = md
            break  # character can be only one type
    requests.append(InsertOne(d))


result = db.characters.bulk_write(requests)

