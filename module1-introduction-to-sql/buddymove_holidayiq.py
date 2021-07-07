import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn, if_exists='replace')

def sql_fetch(conn):
    cursor = conn.cursor()

    """ Get total number of rows"""

    query1 = '''SELECT count(*)
            FROM review;'''
    cursor.execute(query1)
    rows = cursor.fetchall()
    for row in rows:
        print(f'Total number of rows: {row[0]}')


    """ How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?"""

    query2 = '''SELECT COUNT("User Id")from review
            WHERE Nature >= 100 AND Shopping >=100;'''
    cursor.execute(query2)
    rows2 = cursor.fetchall()
    for row in rows2:
        print(f'Users who reviewed at least 100 Nature and Shopping: {row[0]}')


    """What are the average number of reviews for each category?"""

    query3 = '''SELECT AVG(Sports), AVG(Religious), AVG(Nature),
            AVG(Theatre), AVG(Shopping), AVG(Picnic)
            FROM review'''

    cursor.execute(query3)
    rows3 = cursor.fetchall()
    rows_result = [item for t in rows3 for item in t]
    labels = ['Sports','Religious','Nature','Theatre','Shopping', 'Picnic']
    for label, row in zip(labels, rows_result):
        print(f'Avergage number of {label} reviews: {row:.2f}')

    cursor.close()
    conn.commit()

sql_fetch(conn)

