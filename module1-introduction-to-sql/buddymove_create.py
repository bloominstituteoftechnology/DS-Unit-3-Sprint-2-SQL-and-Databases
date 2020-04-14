import pandas as pd
import sqlite3
from sqlalchemy import create_engine


df = pd.read_csv("buddymove_holidayiq.csv")
engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3', echo=False)
df.to_sql('review', con=engine, if_exists='replace')

query = """
SELECT * 
FROM review 
LIMIT 10
"""


print(engine.execute(query).fetchall())