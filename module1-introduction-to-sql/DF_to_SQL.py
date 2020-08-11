import pandas as pd
import sqlite3

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
df = df.rename(columns ={'User Id':'UserId'})

# CREATE DATA BASE
conn = sqlite3.connect('Reviews.db')
c = conn.cursor()
# Create TABLE
c.execute('CREATE TABLE REVIEWS (UserId text, Sports number,Religious number, Nature number,'
          'Theatre number, Shopping number, Picnic number)')
conn.commit()

df.to_sql('REVIEWS', conn, if_exists='replace', index=False)

c.execute("""
SELECT * FROM REVIEWS


""")

for row in c.fetchall():
    print(row)
