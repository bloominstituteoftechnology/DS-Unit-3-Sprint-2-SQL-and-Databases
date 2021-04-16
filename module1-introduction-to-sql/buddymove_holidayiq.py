#!/usr/bin/env python3

import pandas as pd
import sqlite3
import sqlalchemy
import os 

# remove the sqlite3 file if it already exists
os.system("rm buddymove_holidayiq.sqlite3")

# Create dataframe from csv. Open connection to sqlite3, save output sqlite3
infile = "buddymove_holidayiq.csv"

df = pd.read_csv(infile)
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("buddymove_holidayiq.sqlite3", con=conn, index=False)


# perform and display SQL quereies
curs = conn.cursor()


print("\nRow count:")
query = 'select count(*) from "buddymove_holidayiq.sqlite3";'
print(curs.execute(query).fetchone()[0])




print("\nHow many users made at least 100 nature and at least 100 shopping category reviews?")
query = """
select count("User ID") 
from "buddymove_holidayiq.sqlite3" 
where Nature >= 100 and Shopping >= 100;
"""
print(curs.execute(query).fetchone()[0])




print("\n(Stretch) find average number of reviews for each category")
query = """
select avg(Sports), avg(Religious), avg(Nature), avg(Theatre), avg(Shopping), avg(Picnic)
from "buddymove_holidayiq.sqlite3";
"""
categories = "Sports Religous Nature Theatre Shopping Picnic".split()
averages = list(curs.execute(query).fetchall()[0])
for cat,av in zip(categories,averages):
    print(f"{cat}: {av}")

