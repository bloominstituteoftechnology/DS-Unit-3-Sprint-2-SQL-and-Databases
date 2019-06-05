"""
Assignment Instructions

- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 Nature in the
  category also reviewed at least 100 in the Shopping category?
- (Stretch) What are the average number of reviews for each category?
"""

import sqlite3


# Setting global variables for connecting to the database.
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

def get_count():

    result = conn.execute('SELECT COUNT(*) FROM activities').fetchall()

    return result[0][0]

def get_cross_count():

    query = ("SELECT COUNT(*) \n"
             "FROM \n"
             "activities\n"
             "WHERE\n"
             "activities.Nature >= 100 AND\n"
             "activities.Shopping >= 100;")
    result = conn.execute(query).fetchall()

    return result[0][0]

print()