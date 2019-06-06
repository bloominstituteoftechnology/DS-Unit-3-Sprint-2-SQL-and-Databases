import pandas as pd 
import sqlite3

# Import CSV file

buddy = pd.read_csv('buddymove_holidayiq.csv')

# Convert to SQLITE3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
buddy.to_sql(name='review', con=conn, if_exists='replace')
curs = conn.cursor()

# Query 1 - How many rows you have? (249)

query1 = """SELECT COUNT(*) FROM review"""
result = curs.execute(query1)
print('# of Rows: ', result.fetchall()[0][0])

# Query 2 - # of Users who reviewed at least 100 Nature

query2 = """ SELECT COUNT(*)
            FROM review
            WHERE Nature >= 100 AND Shopping >=100"""

results = curs.execute(query2)
print('# of Users who reviewed at least 100 Nature & 100 Shopping: ', result.fetchall()[0][0])

# Query 3 - # AVG # Reviews for each cat
query3 = """SELECT AVG(sports),  
            AVG(Religious), 
            AVG(Nature), 
            AVG(Theatre), 
            AVG(Shopping), 
            AVG(Picnic)
            FROM review"""
result = pd.read_sql_query(query, conn)

print('Average # of Reviews for Each Cat:', result)
