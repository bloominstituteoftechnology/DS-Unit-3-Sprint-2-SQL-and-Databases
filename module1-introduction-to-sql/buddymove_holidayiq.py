import sqlite3
import pandas as pd
import os

FILEPATH = os.path.join(os.path.dirname(__file__),"buddymove_holidayiq.csv")
FILEPATH2 = os.path.join(os.path.dirname(__file__),"buddymove_holidayiq.sqlite3")

df = pd.read_csv(FILEPATH)

print ("shape of pandas df: ", df.shape)

from sqlalchemy import create_engine

engine = create_engine('sqlite://, echo=False)

df.to_sql('review', con=engine)

query = "SELECT count(*) FROM review"

results = engine.execute(query).fetchall()

print ("row count of sql db: ", results)

# #  - How many users who reviewed at least 100 `Nature` in the category also
# #   reviewed at least 100 in the `Shopping` category?

# query1 = "SELECT SUM(Id) FROM review WHERE Nature > 99 and Shopping > 99"


# results1 = engine.execute(query1).fetchall()

# print (results1)


from sqlalchemy import create_engine

engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3', echo=False)

df.to_sql('review', con=engine)

conn = sqlite3.connect(FILEPATH2)

curs = conn.cursor()

query = "SELECT count(*) FROM review"

results = engine.execute(query).fetchall()

print ("row count of sql db: ", results)

print (type(df))
print (type(df2))
#  - How many users who reviewed at least 100 `Nature` in the category also
#   reviewed at least 100 in the `Shopping` category?

# query1 = "SELECT `User Id` `Nature` `Shopping` FROM review WHERE Nature > 99 and Shopping > 99"


# results1 = engine.execute(query1).fetchall()

# print (results1)