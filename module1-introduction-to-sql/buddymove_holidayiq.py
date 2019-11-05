import pandas as pd
import sqlite3

df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape)


conn = sqlite3.connect('module1-introduction-to-sql/buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn)

crs = conn.cursor()

# Count how many rows you have - it should be 249!
row_cnt = crs.execute(
    """
    SELECT count(*) FROM review
    """
).fetchone()[0]
print(f'There are {row_cnt} rows in the DB')


# How many users who reviewed at least 100 Nature in the category
#  also reviewed at least 100 in the Shopping category?
specific_users = crs.execute(
    """
    SELECT count(*)
    FROM review
    WHERE nature >= 100
    AND shopping >= 100
    """
).fetchone()[0]
print(f'There are {specific_users} users who have 100+ reviews in both the nature and shopping categories')