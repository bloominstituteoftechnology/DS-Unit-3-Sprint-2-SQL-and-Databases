#!/usr/bin/env python


# "How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"
#  Working with MongoDB today was taking data several collections to make 'character' documents, that was harder
#  than moving tables from one relational database to another
# coding: utf-8

# In[190]:


import pymongo
from pymongo.operations import InsertOne
import dns
import sqlite3 as sql
import pandas as pd
import regex
import re
import os
from dotenv import load_dotenv


# In[191]:


load_dotenv()


# In[192]:


connection_string = os.getenv('ATLAS_CONNECTION_STRING')


# In[194]:


client = pymongo.MongoClient(connection_string)


# In[195]:


db = client.get_database()


# In[196]:


c = db.get_collection('cml')


# In[197]:


f = c.find_one()


# In[215]:


collection_name = 'characters'
db.drop_collection(collection_name)
db.create_collection(collection_name)


# In[218]:


rpg_db = sql.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
cursor = rpg_db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


# In[219]:


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


# In[220]:


if rpg_db.execute('SELECT i.value FROM armory_item i WHERE i.item_id = 1 ').fetchone()[0] == 0:
    L = rpg_db.execute('SELECT count(*) from armory_item').fetchone()[0]
    for i in range(L):
        rpg_db.execute(
            f" \
            UPDATE armory_item \
                SET value = {i + 100}, \
                    weight = {i + 1000} \
            WHERE armory_item.item_id = {i+1} \
            "
        )
    rpg_db.commit()


# In[221]:


# print(rpg_db.execute('SELECT w.power from armory_weapon w').fetchall())
# print(rpg_db.execute('SELECT i.value, i.weight from armory_item i').fetchall())


# In[222]:


q = """SELECT sql FROM sqlite_master
WHERE tbl_name = 'charactercreator_character' AND type = 'table'"""
columns = rpg_db.execute(q).fetchall()


# In[223]:


q = columns[0][0]
q = q[q.index('AUTOINCREMENT'):]
r = regex.findall("(?<=(?:NOT NULL|AUTOINCREMENT),\s\")(\w+)\"\s(\w+)", q)
print(r)


# In[225]:


r.insert(0, ('_id','integer'))
r


# In[226]:


requests = []
for ch in rpg_db.execute('SELECT * FROM charactercreator_character').fetchall():
#     print(ch, type(ch))
    d = {}
    for n,i in zip(r,range(len(r))):
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
    wl = [{'power': r[0], 'id': r[1], 'name': r[2], 'value': r[3], 'weight': r[4]} for r in w]
    d['weapons'] = wl
    it = list(rpg_db.execute(
        f"""
        SELECT item.item_id, item.name, item.value, item.weight FROM charactercreator_character_inventory as i JOIN
        armory_item AS item on item.item_id = i.item_id
        WHERE i.character_id = {ch[0]}
        AND item.item_id NOT IN (SELECT DISTINCT item_ptr_id FROM armory_weapon) 
        """
    ).fetchall())
    il = [{'id': r[0], 'name': r[1], 'value': r[2], 'weight': r[3]} for r in it]        
    d['items'] = il 
    requests.append(InsertOne(d));


# In[227]:


result = db.characters.bulk_write(requests)

