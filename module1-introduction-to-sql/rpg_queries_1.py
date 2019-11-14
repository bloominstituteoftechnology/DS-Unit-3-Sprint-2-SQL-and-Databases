import os
import sqlite3


X = '/Users/ericchiyembekeza/Desktop/Lambda School/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3'

def count_chars(X):
    CONN  = sqlite3.connect(X)
    cursor1 = CONN.cursor()
    query1 = 'SELECT COUNT() FROM charactercreator_character;'
    count1 = cursor1.execute(query1).fetchall()
    return count1

def count_subs(X):
    CONN  = sqlite3.connect(X)
    cursor2 = CONN.cursor()
    query2a = 'SELECT COUNT(ccl.character_ptr_id) FROM charactercreator_cleric as ccl;'
    q2a = cursor2.execute(query2a).fetchall()
    query2b = 'SELECT COUNT(ccf.character_ptr_id) FROM charactercreator_fighter as ccf;'
    q2b = cursor2.execute(query2b).fetchall()
    query2c = 'SELECT COUNT(ccm.character_ptr_id) FROM charactercreator_mage as ccm;'
    q2c = cursor2.execute(query2c).fetchall()
    query2d = 'SELECT COUNT(cct.character_ptr_id) FROM charactercreator_thief as cct;'
    q2d = cursor2.execute(query2d).fetchall()
    query2e = 'SELECT COUNT(ccn.mage_ptr_id) FROM charactercreator_necromancer as ccn;'
    q2e = cursor2.execute(query2e).fetchall()
    return q2a, q2b, q2c, q2d, q2e

def count_items(X):
    CONN  = sqlite3.connect(X)
    cursor3 = CONN.cursor()
    query3 = 'SELECT COUNT() FROM armory_item;'
    count3 = cursor3.execute(query3).fetchall()
    return count3

def count_item_weap(X):
    CONN  = sqlite3.connect(X)
    cursor4 = CONN.cursor()
    query4a = '''SELECT COUNT(item_id)
                 FROM armory_item as ai, armory_weapon as aw
                 WHERE ai.item_id = aw.item_ptr_id;'''
    query4b = '''SELECT COUNT(DISTINCT item_id)
                 FROM armory_item as ai, armory_weapon as aw
                 WHERE ai.item_id != aw.item_ptr_id;'''
    q4a = cursor4.execute(query4a).fetchall()
    q4b = cursor4.execute(query4b).fetchall()
    return q4a, q4b

def count_char_items(X):
    CONN  = sqlite3.connect(X)
    cursor5 = CONN.cursor()
    query5 = '''SELECT character_id, COUNT(item_id)
                FROM charactercreator_character_inventory
                GROUP BY character_id
                LIMIT 20;'''
    count5 = cursor5.execute(query5).fetchall()
    return count5

def count_char_weap(X):
    CONN  = sqlite3.connect(X)
    cursor6 = CONN.cursor()
    query6 = '''SELECT character_id, COUNT(item_ptr_id)
                FROM charactercreator_character_inventory AS ccinv, armory_weapon AS aw
                WHERE ccinv.item_id = aw.item_ptr_id
                GROUP BY character_id
                LIMIT 20;'''
    count6 = cursor6.execute(query6).fetchall()
    return count6

def avg_char_items(X):
    CONN  = sqlite3.connect(X)
    cursor7 = CONN.cursor()
    query7 = '''SELECT avg(item_count)
                FROM(
                SELECT character_id, COUNT(item_id) as item_count
                FROM charactercreator_character_inventory
                GROUP BY character_id);'''
    count7 = cursor7.execute(query7).fetchall()
    return count7

def avg_char_weap(X):
    CONN  = sqlite3.connect(X)
    cursor8 = CONN.cursor()
    query8 = '''SELECT avg(weapon_count)
                FROM(
                SELECT character_id, COUNT(item_ptr_id) as weapon_count
                FROM charactercreator_character_inventory AS ccinv, armory_weapon AS aw
                WHERE ccinv.item_id = aw.item_ptr_id
                GROUP BY character_id);'''
    count8 = cursor8.execute(query8).fetchall()
    return count8
