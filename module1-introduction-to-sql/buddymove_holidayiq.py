import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv', index_col=False)
df.columns = df.columns.str.replace(' ', '_')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', conn, if_exists='replace')

curs = conn.cursor()

#count rows
query = 'SELECT COUNT(*) FROM review'
rows = curs.execute(query).fetchone()[0]
print(f'Row count: {rows}')

# How many users who reviewed at least 100 Nature in the category,
# also reviewed at least 100 in the Shopping category?
print('''How many users who reviewed at least 100 Nature in the category,
also reviewed at least 100 in the Shopping category?''')
query = '''
    SELECT COUNT(*)
    FROM review
    WHERE review.Nature>=100 and review.Shopping>=100
'''
reviews = curs.execute(query).fetchone()[0]
print(f'{reviews} users')