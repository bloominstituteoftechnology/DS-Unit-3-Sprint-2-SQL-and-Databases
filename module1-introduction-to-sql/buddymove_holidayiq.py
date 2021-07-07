import pandas as pd
import sqlite3


df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# the line below is commented out because it only needed to be run once
# df.to_sql('review', con=conn)
c = conn.cursor()

q1 = 'SELECT COUNT([User Id]) FROM review'
UserIds1 = c.execute(q1)
Users1 = UserIds1.fetchone()[0]

q2 = 'SELECT COUNT([User Id]) FROM (SELECT *\
                                    FROM review\
                                    WHERE Nature > 100 \
                                    AND Shopping > 100)'
UserIds2 = c.execute(q2)
Users2 = UserIds2.fetchone()[0]

print(f'There are {Users1} total users')
print(f'{Users2} users have made at least 100 Nature AND Shopping reviews')
