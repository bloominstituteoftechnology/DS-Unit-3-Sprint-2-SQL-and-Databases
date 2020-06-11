import pandas as pd
import sqlite3

### PART 2
conn_pt2 = sqlite3.connect('buddymove_holidayiq.sqlite3')
review = pd.read_csv('buddymove_holidayiq.csv')
review.to_sql('review', conn_pt2, if_exists='replace')

cur_pt2 = conn_pt2.cursor()
rows = cur_pt2.execute('SELECT count() FROM review').fetchall()
print('# of rows: ',rows)

users = cur_pt2.execute('SELECT COUNT() FROM review r WHERE r.Nature > 100 AND r.Shopping > 100').fetchall()
print('Users who reviewed both Nature and Shopping at least 100 times: ',users)