#!/usr/bin/env python3

import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("buddymove_holidayiq.sqlite3", con=conn, index=False)

curs = conn.cursor()

print("\nHow many rows are there?")
query = """
SELECT 'User Id', COUNT(*)
FROM "buddymove_holidayiq.sqlite3";
"""
print(curs.execute(query).fetchone()[1])

print(
    "\nHow many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?")
query = """
SELECT 'User Id', COUNT(*)
FROM "buddymove_holidayiq.sqlite3"
WHERE Nature >= 100 AND Shopping >= 100;
"""
print(curs.execute(query).fetchone()[1])

print("\nWhat are the average number of reviews for each category?")
category_list = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
for cat in category_list:
    query = f"SELECT AVG({cat}) FROM 'buddymove_holidayiq.sqlite3';"
    print(f"{cat}:", curs.execute(query).fetchone()[0])
