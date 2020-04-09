#Assumption you have pandas installed in some way shape or form.  Futzing with
#and env seems a little overkill for this.

import os
import sqlite3
import pandas as pd

#Load data using pandas from buddymove_holidayiq.csv
#do this platform agnostic, expect 249X7 shape
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), 'buddymove_holidayiq.csv')
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'buddy_move_holidayiq.sqlite3')

#renaming to take care of a warning with converting to sql db later
df = pd.read_csv(CSV_FILEPATH)
df.rename(columns = {'User Id': 'User_Id'}, inplace = True)

print('The dataframe shape is:', df.shape)

#Open a connection to new db buddy_move_holidayiq.sqlite3
con = sqlite3.connect(DB_FILEPATH)
#set row factory for dict style navigation
con.row_factory = sqlite3.Row
#instantiate the current set of records
cur = con.cursor()

#us df.to_sql to insert data into a new table titled review
df.to_sql('review', con = con, if_exists = 'replace')

#SQL queries
#how many rows in the db?
q1 = '''
SELECT count(User_Id) as rows
FROM review
'''

resp = cur.execute(q1).fetchone()

print('DB has', resp['rows'])

#How many users who reviewed at least 100 Nature in the category also reviewed 
#at least 100 in the Shopping category?
q2 = '''
SELECT count(distinct User_ID) as hundo_club
FROM review as r
WHERE r.Nature >= 100 and r.Shopping >= 100
'''

resp2 = cur.execute(q2).fetchone()

print(resp2['hundo_club'], 'users reviewed at least 100 Nature and Shopping')

#Stretch what are the average number of reviews for each category?
#TODO