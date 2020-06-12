import pandas as pd
import sqlite3
# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv")

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
# df.to_sql("review",con=conn)

# count how many rows you have

print(conn.execute("SELECT COUNT(*) FROM review;").fetchall())

print(conn.execute("SELECT * FROM review WHERE Nature >= 100 LIMIT 10;").fetchall())

print(conn.execute("SELECT AVG(Sports),AVG(Religious),AVG(Nature),AVG(Theatre),AVG(Shopping),AVG(Picnic) FROM review;").fetchall())