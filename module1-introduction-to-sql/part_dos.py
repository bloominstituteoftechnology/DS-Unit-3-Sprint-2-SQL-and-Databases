import pandas as pd
import sqlite3

# Already done
# df = pd.read_csv("./buddymove_holidayiq.csv")
# df.to_sql('review', con=conn)
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Count rows
rows = curs.execute(f'''
SELECT COUNT(*) FROM review
''')
print(f'{rows.fetchall()[0][0]} rows')

# How many users who reviewed 100 Nature
# also reviewed at least 100 in shopping?
natural_shoppers = curs.execute(f'''
SELECT COUNT(DISTINCT("User Id"))
FROM review
WHERE Nature >= 100 AND Shopping >= 100;
''')
print(f'''
This is how many natural shoppers: {natural_shoppers.fetchall()[0][0]}
''')

# Average # of reviews for each category
average_for_all = curs.execute(f'''
SELECT
AVG(Sports),
AVG(Religious),
AVG(Nature),
AVG(Theatre),
AVG(Shopping),
AVG(Picnic)
FROM review;
''')
"""
average_for_all = curs.execute(f'''
SELECT
sCount,
AVG(rCount),
AVG(nCount),
AVG(tCount),
AVG(shCount),
AVG(pCount)
FROM (
    SELECT
    SUM(Sports) sCount,
    SUM(Religious) rCount,
    SUM(Nature) nCount,
    SUM(Theatre) tCount,
    SUM(Shopping) shCount,
    SUM(Picnic) pCount
    FROM review r
)
''')
"""
categories = ['Sports', 'Relig', 'Nature', 'Theatre', 'Shop', 'Picnic']
a = 0
for i in average_for_all.fetchall()[0]:
    print(f'{categories[a]}\t{i:.2f} Average number of reviews')
    # Is this sad? Lmao
    a += 1
