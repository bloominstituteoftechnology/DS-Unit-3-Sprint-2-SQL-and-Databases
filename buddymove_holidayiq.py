import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# create df from csv
df = pd.read_csv('/Users/Elizabeth/sql/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

# move csv to sql
engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3', echo=False)
# df.to_sql('review', con=engine)

# Count how many rows you have - it should be 249!
answer = engine.execute("SELECT COUNT(*) FROM review;").fetchall()[0][0]
print('There are', answer, 'rows')

# How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?
query = """
        SELECT COUNT("User Id")
        FROM review
        WHERE Nature>=100 AND Shopping>=100
        """
answer = engine.execute(query).fetchall()[0][0]
print('There are {} people who reviewed at least 100 Nature and 100 Shopping'.format(answer))

# (Stretch) What are the average number of reviews for each category?
categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
for category in categories:
    query = """
            SELECT AVG({}) from review
            """.format(category)
    answer = round(engine.execute(query).fetchall()[0][0],1)
    print('The avg number of reviews for {} is:'.format(category), answer)