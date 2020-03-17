import sqlite3
import pandas as pd
import os

FILEPATH = os.path.dirname(__file__)
CSV_FILEPATH = os.path.join(FILEPATH, "buddymove_holidayiq.csv")
DB_FILEPATH = os.path.join(FILEPATH, "buddymove_holidayiq.sqlite3")

# Delete .sqlite3 file of it already exists so we can make it from scratch.
if os.path.exists(DB_FILEPATH):
  os.remove(DB_FILEPATH)

df = pd.read_csv(CSV_FILEPATH)

print(df.head())

print("Shape:", df.shape)

connection = sqlite3.connect(DB_FILEPATH)
df.to_sql("buddymove_holidayiq", connection)

cursor = connection.cursor()

print("Question 1: Count how many rows you have - it should be 249!")
query = "SELECT COUNT(*) FROM buddymove_holidayiq;"
result = cursor.execute(query).fetchall()
print("ANSWER:", result[0][0])

print("\nQuestion 2: How many users who reviewed at least 100 Nature",
 "in the category also reviewed at least 100 in the Shopping category?")
query = """
SELECT COUNT(*)
FROM buddymove_holidayiq
WHERE Nature >= 100 AND Shopping >= 100
"""
result = cursor.execute(query).fetchall()
print("ANSWER:", result[0][0])

print("\nQuestion 3: What are the average number of reviews for each category?")
query = """
SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic)
FROM buddymove_holidayiq
"""
result = cursor.execute(query).fetchall()
print("Answer:")
print("Sports -", result[0][0])
print("Religious -", result[0][1])
print("Nature -", result[0][2])
print("Theatre -", result[0][3])
print("Shopping -", result[0][4])
print("Picnic -", result[0][5])
