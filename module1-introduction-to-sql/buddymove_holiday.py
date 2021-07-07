import sqlite3

conn = sqlite3.connect('review.sqlite3')
curs = conn.cursor()

# Count the rows 
query = 'SELECT COUNT(*) FROM review;'
print(f'Total Rows: {curs.execute(query).fetchall()[0][0]}')

query2 = 'SELECT Nature AND Shopping FROM review WHERE Nature>99 AND Shopping>99;'
print(f'Users w/ > 100 Nature/Shopping Reviews: {len(curs.execute(query2).fetchall())}')

query3 = 'SELECT AVG(Nature), AVG(Shopping), AVG(Sports), AVG(Religious), AVG(Picnic), AVG(Theatre) FROM review;'

print(f'Average Nature Reviews: {curs.execute(query3).fetchall()[0][0]}')
print(f'Average Shopping Reviews: {curs.execute(query3).fetchall()[0][1]}')
print(f'Average Sports Reviews: {curs.execute(query3).fetchall()[0][2]}')
print(f'Average Religious Reviews: {curs.execute(query3).fetchall()[0][3]}')
print(f'Average Picnic Reviews: {curs.execute(query3).fetchall()[0][4]}')
print(f'Average Theatre Reviews: {curs.execute(query3).fetchall()[0][5]}')

curs.close()
conn.close()
