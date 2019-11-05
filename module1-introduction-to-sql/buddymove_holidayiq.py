import sqlite3, os
import pandas as pd


DF_URL = "buddymove_holidayiq.csv"
SQL_FNAME = "buddymove_holidayiq.sqlite3"


df = pd.read_csv(DF_URL) # Load dataframe
if os.path.exists(SQL_FNAME): # Delete DB if exists
    os.remove(SQL_FNAME)
conn = sqlite3.connect(SQL_FNAME) # Create database and convert dataframe
df.to_sql("review", con=conn)

curs = conn.cursor() # Connect and query the data
print("Length of DB:", curs.execute("SELECT COUNT(*) FROM review;").fetchall())
print("Length where Shopping and Nature >=100:", curs.execute("SELECT COUNT(*) FROM review WHERE Shopping >= 100 AND Nature >= 100;").fetchall())
print("Mean Sports Rating", curs.execute("SELECT AVG(Sports) FROM review;").fetchall())
print("Mean Religious Rating", curs.execute("SELECT AVG(Religious) FROM review;").fetchall())
print("Mean Nature Rating", curs.execute("SELECT AVG(Nature) FROM review;").fetchall())
print("Mean Theatre Rating", curs.execute("SELECT AVG(Theatre) FROM review;").fetchall())
print("Mean Shopping Rating", curs.execute("SELECT AVG(Shopping) FROM review;").fetchall())
print("Mean Picnic Rating", curs.execute("SELECT AVG(Picnic) FROM review;").fetchall())

conn.commit() # Close all connections/cursors
curs.close()
conn.close()
