import pandas as pd
import sqlite3
import os

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cur = conn.cursor()
CSV_FILEPATH = os.path.join(os.path.dirname(
    __file__), 'buddymove_holidayiq.csv')
df = pd.read_csv(CSV_FILEPATH)
# print(df.head())
print(df.shape)

cur.execute('DROP TABLE IF EXISTS Reviews;')
cur.execute(
    'CREATE TABLE Reviews(user_id, sports, religious, nature, theatre, shopping, picnic);')

df.to_sql('Reviews', conn, if_exists='replace', index=False)
print('Count how many rows you have')
query_1 = 'SELECT COUNT(*) FROM Reviews'
result_1 = cur.execute(query_1).fetchone()
print(result_1)

print('How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
query_2 = 'SELECT COUNT(*) FROM Reviews r where r.nature >= 100 AND r.shopping >= 100'
result_2 = cur.execute(query_2).fetchone()
print(result_2)

print('(Stretch) What are the average number of reviews for each category?')
query_3 = 'SELECT AVG(sports) , AVG(religious), AVG(nature), AVG(theatre), AVG(shopping)FROM Reviews'
result_3 = cur.execute(query_3).fetchone()
[print("{:.2f}".format(int(i))) for i in result_3]
