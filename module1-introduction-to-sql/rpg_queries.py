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
            'AS Description FROM charactercreator_cleric ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Fighters" ' \
            'AS Description FROM charactercreator_fighter ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total_Mages" ' \
            'AS Description FROM charactercreator_mage ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Necromancers" ' \
            'AS Description FROM charactercreator_necromancer ' \
            'UNION ALL ' \
            'SELECT COUNT (*) AS Category_Count, "Total Thieves" ' \
            'AS Description FROM charactercreator_thief;'
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

def