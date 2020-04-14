import pandas as pd
import sqlite3

df = pd.read_csv("buddymove_holidayiq.csv")
connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("review", connection)

print(connection.execute("SELECT * FROM review LIMIT 10").fetchall())