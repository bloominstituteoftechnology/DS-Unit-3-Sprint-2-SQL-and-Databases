import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
df = df.rename(mapper = (lambda x : x.replace(' ', '_')), axis=1)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

try:
    df.to_sql('review', conn)
except:
    pass

c0 = conn.cursor()
c0.execute('SELECT count(*) FROM review')
print('Total rows: '+str(c0.fetchone()[0]))

q0 = str('SELECT count(User_Id) FROM review WHERE (Nature >= 100 AND '+
         'Shopping >= 100)')
c0.execute(q0)
print('Users where Nature >= 100 and Shopping >= 100: '+str(c0.fetchone()[0]))

avgs = []
for x in df.columns[1:]:
    q1 = str('SELECT AVG({}) FROM review').format(x)
    print('Average for column {}:\t'.format(x)+
    str(c0.execute(q1).fetchone()[0]))
