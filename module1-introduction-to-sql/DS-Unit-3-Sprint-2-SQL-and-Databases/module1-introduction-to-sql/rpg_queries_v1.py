#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:32:03 2019

@author: ggash
"""


# first import sqlite3
import sqlite3

# create variable for a conn (connection) to the data base
conn = sqlite3.connect('rpg_db.sqlite3')

# run that conn(ection) to the database
conn

# import library for directory related tools
import os 
os.listdir()


# making a mask-variable for...making a table
# making a query-table: maybe a table in which to store query results
# is 'query' the name of a function, or is this a variable?
#make_a_table = 'CREATE TABLE rpg_2 (name varchar(30), answer int);'

 
# create a cursor (an execution environment)
#curs1 = conn.cursor()

#  inspection: just checking
# review for yourself the functions you can do in cursor
#dir(curs1)

# Ask: is this necessary or just inspection?
#curs1.execute(make_a_table)

#  this closes the cursor/environment
#curs1.close()
 
 
# this maybe saves the...work done?
#conn.commit()
 
# making a new cursor for what reason?
curs2 = conn.cursor()

#print text
print ("1. How many total Characters are there?")
 
# look for a sum:
curs2.execute('SELECT count(character_id) FROM charactercreator_character;').fetchall()
print(curs2.execute('SELECT count(character_id) FROM charactercreator_character;').fetchall())


# create a mask-variable for what is to be inserted into the created table
#insert_query = 'INSERT INTO rpg_1 (question, answer) VALUES (01, 302);'

# the executes the action of inserting the results into the table that was created
#curs2.execute(insert_query)
 
# this closes the cursor/environment (why?)
curs2.close()
 
# this saves 
# Q: why is this not done before now?
conn.commit()


print ("2. How many of each specific subclass? Maning, how many subclass necramancer-mages are there?")
print ("Mage")
# for next action make a cursor/environment
curs3 = conn.cursor()
# look for a sum:
curs3.execute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall()
print(curs3.execute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall())
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_mage;').fetchall())
curs3.close()
conn.commit()


print ("cleric")
# for next action make a cursor/environment
curs4 = conn.cursor()
# look for a sum:
curs4.execute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall()
print(curs4.execute('SELECT count(character_ptr_id) FROM charactercreator_mage;').fetchall())
#print(curs3.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs4.close()
conn.commit()


print ("necromancer")
# for next action make a cursor/environment
curs5 = conn.cursor()
# look for a sum:
curs5.execute('SELECT count(mage_ptr_id) FROM charactercreator_necromancer;').fetchall()
print(curs5.execute('SELECT count(mage_ptr_id) FROM charactercreator_necromancer;').fetchall()
)
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs5.close()
conn.commit()



print ("3. How many total Items?")

# for next action make a cursor/environment
curs6 = conn.cursor()
# look for a sum:
curs6.execute('SELECT count(item_id) FROM charactercreator_character_inventory;').fetchall()
print(curs6.execute('SELECT count(item_id) FROM charactercreator_character_inventory;').fetchall())
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs6.close()
conn.commit()


print ("4. How many of the Items are weapons? How many are not?")

# try: inventory - armory: for items that are not weapons. MINUS or EXCEPT


# for next action make a cursor/environment
curs7 = conn.cursor()
# look for a sum:
curs7.execute('SELECT item_id FROM charactercreator_character_inventory EXCEPT SELECT item_id FROM armory_item;').fetchall()
print()
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs7.close()
conn.commit()


print ("5. How many Items does each character have? (Return first 20 rows)")

# try: inventory - armory: for items that are not weapons.


# for next action make a cursor/environment
curs7 = conn.cursor()
# look for a sum:
#curs7.execute('SELECT item_id FROM charactercreator_character_inventory MINUS SELECT item_id FROM armory_item;').fetchall()
print()
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs7.close()
conn.commit()


print ("6. How many Items does each character have? (Return first 20 rows)")

# try: inventory - armory: for items that are not weapons.


# for next action make a cursor/environment
curs8 = conn.cursor()
# look for a sum:
curs8.execute('SELECT item_id FROM charactercreator_character_inventory MINUS SELECT item_id FROM armory_item;').fetchall()
#print()
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs8.close()
conn.commit()

print ("7. How many Weapons does each character have? (Return first 20 rows)")

# try: inventory - armory: for items that are not weapons.


# for next action make a cursor/environment
curs9 = conn.cursor()
# look for a sum:
curs9.execute('SELECT item_id FROM charactercreator_character_inventory MINUS SELECT item_id FROM armory_item;').fetchall()
#print()
#print(curs2.execute('SELECT count(character_id) FROM charactercreator_cleric;').fetchall())
curs9.close()
conn.commit()



