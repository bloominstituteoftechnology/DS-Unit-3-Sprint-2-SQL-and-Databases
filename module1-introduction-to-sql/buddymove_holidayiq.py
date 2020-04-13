import sqlite3
import pandas as pd
import os

FILEPATH = os.path.join(os.path.dirname(__file__),"buddymove_holidayiq.csv")

df = pd.read_csv(FILEPATH)

print ("shape of pandas df: ", df.shape)

from sqlalchemy import create_engine

engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3', echo=False)

df.to_sql('review', con=engine, if_exists='replace')

results = engine.execute("SELECT count(*) FROM review").fetchall()

print("row count of sql db: ", results)

query = '''
SELECT
COUNT(DISTINCT "index")
FROM review
WHERE Nature >= 100 AND Shopping >= 100
;
'''

results2 = engine.execute(query).fetchall()

print("users who reviewed at least 100 Nature and Shopping: ", results2[0][0])

