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
    """Queries and prints total number of characters."""
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (name) FROM charactercreator_character;'
    result = curs.execute(query)
    total_subs = result.fetchall()

    return print('Sub-Character Totals:', total_subs)


