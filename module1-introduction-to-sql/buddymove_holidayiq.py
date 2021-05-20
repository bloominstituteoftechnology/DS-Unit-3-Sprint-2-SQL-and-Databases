import pandas as pd
import sqlite3

# read in data using pandas
df = pd.read_csv('buddymove_holidayiq.csv')

# create database for csv file
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# convert df into DB for SQL use
# df.to_sql('reviews', con=conn)

# function for running queries
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

curs = conn.cursor()

# count number of rows in DB
num_rows = """
    SELECT COUNT(*)
    FROM reviews;
    """
# Answer: 249
results1 = execute_query(curs, num_rows)

# How many users who reviewed at least 100 `Nature` in the category also
#   reviewed at least 100 in the `Shopping` category?
karens = """
    SELECT COUNT(*)
FROM reviews
WHERE Nature > 100
AND Shopping > 100;
"""
# Answer: 78
results2 = execute_query(curs, karens)

# - (*Stretch*) What are the average number of reviews for each category?
avg_reviews = """
SELECT AVG(Sports), 
AVG(Religious), 
AVG(Nature), 
AVG(Shopping), 
AVG(Picnic), 
AVG(Theatre)
FROM reviews;
"""
results3 = execute_query(curs, avg_reviews)




if __name__ == '__main__':
    print(f'Report from buddymove_holidayiq \n'
        f'Number of Users: {results1[0][0]} \n'
        f'Number of Users whom have over 100: {results2[0][0]} \n'
        f'Average number of reviews Sports: Nature reviews and over 100 Shopping reviews{results3[0][0]} \n'
        f'Average number of reviews Religious:{results3[0][1]} \n'
        f'Average number of reviews Nature:{results3[0][2]} \n'
        f'Average number of reviews Shopping:{results3[0][3]} \n'
        f'Average number of reviews Picnic:{results3[0][4]} \n'
        f'Average number of reviews Theatre:{results3[0][5]} \n'
          )
