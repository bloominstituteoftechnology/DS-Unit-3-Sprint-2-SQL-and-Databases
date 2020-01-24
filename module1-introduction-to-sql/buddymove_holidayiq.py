import pandas as pd
import sqlite3

# Read in df
df = pd.read_csv('buddymove_holidayiq.csv')

# Generate connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Convert to SQL df
df.to_sql('review', con=conn, if_exists='replace')

# Create cursor
curs = conn.cursor()

# Confirm correct number of rows
query = '''SELECT COUNT(*)
FROM review
'''
curs.execute(query)
test = curs.fetchall()[0][0]
print("Rows:", test)

# How many users who reviewed at least 100 Nature in the
# category also reviewed at least 100 in the Shopping category?
query = '''SELECT COUNT(*)
FROM review
WHERE Nature >= 100 AND Shopping >= 100
'''
curs.execute(query)
nature_shopping = curs.fetchall()[0][0]
print("Number of high nature & shipping rows:", nature_shopping)

# Commit changes
conn.commit()
