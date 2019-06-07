#!/usr/bin/env python

import sqlite3

"""Tools for querying the rpg_db."""


def character_count():
    """Queries and prints total number of characters."""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM charactercreator_character;'
    result = curs.execute(query)
    total_characters = result.fetchall()

    return print('Total Characters:', total_characters[0][0])


def sub_characters_count():
    """Queries and prints total number of sub-characters."""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) AS Category_Count, "Total Clerics" ' \
            'AS Sub_Character FROM charactercreator_cleric ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Fighters" ' \
            'AS Sub_Character FROM charactercreator_fighter ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total_Mages" ' \
            'AS Sub_Character FROM charactercreator_mage ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Necromancers" ' \
            'AS Sub_Character FROM charactercreator_necromancer ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Thieves" ' \
            'AS Sub_Character FROM charactercreator_thief;'
    result = curs.execute(query)
    total_subs = result.fetchall()

    return print('Sub-Character Totals:', total_subs)


def total_items_count():
    """Queries and prints the total items."""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM charactercreator_character_inventory;'
    result = curs.execute(query)
    total_items = result.fetchall()

    return print('Total Items:', total_items[0][0])


def weapons_vs_nonweapons():
    """Queries the total weapons and non-weapons"""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) AS Inventory_Count, "Weapons"' \
            'AS Items FROM charactercreator_character_inventory ' \
            'WHERE id BETWEEN 138 AND 174 '\
            'UNION ALL '\
            'SELECT COUNT (*) AS Inventory_Count, "Non-Weapons" '\
            'AS Items FROM charactercreator_character_inventory '\
            'WHERE id NOT BETWEEN 138 AND 174;'
    result = curs.execute(query)
    total_w_vs_nw = result.fetchall()

    return print('Weapon vs Non-Weapons:', total_w_vs_nw)

def num_weapons_per_character():
    """Queries the number of weapons of each character."""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = ''
    result = curs.execute(query)
    character_weapons = result.fetchall()

    return print("Number of Weapons per Character:", character_weapons)
