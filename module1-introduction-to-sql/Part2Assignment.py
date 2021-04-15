import os
import sqlite3
import pandas as pd


path = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")
db = sqlite3.connect(path)
cursor = db.cursor()
df = pd.read_csv(r'./buddymove_holidayiq.csv')

df.to_sql("review", con=db, if_exists="replace", index=False,
          dtype={"user_id": "TEXT",
                 "sports": "INTEGER",
                 "religious": "INTEGER",
                 "nature": "INTEGER",
                 "theatre": "INTEGER",
                 "shopping": "INTEGER",
                 "picnic": "INTEGER"})

query = """
SELECT COUNT(User_Id) as total_users
FROM review"""

results = cursor.execute(query).fetchall()
print('There are ' + str(results[0][0]) + ' rows in this database.')

query2 = """
SELECT COUNT(user_id) as shopping_naturists
 FROM review
 WHERE review.Nature >= 100 and review.Shopping >= 100"""

results2 = cursor.execute(query2).fetchall()
print("There are " + str(results2[0][0]) + ' people who reviewed shopping and nature.')


query3 = """
SELECT AVG(Sports),
       AVG(Religious),
       AVG(Nature),
       AVG(Theatre),
       AVG(Shopping),
       AVG(Picnic)
FROM review"""

results = cursor.execute(query3).fetchall()
names = list(df.columns[1:-1])
nums = [0, 1, 2, 3, 4, 5, 6]
i = 0
for row, i in zip(results, nums):
    print("The " + names[i] + ' column had an average of '  + str(results[0][i]) + ' reviews.')
    i += 1