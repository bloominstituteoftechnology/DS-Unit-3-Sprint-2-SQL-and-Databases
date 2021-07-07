import sqlite3
import pandas as pd
import os

FILEPATH = os.path.join(os.path.dirname(__file__),"buddymove_holidayiq.csv")

df = pd.read_csv(FILEPATH)
print("------------------------------")
print ("shape of pandas df: ", df.shape)
print("------------------------------")
from sqlalchemy import create_engine

engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3', echo=False)

df.to_sql('review', con=engine, if_exists='replace')

results = engine.execute("SELECT count(*) FROM review").fetchall()

print("row count of sql db: ", results)
print("------------------------------------------------------------")
query = '''
SELECT
COUNT(DISTINCT "index")
FROM review
WHERE Nature >= 100 AND Shopping >= 100
;
'''

results2 = engine.execute(query).fetchall()

print("users who reviewed at least 100 Nature and Shopping: ", results2[0][0])

# (*Stretch*) What are the average number of reviews for each category?

query1 = '''
SELECT *
FROM review
;
'''

results3 = engine.execute(query1).fetchall()

sports = 0
religious = 0
nature = 0
theatre = 0
shopping = 0
picnic = 0
for i in results3:
    sports += i[2]
    religious += i[3]
    nature += i[4]
    theatre += i[5]
    shopping += i[6]
    picnic += i[7]
  

print("------------------------------------------------------------")
print("Average number of reviews for sports: ", sports/len(results3))
print("------------------------------------------------------------")
print("Average number of reviews for religious: ", religious/len(results3))
print("------------------------------------------------------------")
print("Average number of reviews for nature: ", nature/len(results3))
print("------------------------------------------------------------")
print("Average number of reviews for theatre: ", theatre/len(results3))
print("------------------------------------------------------------")
print("Average number of reviews for shopping: ", shopping/len(results3))
print("------------------------------------------------------------")
print("Average number of reviews for picnic: ", picnic/len(results3))
print("------------------------------------------------------------")

