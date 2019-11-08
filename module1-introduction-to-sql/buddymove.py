import pandas as pd
import sqlite3
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

print("\nNumber of rows:")
query = "select count(*) from 'buddymove_holidayiq.sqlite3'";
print(curs.execute(query).fetchall()[0])

print("\nNumber of people who viewed > 100 Nature and Shopping:")
query = 'SELECT COUNT(*) FROM "buddymove_holidayiq.sqlite3" WHERE Nature > 100 and Shopping >100;'
print(curs.execute(query).fetchall()[0][0])
